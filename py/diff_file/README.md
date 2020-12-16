# 納品ファイル作成ツール（差分テキストありver）

## 事前準備

1. [Python 3系をインストール](https://www.python.org/downloads/)
2. diff_sample.txtをコピーし、ファイル名をdiff.txtにする
3. 使用したいサイトにinit.py, diff.txtをコピーする

## 使用方法

1. ファイルの変更差分をdiff.txtに記載する（相対パス）
2. init.pyがあるディレクトリにて`$ python init.py`を実行
3. dist/に差分ファイルが作成される