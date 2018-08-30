import os
import time
#test4
#removes old repository
os.system("rm -r -f Data-Logging")

#gets new repository

os.system("git clone https://github.com/Anaphite/Data-Logging.git")

os.system("mv /home/pi/Temperature/Data-Logging/update.py /home/pi/Temperature/update.py")
 
