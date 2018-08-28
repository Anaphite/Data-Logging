#script to install latest version from API repository from GitHub


import os
import time

#deletes old programs

os.system("rm TGpub.py")
os.system("rm VOCGpub.py")
os.system("rm updateAPI.py")

#clones repository
os.system("git clone https://github.com/Anaphite/Data-Logging.git")
time.sleep(10)
#moves files out of API file to where update.py stored
os.system("mv /home/pi/Temperature/Data-Logging/TGpub.py /home/pi/Temperature/TGpub.py")
os.system("mv /home/pi/Temperature/Data-Logging/VOCGpub.py /home/pi/Temperature/VOCGpub.py")
os.system("mv /home/pi/Temperature/Data-Logging/updateAPI.py /home/pi/Temperature/updateAPI.py")


#removes the API directory now relavent contents have been removed
os.system("rm -r -f /home/pi/Temperature/Data-Logging")
