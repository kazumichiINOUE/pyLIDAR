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

urg = Urg('/dev/cu.usbmodem1101', 115200)
try:
    count = 0
    dth = 100
    while True:
        clustering = []
        prev_r = 0
        num_cluster = -1 
        success, urg_data = urg.one_shot()
        count += 1
        if count % 10 != 0:
            continue

        if success == True:
            for d in urg_data:
                if abs(prev_r - d[1]) > dth:
                    num_cluster += 1
                prev_r = d[1]
                clustering.append((num_cluster, d[0], d[1]))
        else:
            print("False", file=sys.stderr)

        all_list = []
        for num in range(num_cluster):
            x = []
            y = []
            for c in clustering:
                if c[0] == num:
                    angle = deg2rad(index2angle(c[1]))
                    x.append(c[2] * math.cos(angle))
                    y.append(c[2] * math.sin(angle))
            all_list.append((x, y))
        plt.clf()
        plt.xlim(XMIN, XMAX)
        plt.ylim(YMIN, YMAX)
        for pt in all_list:
            plt.scatter(pt[0], pt[1], s=2)
        plt.grid()
        plt.draw()  # プロットを更新
        plt.pause(0.001)  # 短時間待機
    
except KeyboardInterrupt:
    # Ctrl-Cの後処理
    print("Pressed Ctrl-C")
    # シリアル接続を閉じる
    urg.close()
    print("Bye")

