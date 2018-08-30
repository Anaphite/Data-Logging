import os
import time
#test
#removes old repository
os.system("rm -r -f Data-Logging")

#gets new repository

os.system("git clone https://github.com/Anaphite/Data-Logging.git")

os.system("mv update.py ../update.py")
 
