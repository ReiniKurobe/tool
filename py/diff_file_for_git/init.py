import os
import sys
import shutil
import git

# ----------------------------------------
# 引数を受け取る
# ----------------------------------------

args = sys.argv
git_path = ''
output_path = ''

i = 1

for arg in args :
  if i == 2 :
    git_path = arg
  elif i == 3 :
    output_path = arg
  i += 1


# 引数が足りてなければ処理を中断する
if input_folder == '' :
  print('Git folder is not entered')
  sys.exit(1)
elif output_folder == '' :
  print('Output folder is not entered')
  sys.exit(1)

# ----------------------------------------
# リポジトリ情報
# ----------------------------------------

repo =  git.Repo(git_path)
t = repo.head.commit.tree
diff = repo.git.diff('HEAD~1..HEAD', name_only=True) 
diff_list = diff.split('\n')
print(diff_list)

# ----------------------------------------
# 既存ディレクトリの削除
# ----------------------------------------

if os.path.exists(output_path) :
  shutil.rmtree(output_path)

# ----------------------------------------
# ファイルを探してコピーする
# ----------------------------------------

for target in diff_list :
  directory = target.split('/')
  file_name = directory.pop()
  directory = output_path + '/'.join(directory)

  if os.path.exists(directory) :
    if os.path.isfile(target) :
      shutil.copyfile(target, directory + '/' + file_name)
  else :
    if os.path.isfile(target) :
      os.makedirs(directory)
      shutil.copyfile(target, directory + '/' + file_name)