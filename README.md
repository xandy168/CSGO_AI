YOLOv3 Aimbot

軟體撰寫 XANDY @ 2025/03/31 / 聯繫方式  Contact : xandy168@gmail.com 

源代碼&執行檔下載：https://1drv.ms/f/c/2a09a0ec12e1b46d/EmGdKxHxmO9MqpfHHQM4OugBO0_4Ully5dcgEErOwDDdgg?e=2TGX0T

使用說明：下載程式後直接執行CSGO.EXE即可於遊戲中使用，按下Ctrl+Q啟動描準功能，按下Ctrl+W關閉描準功能。

項目概述 / Project Overview
這個項目是一個基於 YOLOv3 的自動描準程式（Aimbot），利用實時螢幕截圖和目標檢測技術，識別螢幕中的“人”並控制滑鼠移動和點擊。程式支援 1080p (1920x1080) 和 4K (3840x2160) 解析度的顯示器，並可通過快捷鍵啟動或關閉描準功能。

This project is an automatic aiming program (Aimbot) based on YOLOv3. It uses real-time screen capture and object detection to identify "people" on the screen and control mouse movement and clicks. The program supports 1080p (1920x1080) and 4K (3840x2160) resolution displays, with the ability to enable or disable the aimbot via hotkeys.

功能 / Features
目標檢測：使用 YOLOv3 模型檢測螢幕中的“人”。
自動描準：將滑鼠移動到檢測到的目標中心並模擬點擊。
快捷鍵控制：Ctrl+Q 啟動描準，Ctrl+W 關閉描準。
解析度支援：適配 1080p 和 4K 顯示器，並支援其他非標準解析度。
時間日誌：顯示滑鼠移動和點擊的執行時間。
Object Detection: Uses the YOLOv3 model to detect "people" on the screen.
Auto-Aiming: Moves the mouse to the center of detected targets and simulates a click.
Hotkey Control: Ctrl+Q to enable aiming, Ctrl+W to disable aiming.
Resolution Support: Compatible with 1080p and 4K displays, with fallback for non-standard resolutions.
Time Logging: Displays execution time for mouse movement and clicks.
使用說明 / Usage Instructions
啟動程式：
運行 python aimbot.py。
程式會自動檢測螢幕解析度並顯示當前模式（1080p、4K 或默認）。
控制描準：
按 Ctrl+Q 啟動描準功能。
按 Ctrl+W 關閉描準功能。
觀察輸出：
控制台會顯示滑鼠移動和點擊的時間（例如：移動時間: 0.012s, 點擊時間: 0.001s）。
Start the Program:
Run python aimbot.py.
The program will detect your screen resolution and display the current mode (1080p, 4K, or default).
Control Aiming:
Press Ctrl+Q to enable the aimbot.
Press Ctrl+W to disable the aimbot.
Monitor Output:
The console will display the time taken for mouse movement and clicks (e.g., Move time: 0.012s, Click time: 0.001s).
安裝步驟 / Installation Steps
環境需求 / Requirements
Python 3.6+
PyTorch（支援 CUDA 可選）
OpenCV (opencv-python)
PyAutoGUI (pyautogui)
Pillow (pillow)
Keyboard (keyboard)
NumPy (numpy)
安裝依賴 / Install Dependencies
bash

收起

換行

複製
pip install torch torchvision opencv-python pyautogui pillow keyboard numpy
下載 YOLOv3 權重 / Download YOLOv3 Weights
從以下連結下載 yolov3.weights：
官方下載連結
將文件放置在項目根目錄，或修改程式中的 weightsfile 參數指向正確路徑。
準備配置文件 / Prepare Configuration File
確保 cfg/yolov3.cfg 文件存在於項目目錄中。若無，可從 YOLO 官方網站 下載。
運行程式 / Run the Program
bash

收起

換行

複製
python aimbot.py
注意事項 / Notes
硬體需求：
4K 解析度需要較高的計算能力，建議使用 GPU（CUDA 支援）。
確保顯示器解析度正確檢測，避免截圖範圍超出螢幕。
滑鼠縮放係數：
1080p 使用 1.56，4K 使用 3.12。若描準不準確，可根據實際需求調整 mouse_scale_factor。
依賴文件：
程式假設 util.py 和 darknet.py 已實現並包含必要的函數（prep_image 和 write_results）。若缺少這些文件，需自行實現或從 YOLOv3 官方實現中獲取。
法律與道德：
本程式僅用於學習和研究目的。請勿在遊戲或其他未經授權的環境中使用，以免違反相關規定。
Hardware Requirements:
4K resolution requires higher computational power; a GPU with CUDA support is recommended.
Ensure the screen resolution is detected correctly to avoid capturing beyond the screen boundaries.
Mouse Scaling Factor:
1080p uses 1.56, 4K uses 3.12. Adjust mouse_scale_factor if aiming is inaccurate.
Dependent Files:
The program assumes util.py and darknet.py are implemented with required functions (prep_image and write_results). If missing, implement them or obtain from the official YOLOv3 repository.
Legal and Ethical Considerations:
This program is for educational and research purposes only. Do not use it in games or unauthorized environments to avoid violating regulations.
程式結構 / Project Structure
text

收起

換行

複製
aimbot/
├── aimbot.py         # 主程式
├── cfg/
│   └── yolov3.cfg   # YOLOv3 配置文件
├── yolov3.weights   # YOLOv3 權重文件
├── util.py          # 工具函數（需自行實現）
├── darknet.py       # Darknet 模型實現（需自行實現）
└── README.md        # 本說明文件
聯繫方式 / Contact : xandy168@gmail.com 
如有問題或建議，請通過 GitHub Issues 聯繫。

For questions or suggestions, please reach out via GitHub Issues.
