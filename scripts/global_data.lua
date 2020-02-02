return {
   helpers = {
      myJenkinsCheckFunction = function(domoticz, jenkinsDevice, param2)
         -- do your stuff
         domoticz.log('Jenkins Check : '..jenkinsDevice.name)
         if ( jenkinsDevice.text ~= 'SUCCESS' ) then
	         domoticz.notify("Jenkins Alert", "Jenkins ["..jenkinsDevice.name.."] status invalide >"..jenkinsDevice.text.."<", domoticz.PRIORITY_NORMAL, domoticz.SOUND_ALIEN, nil, domoticz.NSS_TELEGRAM)      
         end
      end
  
      ,lcd_writeMessage = function(domoticz, message)
         -- do your stuff
         domoticz.log('LCD print : '..message)
         io.popen('python /home/pi/domoticz/scripts/python/EcranLCD/lcd.py '..tostring(message))
         domoticz.variables('LCD_Message').set(message)
         domoticz.variables('LCD_Message_buffer').set(message)
      end
      
      ,ftp_putHAL = function(domoticz, filenameSrc, pathTarget)
        -- push to HAL/ftp
        local file3 = assert(io.popen('/usr/bin/curl -s --disable-epsv -v -T"'.. filenameSrc ..'" -u papa:rtrtrt ftp://192.168.1.100/' .. pathTarget .. '/', 'r'))
        local output3 = file3:read('*all')
        file3:close()
        print('ftp put:' .. output3)
        domoticz.log('Put file [' .. filenameSrc .. '] on HAL[' .. pathTarget .. ']', domoticz.LOG_INFO)
      end
      
      ,ftp_getHAL = function(domoticz, filenameSrc, pathTarget)
        -- push to HAL/ftp
        local commandFtp = '/usr/bin/curl -p --disable-epsv -v -u papa:rtrtrt ftp://192.168.1.100/' .. filenameSrc .. ' -o "'.. pathTarget .. '"'
        local file3 = assert(io.popen(commandFtp, 'r'))
        local output3 = file3:read('*all')
        file3:close()
        print('ftp get:' .. output3)
        domoticz.log(commandFtp)
        domoticz.log('Get file [' .. filenameSrc .. '] on HAL to put local [' .. pathTarget .. ']', domoticz.LOG_INFO)
      end
  
      ,myHandyFunction = function(domoticz, param1, param2)
         -- do your stuff
         domoticz.log('Hey')
      end
   }
}