from math import pi

DEBUG_MODE = False

def index2angle(index):
    # 以下の数値はUBG-04LX-F01の設定値
    return (index + 44) * 360/1024 - 135.0

def deg2rad(deg):
    return deg * pi/180.0
