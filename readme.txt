# PoE_HAT_B_code_new

## prepare
sudo apt-get install wiringpi
sudo apt-get install python3 python3-pip
sudo apt-get install python3-smbus
sudo pip3 install RPi.GPIO

run python3 main.py
if PermissionError: [Errno 13] Permission denied
sudo chmod a+rw /dev/i2c-*

## install

sudo bash install.sh
