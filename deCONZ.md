# Official doc

[here](https://phoscon.de/en/conbee/install#raspbian)

# Quick steps

* Install deCONZ package following official guide
* Install Domoticz plugin : (https://github.com/Smanar/Domoticz-deCONZ)
* Switch to deCONZ Headless :
    * sudo systemctl disable deconz-gui
    * sudo systemctl stop deconz-gui
    * sudo systemctl enable deconz
* Switch back to deCONZ GUI :
    * sudo systemctl disable deconz
    * sudo systemctl stop deconz
    * sudo systemctl enable deconz-gui

Note : it sounds like a partial package can be updated more often and worth to be upgraded sometimes (https://github.com/dresden-elektronik/deconz-rest-plugin)
