return {
	on = {
		timer = {
--			'every minute',              -- causes the script to be called every minute
			'at 18:00',                  -- specific time
	   },
    },
	execute = function(domoticz, timer)
	    temperature_24h_seuil = domoticz.variables('Temperature_24h_seuil').value
		if ( domoticz.devices("Robinet_Terrasse").bState and domoticz.devices("Detection_Gel24h").bState) then
		    domoticz.log('Temperature sous [' .. tostring(temperature_24h_seuil) .. '] ces dernieres 24h > msg telegram', domoticz.LOG_INFO)
		    domoticz.notify("Robinet", "⚠️ Attention ⚠️,\n  Temperature sous [" .. tostring(temperature_24h_seuil) .. "] ces dernieres 24h. \n ❄️ Il faut vidanger le robinet de la terrasse !", domoticz.PRIORITY_NORMAL, domoticz.SOUND_ALIEN, nil, domoticz.NSS_TELEGRAM)  
	    end
	    domoticz.devices('Detection_Gel24h').switchOff()
	end
}
