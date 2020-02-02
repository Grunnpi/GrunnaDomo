return {
    active = true,
	on = {
		variables = {
			'TemperatureHumidity_Cave'
		}
	},
	execute = function(domoticz, variable)
	    
	    local verbose = false
	    
		if ( verbose ) then
	        domoticz.log('Variable ' .. variable.name .. ' was changed', domoticz.LOG_INFO)
		end
		
		deviceName = string.gsub( variable.name, "TemperatureHumidity_", "")
		
		--domoticz.log('Device Name  : ' .. deviceName)
		
		local temperatureHumidityDevice = domoticz.devices(deviceName)
		local temperatureString, humidity, otherStuff = string.match(variable.value, '(.*);.*;.*'), string.match(variable.value, '.*;(.*);.*'), string.match(variable.value, '.*;.*;(.*)')
		
		if ( verbose ) then
		    domoticz.log('variable temperature : ' .. temperatureString) --decimal
		    domoticz.log('variable humidity : ' .. humidity) --decimal
		    domoticz.log('variable stuff : ' .. otherStuff) --decimal
	    end
	    
		newTemperature = tonumber(temperatureString)
		newHumidity = tonumber(humidity)
		
		if ( verbore ) then
		    -- last time / value for TemperatureHumidity device
		    domoticz.log('last update : ' .. temperatureHumidityDevice.lastUpdate.minutesAgo .. ' min, ' .. temperatureHumidityDevice.lastUpdate.secondsAgo .. ' seconds')
		    domoticz.log('last temperature : ' .. temperatureHumidityDevice.temperature) --integer
    		if ( tonumber(humidity) <= 100 ) then
        		domoticz.log('last humidity : ' .. temperatureHumidityDevice.humidity) --decimal
    	    end
		end
		
		updateTemperature = true
		if ( temperatureHumidityDevice.lastUpdate.minutesAgo < 35 ) then -- less than 1/2h since last update ?
	        -- maximum 3 degree difference
	        temperatureDifference = math.abs(newTemperature - temperatureHumidityDevice.temperature)
	        if ( temperatureDifference > 3 ) then
	            updateTemperature = false
            end
	    else
	        -- ok whatever
	    end
	    
	    if ( updateTemperature ) then
	        if ( verbose ) then
                domoticz.log('update temperature with : ' .. newTemperature) --decimal
    		end
    		if ( tonumber(humidity) <= 100 ) then
                temperatureHumidityDevice.updateTempHum(newTemperature, newHumidity, domoticz.HUM_DRY)
            else
                temperatureHumidityDevice.updateTemperature(newTemperature)
            end
        else
            domoticz.log('weird value, do not update temperature with : ' .. newTemperature, domoticz.LOG_ERROR) --decimal
            --domoticz.notify("Domoticz", "Temperature ["..variable.name.."] difference = " .. temperatureDifference .. " for newTemperature ".. newTemperature .. ", not updated !", domoticz.PRIORITY_NORMAL, domoticz.SOUND_ALIEN, nil, domoticz.NSS_TELEGRAM)           
        end
	end
}