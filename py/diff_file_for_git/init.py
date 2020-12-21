import os
import sys
import shutil
import git

# ----------------------------------------
# リポジトリ情報
# ----------------------------------------

repo =  git.Repo('./')
t = repo.head.commit.tree
diff = repo.git.diff('HEAD~1..HEAD', name_only=True) 
diff_list = diff.split('\n')
print(diff_list)

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