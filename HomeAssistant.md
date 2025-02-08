# Remote Pi
* pinctrl (test gpio pin)
* https://www.home-assistant.io/integrations/remote_rpi_gpio/

# Home Assistant
* Hoe Assistant Core (raspberry + gpio stuff)[here](https://www.home-assistant.io/installation/raspberrypi-other/)
   * https://wiki.lupsha.com/how-to-install-home-assistant-on-a-raspberry-pi/
   * before running `hass` command,
   * https://wiki.lupsha.com/how-to-upgrade-to-python-3-12-on-raspberry-pi/
   * sudo apt install samba -y
   * sudo nano /etc/samba/smb.conf
```
[global]
workgroup = WORKGROUP
server string = Samba Server %v
netbios name = HomeAssistant
security = user
map to guest = bad user
name resolve order = bcast host
dns proxy = no
bind interfaces only = yes

[Public]
path = /home/homeassistant/.homeassistant
writable = yes
guest ok = yes
guest only = yes
read only = no
create mode = 0777
directory mode = 0777
force user = nobody
create mask = 0777
directory mask = 0777
force user = root
force create mode = 0777
force directory mode = 0777
hosts allow =
```
* sudo smbpasswd -a USERNAME_OF_YOUR_CHOICE (existing user)
* sudo service smbd restart
* https://github.com/Kanga-Who/home-assistant/blob/master/Install%20Samba%2C%20Portainer%20and%20MQTT.md

```
python3 -m pip install numpy --upgrade
python3 -m pip install libtiff
```

`sudo nano /etc/systemd/system/ha@homeassistant.service`

```
[Unit]
Description=Home Assistant
After=network-online.target
After=network.target mosquitto.service

[Service]
Type=simple
User=%i
ExecStart=/srv/homeassistant/bin/hass

[Install]
WantedBy=multi-user.target
```
Then enable and start the services, in that order.
```
systemctl enable ha@homeassistant.service
systemctl start ha@homeassistant.service
```

* Home Assistant OS (installation from Raspberry Image mgr)
  * [mqtt](https://www.home-assistant.io/integrations/mqtt/)
  * [zigbee2mqtt](https://github.com/zigbee2mqtt/hassio-zigbee2mqtt#installation)
  * [Nginx Proxy Manager](https://github.com/hassio-addons/addon-nginx-proxy-manager/blob/main/proxy-manager/DOCS.md)
      * domain name (registred @ duckdns using github credz - keep track of duckdns token + domain name)
      * https
      * rasp IP
      * 8123
      * websocket support
      * SSL (Force SSL)
  * `configuration.yaml` : add lines  
```
python_script:

pyscript:
  allow_all_imports: true
  hass_is_global: true

logger:
  default: info
  logs:
    custom_components.pyscript: info

http:
  ssl_certificate: /ssl/fullchain.pem
  ssl_key: /ssl/privkey.pem
  use_x_forwarded_for: true
  trusted_proxies:
    - 172.30.33.0/24
```
  * ~Duck DNS (Proxy Host)~
  * Advanced SSH & Web Terminal
  * Samba share
  * Studio Code Server
  * SQLite Web
  * Log Viewer
  * [hotspot](https://github.com/joaofl/hassio-addons/tree/master/hassio-hotspot)
  * [Install HACS](https://www.hacs.xyz/)
     * HACS // Pyscript
     * HACS // Favicon (setup main title & icon for different HA installations)

# Automation
## Schedule
* [Schedule](https://www.home-assistant.io/integrations/schedule/)
* 

  
# Todo 
* [€/kWh](https://forum.hacf.fr/t/gerer-les-tarifs-de-son-fournisseur-delectricite-dans-le-tableau-energie/31512)
* [Telegram bot](https://community.home-assistant.io/t/telegram-inline-keyboard-template/98917/3)
    * [Telegram stuff](https://www.hacf.fr/ha_integration_telegram/) 
* [gpio](https://github.com/jdeneef/ha_gpiod) - weird unsupported integration
* [crazy charts](https://community.home-assistant.io/t/an-automated-pie-chart-of-all-power-consumers-in-my-home/644937)
* https://github.com/AlexxIT/go2rtc?tab=readme-ov-file#module-hass
* https://github.com/AlexxIT/WebRTC
* https://www.hacf.fr/gestion-eau/
* https://github.com/AlexxIT/PythonScriptsPro

* [Water Meter test 1](https://community.home-assistant.io/t/translated-values-to-save-every-5s/768879/2)

# NodeRed
* [start with NodeRed](https://mikehillyer.com/home-automation/getting-started-with-home-assistant-and-node-red/)
* [first steps](https://forum.hacf.fr/t/debuter-avec-node-red/334)

# Installation guide (docker compose)
* [Install docker](https://qbee.io/docs/tutorial-installing-docker-on-a-Raspberry-Pi.html)
   * `sudo usermod -aG docker $USER` _(see [fix docker access](https://stackoverflow.com/questions/48957195/how-to-fix-docker-got-permission-denied-issue))_
* [Installation HA+MQTT+NodeRed](https://pimylifeup.com/home-assistant-docker-compose/)
  * `Europe/Paris` 
* [Add Zigbee2MQTT](https://antoineperrin.fr/blog/home-assistant-docker-zigbee2mqtt/)
* [Setup Zigbee2MQTT](https://blog.domadoo.fr/106275-home-assistant-et-zigbee2mqtt-installation/)
