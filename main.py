import serial
import time
import math
import sys
import matplotlib.pyplot as plt
from utils import *
from urg_class import Urg
from common import *

XMIN = -3000 #[mm]
XMAX =  3000 #[mm]
YMIN = -3000 #[mm]
YMAX =  3000 #[mm]

# ウィンドウサイズを固定する．お好みで調整
plt.figure(figsize=(8, 8))

try:
    urg = Urg('/dev/cu.usbmodem1101', 115200)
    
    count = 0
    while True:
        success, urg_data = urg.one_shot()
        if success == True:
            x = []
            y = []
            for d in urg_data:
                angle = deg2rad(index2angle(d[0]))
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
    urg.close()
    
except KeyboardInterrupt:
    # Ctrl-Cの後処理
    print("Pressed Ctrl-C")
    # シリアル接続を閉じる
    urg.close()
    print("Bye")

