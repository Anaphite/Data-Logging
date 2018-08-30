import os
import time

#removes old repository
os.system("rm -r -f /home/pi/Temperature/Data-Logging")

#gets new repository

os.system("git clone https://github.com/Anaphite/Data-Logging.git")

os.system("mv update.py")
 
