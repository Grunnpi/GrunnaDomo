# GrunnDomo
All my domotic stuff summarized

## All Raspberry

### Installation
* Domoticz  
    * Wiki provided by Domoticz [here](https://www.domoticz.com/wiki/Raspberry_Pi)
* Telegram bot
    * Use *BotFather* to create bot _(token / my user id)_
* dtgbot
    * Use my own fork [dtgbot](https://github.com/Grunnpi/dtgbot)
* WiringPi for GPIO control
    * Use [WiringPi guide](WiringPi.md)
* DHT22 temperature/humidity
    * Use [DHT22 guide](DHT22.md)
* MotionEye
    * Follow official [MotionEye](https://github.com/ccrisan/motioneye) distribution

## BOB
* Electricity counter
* Webcam

### GPIO

Feature|TYPE|PIN|PIN|TYPE|Feature
-------|----|---|---|----|-------
no|x|1|2|x|no
no|x|3|4|x|no
no|x|5|6|x|no
no|x|7|8|x|no
no|x|9|10|x|no
no|x|11|12|x|no
no|x|13|14|x|no
no|x|15|16|x|no
no|x|17|18|x|no
no|x|19|20|x|no
no|x|21|22|x|no
no|x|23|24|x|no
no|x|25|26|x|no

## BIL
### Features
* Water counter
* Temperature/Humidity
* Garage door
* Webcam

### GPIO

Feature|TYPE|PIN|PIN|TYPE|Feature
-------|----|---|---|----|-------
DHT22 3v|3v|1|2|5v|Garade doors 5v
no|x|3|4|x|no
no|x|5|6|GND|Garade doors Ground
DHT22 gpio|gpio4|7|8|x|no
DHT22 Ground|GND|9|10|x|no
Garage Alim gpio|gpio17|11|12|x|no
no|x|13|14|x|no
Water pulse|gpio22|15|16|gpio23|Garage door 1 gpio 
Water 3v|3v|17|18|gpio24|Garage door 2 gpio 
no|x|19|20|x|no
no|x|21|22|x|no
no|x|23|24|x|no
Water Gound|GND|25|26|x|no
