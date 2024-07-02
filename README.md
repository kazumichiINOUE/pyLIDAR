## 概要
北陽電機製のURG（USB接続タイプ）からシリアル通信でデータ取得するPythonスクリプトです．
最低限の機能だけを提供していますので，プログラムは解析しやすいと思います．
ご活用ください．
（まだ動作確認が完全でないので，お気づきの点はissueを上げていただけると助かります）

## 動作確認機器
- [UBG-04LX-F01](https://www.hokuyo-aut.co.jp/search/single.php?serial=24&utm_source=google&utm_medium=cpc&utm_campaign=[P-MAX]&gad_source=1&gclid=Cj0KCQiAkKqsBhC3ARIsAEEjuJgjW_HZUi4gD8oWFw98hCq3jgN_M4oOZLgG4-RODck_B9eeZfWw2-QaAm4tEALw_wcB) (HOKUYO AUTOMATIC CO.,LTD.)
- [UTM-30LX](https://www.hokuyo-aut.co.jp/search/single.php?serial=21) (HOKUYO AUTOMATIC CO.,LTD.)

## インストール
```
conda install kazumichiinoue::pylidar
```

## 使い方
サンプルコードが`sample/main.py` にあります．
```
cd sample
```
URGとPCをUSB接続してください．続いて，接続されたデバイスファイル名を確認し，`main.py`の設定を修正してください（データ計測の仕方もmain.pyが参考になります）．
```python
# 通信準備
device_file = '/dev/cu.usbmodem1101'
```
実行は次のコマンドです．
```bash
python ./main.py
```
停止は`Ctrl+c`です．

## 動作イメージ
![img](https://publish-01.obsidian.md/access/807e17aa30690c02fbef82ad59c57775/assets/292950747-1695e0d4-79a1-4887-9cd4-6770abcc5a29.png)
