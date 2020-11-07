# Only edit the commented lines


import shutil
import time


time = #expected download time
backupTime = #backup after every ? seconds


iterations = time/(backupTime) + 1 

for i in range(iterations): 

    original = r'C:\Users\ASUS\Downloads\Unconfirmed 174731.crdownload' #path of original crdownload file
    backup = r'C:\Users\ASUS\Desktop\Academia\Unconfirmed 174731.crdownload' #path of backup file

    shutil.copyfile(original, backup)
    time.sleep(backupTime)
