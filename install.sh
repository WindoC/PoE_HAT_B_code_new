#!/bin/bash

install_path=$(dirname $0)

# mkdir -p $install_path
# cp -r * $install_path/
# rm $install_path/install.sh
find $install_path -type f -name "*.pyc" -delete
find $install_path -type d -name __pycache__ -delete

sudo cp $install_path/systemd.txt /etc/systemd/system/poe-hat.service
sed -i "/ExecStart/c\ExecStart=python3 $install_path/main.py" /etc/systemd/system/poe-hat.service
sudo chown root:root /etc/systemd/system/poe-hat.service
sudo chmod 644 /etc/systemd/system/poe-hat.service

sudo systemctl daemon-reload
sudo systemctl enable poe-hat
sudo systemctl start poe-hat

echo execute the below command to start the script manually
echo "nohup python3 $install_path/main.py >/dev/null 2>&1 &"
