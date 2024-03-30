# PoE_HAT_B_code_new

## prepare

```bash
sudo apt-get install wiringpi
sudo apt-get install python3 python3-pip
sudo apt-get install python3-smbus
sudo pip3 install RPi.GPIO
```

try run `python3 main.py`

if PermissionError: [Errno 13] Permission denied

`sudo chmod a+rw /dev/i2c-*`

## install

```bash
sudo bash install.sh

# check running status
systemctl status poe-hat
```

## others command

1. `led_hostname.py` to show the hostname on the LED
2. `led_clear.py` to remove all from the LED
3. `fan_on.py` to turn on the fan
4. `fan_off.py` to turn off the fan

remark: use `python3 xxx.py` to run the command.
