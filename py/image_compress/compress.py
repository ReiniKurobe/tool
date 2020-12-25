import sys
import os
import glob
import cv2

# ----------------------------------------
# 引数を受け取る
# ----------------------------------------

args = sys.argv
input_folder = ''
output_folder = ''

i = 1

for arg in args :
  if i == 2 :
    input_folder = arg
  elif i == 3 :
    output_folder = arg
  i += 1


# 引数が足りてなければ処理を中断する
if input_folder == '' :
  print('Input folder is not entered')
  sys.exit(1)
elif output_folder == '' :
  print('Output folder is not entered')
  sys.exit(1)

# ----------------------------------------
# 引数で入力されたフォルダをよみこむ
# ----------------------------------------

if input_folder[-1] == '/' :
  input_files = glob.glob(input_folder + '*')
else :
  input_files = glob.glob(input_folder + '/*')

for input_file in input_files :
  path, ext = os.path.splitext(input_file)
  if ext == '.jpeg' or ext == '.png' or ext == '.jpg' :
    img = cv2.imread(input_file)
    result, encimg = cv2.imencode(ext, img, [cv2.IMWRITE_JPEG_QUALITY, 30])
  
    if result:
        directory = input_file.split('/')
        file_name = directory.pop()
        decimg = cv2.imdecode(encimg, cv2.IMREAD_COLOR)
        cv2.imwrite(output_folder + file_name, decimg)
        print(output_folder + file_name + 'to compress')