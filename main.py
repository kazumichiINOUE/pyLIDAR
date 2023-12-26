import serial
import time

def remove_semicolon_followed_by_char(line):
    # 改行を除去する
    line = line.rstrip('\n')
    # 「;」の位置を見つける
    semicolon_index = line.find(';')
    if semicolon_index != -1:
        # 「;」の前の部分のみを抽出
        return line[:semicolon_index]
    return line

def cmd_VV(ser_dev):
    # VVコマンドを送信（デバイス情報を要求）
    ser_dev.write(b'VV\n')
    # 応答を読み取る
    ret = []
    for i in range(7):
        response = ser_dev.read_until().decode('utf-8')
        ret.append(remove_semicolon_followed_by_char(response))
    if len(ret) > 0:
        return True, ret
    else:
        return False, ret

# ここでデバイスファイル名をダミーで設定します（実際には適切なデバイスファイル名を使用してください）
device_file = '/dev/cu.usbmodem1101'

# シリアル接続の設定
ser = serial.Serial(device_file, 115200, timeout=1)

# センサーの初期化に少し時間がかかる場合があるので、少し待つ
time.sleep(2)

# VVコマンドを送信し通信テスト
success, response = cmd_VV(ser)
if success == True:
    print(response)
else:
    print("False")

# シリアル接続を閉じる
ser.close()

