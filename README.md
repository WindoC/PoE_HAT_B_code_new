# PoE_HAT_B_code_new

# install by docker (new)

```bash
docker run -d \
 --name poe_hat \
 --hostname $(hostname) \
 --device /dev/i2c-1 \
 -v /sys/class/thermal/thermal_zone0/temp:/sys/class/thermal/thermal_zone0/temp \
 --restart=on-failure \
 ghcr.io/windoc/poe_hat_b_code_new
```

remark:
- `--device /dev/i2c-1` that `/dev/i2c-1` change to the i2c device name in your system.
- `-v /sys/class/thermal/thermal_zone0/temp:/sys/class/thermal/thermal_zone0/temp` use to get the temperature of the raspberry pi.

## variables

- `POE_HAT_TEMPERATURE` - middle temperature point to control the fan on and off.
- `POE_HAT_DELTA` - buffer temperature to avoid the fan going on and off too frequently.
  - if `temperature > POE_HAT_TEMPERATURE + POE_HAT_DELTA` switch on the fan
  - if `temperature < POE_HAT_TEMPERATURE - POE_HAT_DELTA` switch off the fan

```bash
docker run -d \
 --name poe_hat \
 --hostname $(hostname) \
 -e POE_HAT_TEMPERATURE=50.0 -e POE_HAT_DELTA=10.0 \
 --device /dev/i2c-1 \
 -v /sys/class/thermal/thermal_zone0/temp:/sys/class/thermal/thermal_zone0/temp \
 --restart=on-failure \
 ghcr.io/windoc/poe_hat_b_code_new
```

remark:
- new add line `-e POE_HAT_TEMPERATURE=50.0 -e POE_HAT_DELTA=10.0` pass the special values into the container.

## debug

```bash
# build
docker build -t poe_hat_b -f docker/Dockerfile .

# try command
docker run -it --rm --device /dev/i2c-1 -v /sys/class/thermal/thermal_zone0/temp:/sys/class/thermal/thermal_zone0/temp poe_hat_b python3 main.py
docker run -it --rm --device /dev/i2c-1 poe_hat_b python3 fan_off.py
docker run -it --rm --device /dev/i2c-1 poe_hat_b python3 fan_on.py
docker run -it --rm --device /dev/i2c-1 poe_hat_b python3 led_clear.py
docker run -it --rm --device /dev/i2c-1 poe_hat_b python3 led_hostname.py
```

# install by systemd

## prepare

```bash
sudo apt-get install wiringpi
sudo apt-get install python3 python3-pip
sudo apt-get install python3-smbus
sudo pip3 install RPi.GPIO
pip3 install Pillow
```

try run `python3 main.py`

if PermissionError: [Errno 13] Permission denied

`sudo chmod a+rw /dev/i2c-*`

## install (need systemd)

```bash
# expect you are in /home/pi now
git clone https://github.com/WindoC/PoE_HAT_B_code_new
cd PoE_HAT_B_code_new

# command will set new service in systemd (copy /etc/systemd/system/poe-hat.service)
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
