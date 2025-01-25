# Home Assistant
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
  * Studio Code Server
  * SQLite Web
  * Log Viewer
  * [hotspot](https://github.com/joaofl/hassio-addons/tree/master/hassio-hotspot)
  * [Install HACS](https://www.hacs.xyz/)
     * HACS // Pyscript

# Automation
## Schedule
* [Schedule](https://www.home-assistant.io/integrations/schedule/)
* 

  
# Todo 
* [€/kWh](https://forum.hacf.fr/t/gerer-les-tarifs-de-son-fournisseur-delectricite-dans-le-tableau-energie/31512)
* [Telegram bot](https://community.home-assistant.io/t/telegram-inline-keyboard-template/98917/3)

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
