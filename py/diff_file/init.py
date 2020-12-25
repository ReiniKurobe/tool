import os
import sys
import shutil

# ----------------------------------------
# 引数を受け取る
# ----------------------------------------

args = sys.argv
diff_file_path = ''
output_path = ''

i = 1

for arg in args :
  if i == 2 :
    diff_file_path = arg
  elif i == 3 :
    output_path = arg
  i += 1


# 引数が足りてなければ処理を中断する
if input_folder == '' :
  print('Diff file is not entered')
  sys.exit(1)
elif output_folder == '' :
  print('Output folder is not entered')
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

if os.path.exists(output_folder) :
  shutil.rmtree(output_folder)

# ----------------------------------------
# ファイルを探してコピーする
# ----------------------------------------

for target in diff_list :
  directory = target.split('/')
  file_name = directory.pop()
  directory = output_folder + '/'.join(directory)

  if os.path.exists(directory) :
    if os.path.isfile(target) :
      shutil.copyfile(target, directory + '/' + file_name)
  else :
    if os.path.isfile(target) :
      os.makedirs(directory)
      shutil.copyfile(target, directory + '/' + file_name)