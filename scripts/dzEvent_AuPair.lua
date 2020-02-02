return {
	on = {
		devices = {
			'AuPair'
		}
	},
	execute = function(domoticz, device)
		domoticz.log('Device ' .. device.name .. ' was changed', domoticz.LOG_INFO)
		if ( device.bState ) then
		    domoticz.log('On est a AuPair = oui, alors action puis off', domoticz.LOG_INFO)
		    
		    if ( domoticz.devices("AuPair_actif").bState ) then
		        token = domoticz.variables('TelegramBotScriptToken').value
                chatid = domoticz.variables('TelegramBotScriptChatId').value
                
    		    -- execute AuPair for real
    		    local auPairCommand = 'nohup /usr/bin/python3 /home/pi/domoticz/scripts/python/AuPairTool/AuPair.py --user pierre.grunnagel@gmail.com --pwd Mdpaupair197619784 --cred "/home/pi/domoticz/scripts/python/AuPair.json" --token "'.. token ..'" --chatid "' ..chatid .. '" > /var/tmp/AuPair/auPair.log 2>&1 &'
    		    
    		    domoticz.log('AuPairCommand.in[' .. auPairCommand .. ']')
    		    io.popen(auPairCommand)
    		   
                --domoticz.notify("AuPair", "AuPair fetch lancé", domoticz.PRIORITY_NORMAL, domoticz.SOUND_ALIEN, nil, domoticz.NSS_TELEGRAM)      
	        else
	            domoticz.log('Process AuPair en mode off. Alors on skip', domoticz.LOG_INFO)
	        end
	        
		    device.switchOff()
	    end
	end
}