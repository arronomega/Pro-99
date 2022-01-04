import os
import shutil
import time
path = input("Give the name of the folder to be sorted:  ")
days = 77760000
listfiles= os.listdir(path)
Time = time.time()

for i in listfiles :
    name,ext = os.path.splitext(i)
    ct_Time = os.stat(path).st_ctime
    ext= ext[1:]
    if ext == '':
        continue
    if os.path.exists(path):
        os.walk(path)
        os.path.join(path)
        ctime=os.stat(path).st_ctime
    if (Time-ctime) >= days:
        if os.path.isfile(path):
            os.remove(path)
        else :
            shutil.rmtree()
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+i,path+'/'+ext+'/'+i)
    else :
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+i,path+'/'+ext+'/'+i)