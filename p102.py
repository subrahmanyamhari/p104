import os
import shutil
os.mkdir("D:/dowloaded")
print(os.getcwd())
source = "C:/Users/subra/Downloads"
destintion = 'D:/dowloaded'

for i in os.listdir(source):
    print("moving..." + source)
    v, r = os.path.splitext(i)
    file1 = source+"/" + i
    file2 = destintion + "/" + i
    shutil.move(file1,file2)