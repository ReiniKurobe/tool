# 納品ファイル作成ツール（差分テキストありver）

## 事前準備

1. [Python 3系をインストール](https://www.python.org/downloads/)
2. diff_sample.txtをコピーし、ファイル名をdiff.txtにする

## 使用方法

1. ファイルの変更差分をdiff.txtに記載する（相対パス）
2. init.pyがあるディレクトリにて`$ python init.py {/path/to/} {/output_folder/path/}`を実行
  - 第一引数にdiff.txtがある場所を指定。第二引数に出力したいフォルダを指定。
3. 指定したアプトプットフォルダに差分ファイルが作成される