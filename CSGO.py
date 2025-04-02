from __future__ import division
import time
import numpy as np
import cv2
from PIL import ImageGrab
import pyautogui
import keyboard
from ultralytics import YOLO
import torch

# 全局變數：控制描準功能的開關
aimbot_enabled = False

# 快捷鍵回調函數
def toggle_aimbot_on():
    global aimbot_enabled
    aimbot_enabled = True
    print("描準功能已啟動 (Ctrl+Q)")

def toggle_aimbot_off():
    global aimbot_enabled
    aimbot_enabled = False
    print("描準功能已關閉 (Ctrl+W)")

# 綁定組合鍵
keyboard.add_hotkey("ctrl+q", toggle_aimbot_on)
keyboard.add_hotkey("ctrl+w", toggle_aimbot_off)

# 檢查並優先使用 GPU (CUDA)
print("檢查 CUDA 可用性...")
if not torch.cuda.is_available():
    print("錯誤: CUDA 不可用，將回退到 CPU 模式，這將顯著降低性能。")
    print("請確認以下項目：")
    print("1. 是否有 NVIDIA GPU 並已安裝最新驅動程式 (檢查 nvidia-smi)。")
    print("2. 是否已安裝 CUDA Toolkit (檢查 nvcc --version)。")
    print("3. 是否已安裝 cuDNN。")
    print("4. 是否安裝支援 CUDA 的 PyTorch (檢查 torch.__version__)。")
    device = torch.device("cpu")
    print("使用設備: CPU")
else:
    device = torch.device("cuda")
    print(f"CUDA 可用，使用 GPU: {torch.cuda.get_device_name(0)}")
    print(f"CUDA 版本: {torch.version.cuda}")
    print(f"PyTorch 版本: {torch.__version__}")
    torch.cuda.set_device(0)  # 明確指定使用第一個 GPU

# 初始化 YOLOv11 模型並移動到 GPU
print("載入 YOLOv11 模型到 GPU...")
try:
    model = YOLO("yolo11n.pt").to(device)  # 將模型載入指定設備
    print("模型載入成功.")
except Exception as e:
    print(f"載入模型時發生錯誤: {e}")
    print("請從 https://github.com/ultralytics/ultralytics 下載 YOLOv11 權重文件")
    exit(1)

# 設置參數
confidence = 0.5  # 置信度閾值
inp_dim = 640     # YOLOv11 默認輸入分辨率

# 動態調整截圖範圍和滑鼠縮放係數根據顯示器解析度
screen_width, screen_height = pyautogui.size()
print(f"檢測到螢幕解析度: {screen_width}x{screen_height}")

if screen_width == 1920 and screen_height == 1080:  # 1080p
    capture_width = 1280
    capture_height = 720
    mouse_scale_factor = 1.56
    print("設定為 1080p 模式")
elif screen_width == 3840 and screen_height == 2160:  # 4K
    capture_width = 2560
    capture_height = 1440
    mouse_scale_factor = 3.12
    print("設定為 4K 模式")
else:  # 默認設置
    capture_width = min(1280, screen_width)
    capture_height = min(468, screen_height - 32)
    mouse_scale_factor = 1.56
    print("使用默認模式（非標準解析度）")

capture_width = min(capture_width, screen_width)
capture_height = min(capture_height, screen_height - 32)

# 主迴圈
print("程式已啟動，按 Ctrl+Q 開啟描準，Ctrl+W 關閉描準")
while True:
    try:
        MouseX, MouseY = pyautogui.position()
        # 動態截圖範圍
        frame = ImageGrab.grab((0, 32, capture_width, 32 + capture_height))
        frame = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)

        # 將圖像數據轉換為 PyTorch 張量並移動到 GPU
        frame_tensor = torch.from_numpy(frame).to(device).permute(2, 0, 1).float() / 255.0
        frame_tensor = frame_tensor.unsqueeze(0)  # 添加批次維度

        # 使用 YOLOv11 進行目標檢測（優先在 GPU 上運行）
        results = model.predict(frame, conf=confidence, imgsz=inp_dim, verbose=False, device=device)

        # 處理檢測結果
        if aimbot_enabled and len(results) > 0:
            detections = results[0].boxes  # 獲取檢測框
            person_detections = [box for box in detections if box.cls == 0]  # 0 為 "person" 類別

            if not person_detections:
                continue

            # 計算最近的人目標
            min_dist = float("inf")
            target_box = None
            for box in person_detections:
                x1, y1, x2, y2 = box.xyxy[0].cpu().tolist()  # 將座標移回 CPU 進行計算
                center_x = (x1 + x2) / 2
                center_y = (y1 + y2) / 2
                dist = ((center_x - MouseX) ** 2 + (center_y - MouseY) ** 2) ** 0.5
                if dist < min_dist:
                    min_dist = dist
                    target_box = (x1, y1, x2, y2)

            if target_box:
                x1, y1, x2, y2 = target_box
                target_x = (x1 + x2) / 2 - MouseX
                target_y = 0.6 * y1 + 0.4 * y2 - MouseY  # 頭部偏上的位置

                # 使用動態縮放係數調整滑鼠移動
                move_x = target_x / mouse_scale_factor
                move_y = target_y / mouse_scale_factor

                A = time.time()
                pyautogui.moveRel(move_x, move_y)
                B = time.time()
                pyautogui.click()
                C = time.time()
                print(f"移動時間: {B-A:.3f}s, 點擊時間: {C-B:.3f}s")

        time.sleep(0.01) # 控制迴圈速度

    except Exception as e:
        print(f"運行時錯誤: {e}")
        time.sleep(1)