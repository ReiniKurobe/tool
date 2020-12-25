import os
import sys
import shutil

# ----------------------------------------
# 引数を受け取る
# ----------------------------------------

args = sys.argv
diff_file_path = './diff.txt'
file_path = ''
output_path = ''

i = 1

for arg in args :
  if i == 2 :
    file_path = arg
  elif i == 3 :
    output_path = arg
  i += 1


# 引数が足りてなければ処理を中断する
if file_path == '' :
  print('File path folder is not entered')
  sys.exit(1)
elif output_path == '' :
  print('Output path is not entered')
  sys.exit(1)


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

if os.path.exists(output_path) :
  shutil.rmtree(output_path)

os.mkdir(output_path)

# ----------------------------------------
# ファイルコピペの準備 ディレクトリの記述を揃える
# ----------------------------------------

if output_path[-1] != '/' :
  output_path = output_path + '/'

if file_path[-1] != '/' :
  file_path = file_path + '/'

# ----------------------------------------
# ファイルを探してコピーする
# ----------------------------------------

for target in diff_list :
  directory = target.split('/')
  file_name = directory.pop()
  directory = output_path + '/'.join(directory)

  if os.path.exists(directory) :
    if os.path.isfile(file_path + target) :
      shutil.copyfile(file_path + target, directory + '/' + file_name)
  else :
    if os.path.isfile(file_path + target) :
      os.makedirs(directory)
      shutil.copyfile(file_path + target, directory + '/' + file_name)