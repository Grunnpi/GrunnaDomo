return {
	on = {
		timer = {
			'at 20:00'
			,'at 18:00'
			,'at 12:30'
			
			--,' every minute'
	   },
    },
	execute = function(domoticz, timer)
		domoticz.log('Timer event was triggered by ' .. timer.trigger, domoticz.LOG_INFO)
	    
	    local volumeParPlein = domoticz.variables("Adoucisseur_VolumeParPlein").value
	    local dernierPlein = domoticz.variables("Adoucisseur_DernierPlein").value
	    local waterMeter = domoticz.devices('WaterMeter')
	    
	    local volumeConsome = (waterMeter.counter * 1000) - tonumber(dernierPlein)
	    domoticz.log('Eau ' .. waterMeter.counter .. ', volumeConsome=' .. volumeConsome, domoticz.LOG_INFO)
	    if ( volumeConsome > volumeParPlein ) then
    	    domoticz.notify("Adoucisseur Alert", "Remettre du sel dans l'adoucisseur (" .. tostring(volumeConsome) .. " litres depuis le dernier plein (seuil:" .. volumeParPlein .." litres)", domoticz.PRIORITY_NORMAL, domoticz.SOUND_ALIEN, nil, domoticz.NSS_TELEGRAM)  
        end 

	end
}
