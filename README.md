# GrunnDomo
All my domotic stuff summarized

## All Raspberry

# LCD screen
[Drivers](https://github.com/goodtft/LCD-show)

### Installation
* Rapsberry warm up
    * See [Raspberry](Raspberry.md)
* Domoticz  
    * Wiki provided by Domoticz [here](https://www.domoticz.com/wiki/Raspberry_Pi)
    * Few personnal setup [here](Domoticz.md)
* Telegram bot
    * Use *BotFather* to create bot _(token / my user id)_
* dtgbot
    * Use my own fork [dtgbot](https://github.com/Grunnpi/dtgbot)
* WiringPi for GPIO control
    * Use [WiringPi guide](WiringPi.md)
* DHT22 temperature/humidity
    * Use [DHT22 guide](DHT22.md)
* MotionEye
    * Use [MotionEye](MotionEye.md)
* Range Detector
    * Use [Range guide](RangeDetector.md)
* deCONZ Zigbee bridge
    * Quick guide [deCONZ](deCONZ.md)
* Rasp AP (hotspot)
    * Install [here](https://raspap.com/)
    * update lighthttpd port to 88 in `sudo nano /etc/lighttpd/lighttpd.conf`
    * install macchanger `sudo apt install macchanger` + configure it to change on each network up/down
    * ifconfig + get mac from eth0 to assign to br0 : `sudo macchanger --mac dc:a6:32:56:3b:49 br0`
* Dashticz install
    * [here](https://dashticz.readthedocs.io/en/master/gettingstarted/automaticinstall.html)
    * /home/pi/dev
* Keep2Todoist
    * [here](https://github.com/flecmart/keep2todoist)
    * `sudo docker run -v /home/pi/dev/keep2todoist/config.yaml:/app/config.yaml --restart always ghcr.io/flecmart/keep2todoist:latest`
    * `sudo docker container logs --follow b777c1fccfe8`
    * app password generated [here](https://myaccount.google.com/apppasswords)
* Ngnix reverse proxy
    * doc [here](https://github.com/DewGew/Domoticz-Google-Assistant/wiki/Nginx-reverse-proxy)
    * config file : `/etc/nginx/sites-enabled/default`
* Backup to GDrive
    * [this tool](https://github.com/bachvtuan/Backup-To-Google-Drive)
    * Installed in /domoticz/scripts and push to personnal Drive
* Default chromium page
   * /home/pi/.config/autostart/chrome_domoticz.desktop
* Node install
   * `curl -sSL https://deb.nodesource.com/setup_14.x | sudo bash -`
   * `sudo apt install -y nodejs`

## GRU
* Main instance

### GPIO

Feature|TYPE|PIN|PIN|TYPE|Feature
-------|----|---|---|----|-------
no|3v|1|2|5v|no
no|2/SDA|3|4|5v|no
no|3/SCL|5|6|GND|no
no|gpio4|7|8|14/TXD|no
no|GND|9|10|15/RXD|no
no|gpio17|11|12|gpio18|no
no|gpio27|13|14|GND|no
no|gpio22|15|16|gpio23|no
no|3v|17|18|gpio24|no
no|10/MOSI|19|20|GND|no
no|9/MISO|21|22|gpio25|no
no|11/SCKL|23|24|gpio8|no
no|GND|25|26|gpio7|no

## BOB
* Electricity counter
* Main instance
* Webcam (sometimes)

### GPIO

Feature|TYPE|PIN|PIN|TYPE|Feature
-------|----|---|---|----|-------
no|3v|1|2|5v|no
no|2/SDA|3|4|5v|no
no|3/SCL|5|6|GND|no
no|gpio4|7|8|14/TXD|no
no|GND|9|10|15/RXD|no
no|gpio17|11|12|gpio18|no
no|gpio27|13|14|GND|no
no|gpio22|15|16|gpio23|no
no|3v|17|18|gpio24|no
no|10/MOSI|19|20|GND|no
no|9/MISO|21|22|gpio25|no
no|11/SCKL|23|24|gpio8|no
no|GND|25|26|gpio7|no

## BIL
### Features
* Water counter
* Temperature/Humidity
* Garage door
* Rain water collector
* Webcam

### GPIO

Feature|TYPE|PIN|PIN|TYPE|Feature
-------|----|---|---|----|-------
DHT22 3v|3v|1|2|5v|Garade doors 5v
no|2/SDA|3|4|5v|Watertank range 5v
no|3/SCL|5|6|GND|Garade doors Ground
DHT22 gpio|gpio4|7|8|14/TXD|no
DHT22 Ground|GND|9|10|15/RXD|no
Garage Alim gpio|gpio17|11|12|gpio18|Watertank range echo
no|gpio27|13|14|GND|no
Water pulse|gpio22|15|16|gpio23|Garage door 1 gpio 
Water 3v|3v|17|18|gpio24|Garage door 2 gpio 
no|10/MOSI|19|20|GND|Watertank range gnd
no|9/MISO|21|22|gpio25|Watertank range trig
no|11/SCKL|23|24|gpio8|no
Water Gound|GND|25|26|gpio7|no

## EVE
### Features
* Water Tank range detector
* Movement sensor

### GPIO

Feature|TYPE|PIN|PIN|TYPE|Feature
-------|----|---|---|----|-------
no|3v|1|2|5v|no
no|2/SDA|3|4|5v|no
no|3/SCL|5|6|GND|no
no|gpio4|7|8|14/TXD|no
no|GND|9|10|15/RXD|no
no|gpio17|11|12|gpio18|no
no|gpio27|13|14|GND|no
no|gpio22|15|16|gpio23|no
no|3v|17|18|gpio24|no
no|10/MOSI|19|20|GND|no
no|9/MISO|21|22|gpio25|no
no|11/SCKL|23|24|gpio8|no
no|GND|25|26|gpio7|no
