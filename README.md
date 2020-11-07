# download-interrupt-handler



Creates regular back-ups of the CRDOWNLOAD file, so that the download might resume from where it left off after an interruption.



Download interruptions can be really frustating, and might cause the entire download to start from scratch. The situation worsens if you have intermittent internet connectivity, or a metered internet connection.



This simple program essentially creates a backup of the CRDOWNLOAD file periodically (automatically). Even when the download fails, the backup file can be used to resume the download from where it left off. This is _intended_ to be used while downloading large files, where you don't really want the download progress to reset (for smaller files, <50MB -  you can simply download them again).   



==============================================================================

__Steps__ _(Its simple, really - the hardest part will be to read the steps):_

==============================================================================


•Start your download
•Modify the mains.py file by following the comments therein, and run it on your computer



•**If the download is interrupted** 
  •Stop the program (exit)
  •Start the download again, then pause it
  •In the downloads folder, note the name of the new CROWNLOAD file 
  •Rename the previous backup file to this new name
  •In the downloads folder, replace the new CRDOWNLOAD file with the backup file
  •Resume the download again. It will progress from the point it was interrupted



•If the download is not interrupted
  •Congratulations
  

_Good day!_
