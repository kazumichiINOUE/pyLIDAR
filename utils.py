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
    for _ in range(8):
        response = ser_dev.read_until().decode('utf-8')
        ret.append(remove_semicolon_followed_by_char(response))
    if len(ret) > 0:
        return True, ret

    return False, ret

def cmd_PP(ser_dev):
    # PPコマンドを送信（デバイスパラメータ情報を要求）
    ser_dev.write(b'PP\n')
    # 応答を読み取る
    ret = []
    for _ in range(11):
        response = ser_dev.read_until().decode('utf-8')
        ret.append(remove_semicolon_followed_by_char(response))
    if len(ret) > 0:
        return True, ret
    return False, ret

def cmd_II(ser_dev):
    # IIコマンドを送信（ステータス情報を要求）
    ser_dev.write(b'II\n')
    # 応答を読み取る
    ret = []
    for _ in range(10):
        response = ser_dev.read_until().decode('utf-8')
        ret.append(remove_semicolon_followed_by_char(response))
    if len(ret) > 0:
        return True, ret
    return False, ret

def cmd_MD(ser_dev):
    # MDコマンドを送信（距離データの取得）
    ser_dev.write(b'MD0044072501101\n')
    # 応答を読み取る
    head = []
    data = []
    for _ in range(6):
        response = ser_dev.read_until().decode('utf-8')
        head.append(remove_semicolon_followed_by_char(response))
    for _ in range(33):
        response = ser_dev.read_until().decode('utf-8')
        response = response.rstrip('\n')
        data.append(response)
    if len(head) > 0:
        return True, head, data
    return False, head, []
