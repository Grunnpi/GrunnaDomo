return {
	on = {
		timer = {
			'every minute',              -- causes the script to be called every minute
	   },
    },
	execute = function(domoticz, timer)
		local command = 'ps -aux | grep dtgbot.pid | grep -v grep'
		local handle = io.popen(command)
        local check_bot = handle:read("*a")
        handle:close()
        
        local bot_present = true
		if ( not not string.find(check_bot,"^%s*$") ) then
		    bot_present = false
	    else
	        
	        command = "awk '/./{line=$0} END{print line}' /var/tmp/dtgloop.txt"
		    handle = io.popen(command)
            local retour_dtgloop = handle:read("*a")
            handle:close()
            retour_dtgloop = string.gsub(retour_dtgloop,"[\r\n]", "")
            
            local retour_dtgloop_var = domoticz.variables("TelegramBotLastLoop")
            if ( retour_dtgloop_var ~= nil ) then
                retour_dtgloop_actuel = retour_dtgloop_var.value
                if ( retour_dtgloop_actuel == retour_dtgloop ) then
                    if (retour_dtgloop_var.lastUpdate.minutesAgo > 4) then
                        bot_present = false
                    end
                else
                    domoticz.variables("TelegramBotLastLoop").set(retour_dtgloop)
                end
            else
                retour_dtgloop_actuel = ""
            end
            
	        -- seems ok, we should try to talk to the bot...
	        domoticz.log('Bot process present, dernier dtgloop[' .. retour_dtgloop .. '] avant [' .. retour_dtgloop_actuel .. '] depuis [' .. retour_dtgloop_var.lastUpdate.minutesAgo .. ']', domoticz.LOG_INFO)

		    --bot_present = true
		end
		
		if ( not bot_present ) then
            domoticz.log('try to restart bot up ', domoticz.LOG_INFO)
            domoticz.notify("Bot", "Attention,\n bot non detecté : tentative de redémarrage",domoticz.PRIORITY_NORMAL, domoticz.SOUND_ALIEN, nil, domoticz.NSS_TELEGRAM)  

		    -- blank, possible bot down : alert and restart
	        command = 'sudo service dtgbot restart'
		    handle = io.popen(command)
            local restart_bot = handle:read("*a")
            handle:close()
		end
	end
}
