return {
	on = {
		devices = {
			'TempsEcranJeremie',
			'TempsEcranMatthieu'
		}
	},
	execute = function(domoticz, device)
		domoticz.log('Device ' .. device.name .. ' was changed', domoticz.LOG_INFO)
		
		--temperature_24h_seuil = domoticz.variables('Temperature_24h_seuil').value
		local minutesRestante = domoticz.variables(device.name).value
		if ( device.bState ) then
		    -- Il est sur son écran
		    domoticz.log('il reste : ' .. minutesRestante .. ' min')
            domoticz.notify("Domoticz", "Debut ["..device.name.."] solde total = " .. minutesRestante .. " minutes", domoticz.PRIORITY_NORMAL, domoticz.SOUND_ALIEN, nil, domoticz.NSS_TELEGRAM)    
            domoticz.variables(device.name).set(minutesRestante)

		else    
		    -- Stop de temps d'écran
    		domoticz.log('allumé depuis : ' .. domoticz.variables(device.name).lastUpdate.minutesAgo .. ' min')
    		if ( domoticz.variables(device.name).lastUpdate.minutesAgo > 0 ) then
    		    minutesRestante = minutesRestante - domoticz.variables(device.name).lastUpdate.minutesAgo
    		    domoticz.variables(device.name).set(minutesRestante)
		    end
            domoticz.notify("Domoticz", "Fin ["..device.name.."] apres ".. domoticz.variables(device.name).lastUpdate.minutesAgo.. "min\nSolde restant = " .. minutesRestante .. " minutes", domoticz.PRIORITY_NORMAL, domoticz.SOUND_ALIEN, nil, domoticz.NSS_TELEGRAM)           
		end
	end
}