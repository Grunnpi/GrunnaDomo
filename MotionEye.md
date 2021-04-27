# MotionEye

Today _(6th Nov 2019)_ instsallation following official instruction failed.  
I don't remember how I did last time, but anymay, here is what I do today

official [MotionEye](https://github.com/ccrisan/motioneye) distribution

What|Why
----|---
``sudo -i``|easier to switch up to sudo for all next steps
``apt-get install motion``|motion regular package, as dependencies in official doc are outdated.
``apt-get install python-pillow``|as direct motionEye install failed
``apt-get install libssl-dev libcurl4-openssl-dev python-dev``|install some dependencies regarding pycurl stuff
``pip install pycurl``|yeah
``pip install --no-cache-dir motioneye``| motionEye on top by Python installer with my small Raspberry
or ``python2.7 -m pip install --no-cache-dir motioneye``| to force python2 usage
...|then follow official instructions

# MotionEye front end setup

Once installed, and webcam added, configure "motion detection" to ON and "motion notification" with *"your_ID"* a custom switch id defined in Domoticz. 

For **Run a command**    
``/usr/bin/curl -s "http://domoticz_server:domoticz_port/json.htm?type=command&param=switchlight&idx=your_ID&switchcmd=On"``

For **Run an end command**   
``/usr/bin/curl -s "http://domoticz_server:domoticz_port/json.htm?type=command&param=switchlight&idx=your_ID&switchcmd=Off"``

In Domoticz, LUA event can be defined as following :

```
commandArray = {}

if (otherdevices['Mouvement_detection_actif'] == 'On')
then
    if (devicechanged['Mouvement_detection'] == 'On')
    then
        message = 'Detection mouvement debut'
        if (otherdevices['Mouvement_notification_actif'] == 'On')
        then
            token = uservariables["TelegramBotScriptToken"]
            chatid = uservariables["TelegramBotScriptChatId"]
            print(message..' et notification')
    
            os.execute('curl -o /var/tmp/toto.jpg http://$DomoticzIP:8765/picture/1/current')
            os.execute('curl -s -X POST "https://api.telegram.org/bot'..token..'/sendPhoto" -F chat_id='..chatid..' -F photo="@/var/tmp/toto.jpg" -F caption="'..message..'"')
            os.execute('rm /var/tmp/toto.jpg')
        else
            print(message..' log seulement')
        end
    elseif(devicechanged['Mouvement_detection'] == 'Off') 
    then
        message = 'Detection mouvement fin'
        if (otherdevices['Mouvement_notification_actif'] == 'On')
        then
            token = uservariables["TelegramBotScriptToken"]
            chatid = uservariables["TelegramBotScriptChatId"]
            print(message..' et notification')
            os.execute('curl --data chat_id='..chatid..' --data-urlencode "text='..message..'"  "https://api.telegram.org/bot'..token..'/sendMessage" ')
        else
            print(message..' log seulement')
        end
    end
end

return commandArray
```
