import os
import sys
import shutil

# ----------------------------------------
# 定義
# ----------------------------------------

diff_file_path = './diff.txt'

# ----------------------------------------
# diffファイルの存在を確認
# ----------------------------------------

if os.path.isfile(diff_file_path) == False :
  print('diff file is not')
  sys.exit(1)

# ----------------------------------------
# diffファイルを読み込み
# ----------------------------------------

# diffファイルを開く
diff_f = open(diff_file_path)
diff_file = diff_f.read()
diff_f.close()

# diffを改行で区切ってファイルごとに独立させる
diff_list = diff_file.split('\n')

# ----------------------------------------
# 既存ディレクトリの削除
# ----------------------------------------

if os.path.exists('./dist/') :
  shutil.rmtree('./dist/')

# ----------------------------------------
# ファイルを探してコピーする
# ----------------------------------------

for target in diff_list :
  directory = target.split('/')
  file_name = directory.pop()
  directory = './dist/' + '/'.join(directory)

  if os.path.exists(directory) :
    if os.path.isfile(target) :
      shutil.copyfile(target, directory + '/' + file_name)
  else :
    if os.path.isfile(target) :
      os.makedirs(directory)
      shutil.copyfile(target, directory + '/' + file_name)