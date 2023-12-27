import serial
import time
import math
import sys
import matplotlib.pyplot as plt
from utils import *

DEBUG_MODE = False
XMIN = -3000 #[mm]
XMAX =  3000 #[mm]
YMIN = -3000 #[mm]
YMAX =  3000 #[mm]

# ウィンドウサイズを固定する．お好みで調整
plt.figure(figsize=(8, 8))

try:
    # 通信準備
    device_file = '/dev/cu.usbmodem1101'
    try:
        ser = serial.Serial(device_file, 115200, timeout=1)
    except serial.SerialException as e:
        print(f"Connection error {e}", file=sys.stderr)
        print("Bye")
        sys.exit(0)
    
    time.sleep(2)
    
    # VVコマンドを送信し通信テスト
    success, response = cmd_VV(ser)
    if success == True:
        print("[OK] VV")
        if DEBUG_MODE:
            print(response, file=sys.stderr)
    else:
        print("[False] VV", file=sys.stderr)
    
    time.sleep(1)
    
    # PPコマンドを送信し通信テスト
    success, response = cmd_PP(ser)
    if success == True:
        print("[OK] PP")
        if DEBUG_MODE:
            print(response, file=sys.stderr)
    else:
        print("[False] PP", file=sys.stderr)
    
    time.sleep(1)
    
    # IIコマンドを送信し通信テスト
    success, response = cmd_II(ser)
    if success == True:
        print("[OK] II")
        if DEBUG_MODE:
            print(response, file=sys.stderr)
    else:
        print("[False] II", file=sys.stderr)

    print("Connect test all clear.")
    
    count = 0
    while True:
        # MDコマンドを送信しone-shot計測
        success, head, data = cmd_MD(ser)
        if success == True:
            urg_data = one_shot(data)
            x = []
            y = []
            for d in urg_data:
                angle = index2angle(d[0]) * math.pi/180
                x.append(d[1] * math.cos(angle))
                y.append(d[1] * math.sin(angle))
            plt.clf()
            plt.xlim(XMIN, XMAX)
            plt.ylim(YMIN, YMAX)
            plt.scatter(x, y, s=1)
            plt.grid()
            plt.draw()  # プロットを更新
            plt.pause(0.001)  # 短時間待機
            print(count, "data recieved")
            count += 1
        else:
            print("False", file=sys.stderr)
    # シリアル接続を閉じる
    ser.close()
    
except KeyboardInterrupt:
    # Ctrl-Cの後処理
    print("Pressed Ctrl-C")
    # シリアル接続を閉じる
    ser.close()
    print("Bye")

