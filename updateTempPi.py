import os
import time
#test7

os.system("rm updateTempPi.py")
#removes old repository
os.system("rm -r -f Data-Logging")

#gets new repository

os.system("git clone https://github.com/Anaphite/Data-Logging.git")

os.system("mv /home/pi/Temperature/Data-Logging/updateTempPi.py /home/pi/Temperature/updateTempPi.py")
 
