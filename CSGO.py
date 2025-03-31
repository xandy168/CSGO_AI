from __future__ import division
import time
import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
import cv2
from util import *
import argparse
import os
import os.path as osp
from darknet import Darknet
import pickle as pkl
import pandas as pd
import random
from PIL import ImageGrab
import pyautogui
import keyboard  # 用於快捷鍵處理

# 定義參數解析函數
def arg_parse():
    parser = argparse.ArgumentParser(description='YOLO v3 檢測模型')
    parser.add_argument("--bs", dest="bs", help="批次大小，預設為 1", default=1)
    parser.add_argument("--confidence", dest="confidence", help="目標檢測結果置信度閾值", default=0.5)
    parser.add_argument("--nms_thresh", dest="nms_thresh", help="NMS非極大值抑制閾值", default=0.4)
    parser.add_argument("--cfg", dest='cfgfile', help="配置文件", default="cfg/yolov3.cfg", type=str)
    parser.add_argument("--weights", dest='weightsfile', help="模型權重", default="yolov3.weights", type=str)
    parser.add_argument("--reso", dest='reso', help="網絡輸入分辨率", default="416", type=str)
    return parser.parse_args()

# 初始化參數
args = arg_parse()
batch_size = int(args.bs)
confidence = float(args.confidence)
nms_thesh = float(args.nms_thresh)
CUDA = torch.cuda.is_available()
num_classes = 80  # COCO 數據集有 80 類

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

# 初始化網絡並載入權重
print("載入神經網絡....")
try:
    model = Darknet(args.cfgfile)
    if not os.path.exists(args.weightsfile):
        raise FileNotFoundError(f"權重文件未找到: {args.weightsfile}")
    model.load_weights(args.weightsfile)
    print("模型載入成功.")
except FileNotFoundError as e:
    print(f"錯誤: {e}")
    print("請從 https://pjreddie.com/media/files/yolov3.weights 下載權重文件並放置在正確位置")
    exit(1)
except Exception as e:
    print(f"載入模型時發生未知錯誤: {e}")
    exit(1)

model.net_info["height"] = args.reso
inp_dim = int(model.net_info["height"])
assert inp_dim % 32 == 0 and inp_dim > 32

if CUDA:
    model.cuda()
model.eval()

# 動態調整截圖範圍和滑鼠縮放係數根據顯示器解析度
screen_width, screen_height = pyautogui.size()  # 獲取螢幕寬高
print(f"檢測到螢幕解析度: {screen_width}x{screen_height}")

# 根據解析度設置參數
if screen_width == 1920 and screen_height == 1080:  # 1080p
    capture_width = 1280
    capture_height = 720
    mouse_scale_factor = 1.56  # 1080p 的滑鼠縮放係數
    print("設定為 1080p 模式")
elif screen_width == 3840 and screen_height == 2160:  # 4K
    capture_width = 2560
    capture_height = 1440
    mouse_scale_factor = 3.12  # 4K 的滑鼠縮放係數（2 倍 1080p）
    print("設定為 4K 模式")
else:  # 默認設置（其他解析度）
    capture_width = min(1280, screen_width)
    capture_height = min(468, screen_height - 32)
    mouse_scale_factor = 1.56  # 默認縮放係數
    print("使用默認模式（非標準解析度）")

# 確保截圖範圍不超出螢幕
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

        img = prep_image(frame, inp_dim)
        im_dim = frame.shape[1], frame.shape[0]
        im_dim = torch.FloatTensor(im_dim).repeat(1, 2)

        if CUDA:
            im_dim = im_dim.cuda()
            img = img.cuda()

        with torch.no_grad():
            output = model(Variable(img), CUDA)
        output = write_results(output, confidence, num_classes, nms_conf=nms_thesh)

        if type(output) == int:
            continue

        # 後續座標處理（僅在描準功能啟動時執行）
        if aimbot_enabled:
            im_dim = im_dim.repeat(output.size(0), 1)
            scaling_factor = torch.min(int(args.reso) / im_dim, 1)[0].view(-1, 1)
            output[:, [1, 3]] -= (inp_dim - scaling_factor * im_dim[:, 0].view(-1, 1)) / 2
            output[:, [2, 4]] -= (inp_dim - scaling_factor * im_dim[:, 1].view(-1, 1)) / 2
            output[:, 1:5] /= scaling_factor
            for i in range(output.shape[0]):
                output[i, [1, 3]] = torch.clamp(output[i, [1, 3]], 0.0, im_dim[i, 0])
                output[i, [2, 4]] = torch.clamp(output[i, [2, 4]], 0.0, im_dim[i, 1])

            output = output[output[:, 7] == 0, :]  # 只保留“人”
            if output.shape[0] == 0:
                continue

            x = output[:, 1] + output[:, 3]
            x = x / 2 - MouseX
            _, index_x = torch.min(abs(x), 0)
            x = int(x[index_x])

            y = 0.6 * output[index_x][2] + 0.4 * output[index_x][4]
            y = int(y) - MouseY

            # 使用動態縮放係數調整滑鼠移動
            currentMouseX = x / mouse_scale_factor
            currentMouseY = y / mouse_scale_factor

            A = time.time()
            pyautogui.moveRel(currentMouseX, currentMouseY)
            B = time.time()
            pyautogui.click()
            C = time.time()
            print(f"移動時間: {B-A:.3f}s, 點擊時間: {C-B:.3f}s")

        time.sleep(0.2)  # 控制迴圈速度

    except Exception as e:
        print(f"運行時錯誤: {e}")
        time.sleep(1)  # 避免過快重試