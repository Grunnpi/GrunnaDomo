# Dependency

* on raspberry, after some troubleshooting : use `sudo raspi-config` for *Interface*, activate I2C / deactivate 1-Wire
* prepare environment for python3 at least for easier compatiblity
* Follow [Adafruit DHT22](https://github.com/adafruit/Adafruit_Python_DHT) installation guide
* copy capteur_dht22.py scripts into `domoticz/scripts/python` directory
* test it :)
* add to crontab using : `crontab -e`
    * `*/10 * * * * sudo /usr/bin/python3.5 /home/pi/domoticz/scripts/python/capteur_dht22.py >> /home/pi/domoticz/log/capteur_dht22.log 2>&1`

