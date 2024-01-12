"""
This script interfaces with the URG series of laser rangefinders to visualize 
the scanned data in real-time.

Attributes:
    XMIN (int): Minimum x-coordinate of the plot in millimeters.
    XMAX (int): Maximum x-coordinate of the plot in millimeters.
    YMIN (int): Minimum y-coordinate of the plot in millimeters.
    YMAX (int): Maximum y-coordinate of the plot in millimeters.

Note:
    This script requires a URG series laser rangefinder connected to the system,
    and the appropriate serial port must be specified when creating 
    an instance of the `Urg` class.

Example:
    To run the script, ensure that the URG device is connected and specify the correct serial port:
        $ python main.py
"""

import math
import sys
import matplotlib.pyplot as plt
from urg_class import Urg
from common import DEBUG_MODE, index2angle, deg2rad

XMIN = -3000 #[mm]
XMAX =  3000 #[mm]
YMIN = -3000 #[mm]
YMAX =  3000 #[mm]

# ウィンドウサイズを固定する．お好みで調整
plt.figure(figsize=(8, 8))

print(f"DEBUG MODE -> {DEBUG_MODE}")

urg = Urg('/dev/cu.usbmodem101', 115200)
try:
    count = 0
    while True:
        success, urg_data = urg.one_shot()
        if success is True:
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

except KeyboardInterrupt:
    # Ctrl-Cの後処理
    print("Pressed Ctrl-C")
    # シリアル接続を閉じる
    urg.close()
    print("Bye")
