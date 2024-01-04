## 概要
北陽電機製のURG（USB接続タイプ）からシリアル通信でデータ取得するPythonスクリプトです．
最低限の機能だけを提供していますので，プログラムは解析しやすいと思います．
ご活用ください．
（まだ動作確認が完全でないので，お気づきの点はissueを上げていただけると助かります）

## 動作確認機器
- [UBG-04LX-F01](https://www.hokuyo-aut.co.jp/search/single.php?serial=24&utm_source=google&utm_medium=cpc&utm_campaign=[P-MAX]&gad_source=1&gclid=Cj0KCQiAkKqsBhC3ARIsAEEjuJgjW_HZUi4gD8oWFw98hCq3jgN_M4oOZLgG4-RODck_B9eeZfWw2-QaAm4tEALw_wcB)（HOKUYO AUTOMATIC CO.,LTD.）

## 使い方
URGとPCをUSB接続してください．続いて，接続されたデバイスファイル名を確認し，`main.py`の設定を修正してください．
```python
# 通信準備
device_file = '/dev/cu.usbmodem1101'
```
実行は次のコマンドです．
```bash
python ./main.py
```
停止は`Ctrl+c`です．

## 注意
- `main.py`と`utils.py`は同じディレクトリ下に置いてください

## 動作イメージ
![img](https://private-user-images.githubusercontent.com/20371927/292950747-1695e0d4-79a1-4887-9cd4-6770abcc5a29.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDQzNTIwOTYsIm5iZiI6MTcwNDM1MTc5NiwicGF0aCI6Ii8yMDM3MTkyNy8yOTI5NTA3NDctMTY5NWUwZDQtNzlhMS00ODg3LTljZDQtNjc3MGFiY2M1YTI5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAxMDQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMTA0VDA3MDMxNlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTk5Yzg4Njc1NzlmZTFhNjg1M2ViY2Y5NDJjNzI0MzY3OThlYTJkMjE5YjdiMjEyY2E1NDExNGVlYzMyMTI0NzQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.yQfmUhLc16QBLqb2bOuReD5jeE0eoHEPHk8-6ckPb1c)
