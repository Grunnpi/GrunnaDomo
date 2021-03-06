# GrunnDomo
All my domotic stuff summarized

## All Raspberry

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
