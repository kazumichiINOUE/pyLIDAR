def remove_semicolon_followed_by_char(line):
    # 改行を除去する
    line = line.rstrip('\n')
    # 「;」の位置を見つける
    semicolon_index = line.find(';')
    if semicolon_index != -1:
        # 「;」の前の部分のみを抽出
        return line[:semicolon_index]
    return line

def index2angle(index):
    # 以下の数値はUBG-04LX-F01の設定値
    return (index + 44) * 360/1024 - 135.0

def cmd_VV(ser_dev):
    # VVコマンドを送信（デバイス情報を要求）
    ser_dev.write(b'VV\n')
    # 応答を読み取る
    ret = []
    for i in range(8):
        response = ser_dev.read_until().decode('utf-8')
        ret.append(remove_semicolon_followed_by_char(response))
    if len(ret) > 0:
        return True, ret
    else:
        return False, ret

def cmd_PP(ser_dev):
    # PPコマンドを送信（デバイスパラメータ情報を要求）
    ser_dev.write(b'PP\n')
    # 応答を読み取る
    ret = []
    for i in range(11):
        response = ser_dev.read_until().decode('utf-8')
        ret.append(remove_semicolon_followed_by_char(response))
    if len(ret) > 0:
        return True, ret
    else:
        return False, ret

def cmd_II(ser_dev):
    # IIコマンドを送信（ステータス情報を要求）
    ser_dev.write(b'II\n')
    # 応答を読み取る
    ret = []
    for i in range(10):
        response = ser_dev.read_until().decode('utf-8')
        ret.append(remove_semicolon_followed_by_char(response))
    if len(ret) > 0:
        return True, ret
    else:
        return False, ret

def cmd_MD(ser_dev):
    # MDコマンドを送信（距離データの取得）
    ser_dev.write(b'MD0044072501101\n')
    # 応答を読み取る
    head = []
    data = []
    for i in range(6):
        response = ser_dev.read_until().decode('utf-8')
        head.append(remove_semicolon_followed_by_char(response))
    for i in range(33):
        response = ser_dev.read_until().decode('utf-8')
        response = response.rstrip('\n')
        data.append(response)
    if len(head) > 0:
        return True, head, data
    else:
        return False, head

def one_shot(data):
    data_strings = ""
    for p in data:
        if len(p) > 0:
            check_sum = p[-1]
            body = p[:-1]
            data_strings += body
            #ascii_values = [ord(char) for char in body]
            #total_ascii_value = sum(ascii_values)
            #hex_total_ascii_value = hex(total_ascii_value)
            #binary = bin(int(hex_total_ascii_value, 16)) 
            #lower_6_bits = binary[-6:] 
            #ascii_value = int(lower_6_bits, 2) + 0x30
            #character = chr(ascii_value)
            #if check_sum != character:
            #    print("Data Error!\n")
            #else:
            #    data_strings += body
    #print(data_strings)
    urg_data = []
    for i in range(0, len(data_strings), 3):
        three_chars = data_strings[i:i+3]
        binary = []
        for char in three_chars:
            ch = ord(char) - 0x30
            hex_ascii_value = hex(ch)
            bin_val = bin(int(hex_ascii_value, 16)) 
            # 2進数 '0b0' を6ビットの2進数に変換
            binary.append(format(int(bin_val, 2), '06b'))
        combined_binary_24bit = ''.join(binary)
        r = int(combined_binary_24bit, 2)
        index = int(i/3)
        urg_data.append((index, r))
    return urg_data
