YOLOv3 Aimbot

�n�鼶�g XANDY @ 2025/03/31 / �pô�覡  Contact : xandy168@gmail.com 

�ϥλ����G�U���{���᪽������CSGO.EXE�Y�i��C�����ϥΡA���UCtrl+Q�Ұʴy�ǥ\��A���UCtrl+W�����y�ǥ\��C

���ط��z / Project Overview
�o�Ӷ��جO�@�Ӱ�� YOLOv3 ���۰ʴy�ǵ{���]Aimbot�^�A�Q�ι�ɿù��I�ϩM�ؼ��˴��޳N�A�ѧO�ù��������H���ñ���ƹ����ʩM�I���C�{���䴩 1080p (1920x1080) �M 4K (3840x2160) �ѪR�ת���ܾ��A�åi�q�L�ֱ���Ұʩ������y�ǥ\��C

This project is an automatic aiming program (Aimbot) based on YOLOv3. It uses real-time screen capture and object detection to identify "people" on the screen and control mouse movement and clicks. The program supports 1080p (1920x1080) and 4K (3840x2160) resolution displays, with the ability to enable or disable the aimbot via hotkeys.

�\�� / Features
�ؼ��˴��G�ϥ� YOLOv3 �ҫ��˴��ù��������H���C
�۰ʴy�ǡG�N�ƹ����ʨ��˴��쪺�ؼФ��ߨü����I���C
�ֱ��䱱��GCtrl+Q �Ұʴy�ǡACtrl+W �����y�ǡC
�ѪR�פ䴩�G�A�t 1080p �M 4K ��ܾ��A�ä䴩��L�D�зǸѪR�סC
�ɶ���x�G��ܷƹ����ʩM�I��������ɶ��C
Object Detection: Uses the YOLOv3 model to detect "people" on the screen.
Auto-Aiming: Moves the mouse to the center of detected targets and simulates a click.
Hotkey Control: Ctrl+Q to enable aiming, Ctrl+W to disable aiming.
Resolution Support: Compatible with 1080p and 4K displays, with fallback for non-standard resolutions.
Time Logging: Displays execution time for mouse movement and clicks.
�ϥλ��� / Usage Instructions
�Ұʵ{���G
�B�� python aimbot.py�C
�{���|�۰��˴��ù��ѪR�ר���ܷ�e�Ҧ��]1080p�B4K ���q�{�^�C
����y�ǡG
�� Ctrl+Q �Ұʴy�ǥ\��C
�� Ctrl+W �����y�ǥ\��C
�[���X�G
����x�|��ܷƹ����ʩM�I�����ɶ��]�Ҧp�G���ʮɶ�: 0.012s, �I���ɶ�: 0.001s�^�C
Start the Program:
Run python aimbot.py.
The program will detect your screen resolution and display the current mode (1080p, 4K, or default).
Control Aiming:
Press Ctrl+Q to enable the aimbot.
Press Ctrl+W to disable the aimbot.
Monitor Output:
The console will display the time taken for mouse movement and clicks (e.g., Move time: 0.012s, Click time: 0.001s).
�w�˨B�J / Installation Steps
���һݨD / Requirements
Python 3.6+
PyTorch�]�䴩 CUDA �i��^
OpenCV (opencv-python)
PyAutoGUI (pyautogui)
Pillow (pillow)
Keyboard (keyboard)
NumPy (numpy)
�w�˨̿� / Install Dependencies
bash

���_

����

�ƻs
pip install torch torchvision opencv-python pyautogui pillow keyboard numpy
�U�� YOLOv3 �v�� / Download YOLOv3 Weights
�q�H�U�s���U�� yolov3.weights�G
�x��U���s��
�N����m�b���خڥؿ��A�έק�{������ weightsfile �Ѽƫ��V���T���|�C
�ǳưt�m��� / Prepare Configuration File
�T�O cfg/yolov3.cfg ���s�b�󶵥إؿ����C�Y�L�A�i�q YOLO �x����� �U���C
�B��{�� / Run the Program
bash

���_

����

�ƻs
python aimbot.py
�`�N�ƶ� / Notes
�w��ݨD�G
4K �ѪR�׻ݭn�������p���O�A��ĳ�ϥ� GPU�]CUDA �䴩�^�C
�T�O��ܾ��ѪR�ץ��T�˴��A�קK�I�Ͻd��W�X�ù��C
�ƹ��Y��Y�ơG
1080p �ϥ� 1.56�A4K �ϥ� 3.12�C�Y�y�Ǥ��ǽT�A�i�ھڹ�ڻݨD�վ� mouse_scale_factor�C
�̿���G
�{�����] util.py �M darknet.py �w��{�å]�t���n����ơ]prep_image �M write_results�^�C�Y�ʤֳo�Ǥ��A�ݦۦ��{�αq YOLOv3 �x���{������C
�k�߻P�D�w�G
���{���ȥΩ�ǲߩM��s�ت��C�ФŦb�C���Ψ�L���g���v�����Ҥ��ϥΡA�H�K�H�Ϭ����W�w�C
Hardware Requirements:
4K resolution requires higher computational power; a GPU with CUDA support is recommended.
Ensure the screen resolution is detected correctly to avoid capturing beyond the screen boundaries.
Mouse Scaling Factor:
1080p uses 1.56, 4K uses 3.12. Adjust mouse_scale_factor if aiming is inaccurate.
Dependent Files:
The program assumes util.py and darknet.py are implemented with required functions (prep_image and write_results). If missing, implement them or obtain from the official YOLOv3 repository.
Legal and Ethical Considerations:
This program is for educational and research purposes only. Do not use it in games or unauthorized environments to avoid violating regulations.
�{�����c / Project Structure
text

���_

����

�ƻs
aimbot/
�u�w�w aimbot.py         # �D�{��
�u�w�w cfg/
�x   �|�w�w yolov3.cfg   # YOLOv3 �t�m���
�u�w�w yolov3.weights   # YOLOv3 �v�����
�u�w�w util.py          # �u���ơ]�ݦۦ��{�^
�u�w�w darknet.py       # Darknet �ҫ���{�]�ݦۦ��{�^
�|�w�w README.md        # ���������
�pô�覡 / Contact : xandy168@gmail.com 
�p�����D�Ϋ�ĳ�A�гq�L GitHub Issues �pô�C

For questions or suggestions, please reach out via GitHub Issues.