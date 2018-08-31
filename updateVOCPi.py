import os
import time
#test6

os.system("rm updateVOCPi.py")
#removes old repository
os.system("rm -r -f Data-Logging")

#gets new repository

os.system("git clone https://github.com/Anaphite/Data-Logging.git")
#paths need changeing to the approriate ones for the pi zero
os.system("mv /home/pi/Vlog/Data-Logging/updateVOCPi.py /home/pi/Vlog/updateVOCPi.py")
