"""
Urg class
"""
import sys
import time
import serial
from utils import cmd_VV, cmd_PP, cmd_MD, cmd_II
from common import DEBUG_MODE

class Urg:
    """
    Urgクラスの定義
    """
    def __init__(self, device_file, baurate):
        self.device_file = device_file
        self.baurate = baurate
        self.timeout = 1
        try:
            self.ser = serial.Serial(self.device_file, self.baurate, timeout=self.timeout)
        except serial.SerialException as e:
            print(f"Connection error {e}", file=sys.stderr)
            print("Bye")
            sys.exit(0)
        time.sleep(2)

        # VVコマンドを送信し通信テスト
        success, response = cmd_VV(self.ser)
        if success is True:
            print("[OK] VV")
            if DEBUG_MODE:
                print(response, file=sys.stderr)
        else:
            print("[False] VV", file=sys.stderr)
            sys.exit(0)

        time.sleep(1)

        # PPコマンドを送信し通信テスト
        success, response = cmd_PP(self.ser)
        if success is True:
            print("[OK] PP")
            if DEBUG_MODE:
                print(response, file=sys.stderr)
        else:
            print("[False] PP", file=sys.stderr)
            sys.exit(0)

        time.sleep(1)

        # IIコマンドを送信し通信テスト
        success, response = cmd_II(self.ser)
        if success is True:
            print("[OK] II")
            if DEBUG_MODE:
                print(response, file=sys.stderr)
        else:
            print("[False] II", file=sys.stderr)
            sys.exit(0)

        # 通信テストを合格
        print("Connect test all clear.")

    def one_shot(self):
        """
        1回だけ計測する
        """
        # MDコマンドを送信しone-shot計測
        success, _, data = cmd_MD(self.ser)
        urg_data = []
        if success is True:
            data_strings = ""
            for p in data:
                if len(p) > 0:
                    # check_sum = p[-1]
                    body = p[:-1]
                    data_strings += body
            for i in range(0, len(data_strings), 3):
                three_chars = data_strings[i:i+3]
                binary = []
                for char in three_chars:
                    ch = ord(char) - 0x30
                    hex_ascii_value = hex(ch)
                    bin_val = bin(int(hex_ascii_value, 16))
                    # 2進数を6ビットの2進数に変換
                    binary.append(format(int(bin_val, 2), '06b'))
                combined_binary_24bit = ''.join(binary)
                if all(c in '01' for c in combined_binary_24bit):
                    r = int(combined_binary_24bit, 2)
                    index = int(i/3)
                    urg_data.append((index, r))
                else:
                    print("不正なデータが含まれています")
                    self.close()
                    sys.exit(0)
            return True, urg_data
        return False, urg_data

    def close(self):
        """
        close serial port
        """
        self.ser.close()
