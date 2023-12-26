import serial
import time
import math
import sys
import matplotlib.pyplot as plt
from utils import *

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
        #print(response, file=sys.stderr)
    else:
        print("False", file=sys.stderr)
    
    time.sleep(1)
    
    # PPコマンドを送信し通信テスト
    success, response = cmd_PP(ser)
    if success == True:
        print("[OK] PP")
        #print(response, file=sys.stderr)
    else:
        print("False", file=sys.stderr)
    
    time.sleep(1)
    
    # IIコマンドを送信し通信テスト
    success, response = cmd_II(ser)
    if success == True:
        print("[OK] II")
        #print(response, file=sys.stderr)
    else:
        print("False", file=sys.stderr)

    print("Connect test all clear.")
    
    for i in range(100):
        # MDコマンドを送信しone-shot計測
        success, head, data = cmd_MD(ser)
        if success == True:
            urg_data = one_shot(data)
            x = []
            y = []
            for d in urg_data:
                angle = index2angle(d[0])
                x.append(d[1] * math.cos(angle * math.pi/180))
                y.append(d[1] * math.sin(angle * math.pi/180))
            plt.clf()
            plt.xlim(-6000, 6000)
            plt.ylim(-6000, 6000)
            plt.scatter(x, y, s=1)
            plt.grid()
            plt.draw()  # プロットを更新
            plt.pause(0.001)  # 短時間待機
            print(i, "data recieved")
        else:
            print("False", file=sys.stderr)
    # シリアル接続を閉じる
    ser.close()
    
except KeyboardInterrupt:
    # シリアル接続を閉じる
    ser.close()

