# Data Logging
Data logging utilising the google sheets API with an interactive menu allowing for variation in tming length and frequency. The entire code is run off a raspberry pi from its logging directory and updated from this git repository.

## Getting Started

### Prerequisites
- Working google service account
- Raspberry Pi set up with Python 3, git and the appropriate control packages for the data logger
- Open google sheet with the correct name dependant on the data being logged

## Running the code
- Log on to the pi using an SSH client. IP addresses are provided in the drive
### On Windows
- Install PuTTY 
- Follow instructions through the GUI to log on, username is Pi
### On Mac
In terminal:
```
ssh pi@ipadress
```

passwords are provided in the drive

## Temperature Logger - logging data
```
cd Temperature/Data-Logging

python3 TGpub.py

```

## VOC logger - logging data
```
cd Vlog

python VOCGpub.py

```

Follow the python menu provided, all data will be written to the corresponding google sheets document as well as a data file on the pi. 

## Updating Code
Will update the code from this github repository, if anything is changed here it will be changed on the pi.
2 Programs updateTempPi.py for updating the Temperature Raspberry pi, updateVOCPi.py for the VOC Pi Zero.Runt he relevant one for the Pi you are dealing with.

```
python3 updateTempPi.py
python3 updateVOCPi.py
```

## Built With
* [Adafruit_CCS811_python](https://github.com/adafruit/Adafruit_CCS811_python) - VOC meter Python Package (depreciated - in need of updating)
* [w1thermsensor](https://github.com/timofurrer/w1thermsensor) - Temperature meter Python Package

## Authors
* **Christopher Brown** - *28/08/2018* - [ChriisBrown](https://github.com/chriisbrown)
