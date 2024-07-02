from math import pi

DEBUG_MODE = False

def index2angle(index):
    return (index + 0) * 360/1440.0 - 135.0
    # 以下の数値はUBG-04LX-F01の設定値
    #return (index + 44) * 360/1024 - 135.0

def angle2index(angle):
    return int((angle - (-135.0)*1440.0/360))

def deg2rad(deg):
    return deg * pi/180.0
