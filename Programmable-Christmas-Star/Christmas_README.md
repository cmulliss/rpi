# How to run Christmas star etc

## on mac:

* Use app LanScan to find IP addresses of everything on network


## on Rpi

* Enable SSH on RPi which is 192.168.68.124


## on star

* star is at raspberrypiz, 192.168.68.125

* ssh pi@192.168.68.25

* ls /etc/systemd/system

* sudo nano /etc/systemd/system/threedtree.service

or:

* sudo nano /etc/systemd/system/star.service

* ssh pi@192.168.68.126

* cd code

* sudo systemctl start star.service

* sudo systemctl stop star.service

* sudo systemctl start threedtree.service


### also

* sudo poweroff
