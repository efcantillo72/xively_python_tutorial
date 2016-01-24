# xively_python_tutorial
This script is a modified version of the Xively load_avg script for the Raspberry Pi.I installed the Xively library via pip install xively-python.
The Xively Raspberry Pi tutorial canvbe found here: https://personal.xively.com/dev/tutorials/pi/

This code also uses a Python class from Timo Furrer called W1ThermSensor. This reads the temperature of the one wire DS18B20 digital temperature sensors. 
https://github.com/timofurrer/w1thermsensor.git

Make sure to enable One Wire support to /boot/config.txt by adding the line dtoverlay=w1-gpio
Adafruit's tutorial is here:
https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/ds18b20

Finally to ensure that the script runs on boot I added it to rc.local to run the script on boot. 
sudo /home/pi/xively_python_ds18.py &


