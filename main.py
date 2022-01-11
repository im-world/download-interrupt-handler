# Only edit the commented lines


import shutil
import time
import glob, os


time = 60           #expected download time in minutes
backupTime = 2      #backup after every ? minutes
downloadsPath = ''
backupPath = ''
filename = ''

iterations = (time)/(backupTime) + 1 

os.chdir(downloadsPath)
for file in glob.glob("*.crdownload"):
    filename = file

original = str(downloadsPath + filename)            #path of original crdownload file
backup = str(backupPath + filename)                 #path of backup file


for i in range(iterations): 
    shutil.copyfile(original, backup)
    time.sleep(backupTime*60)
