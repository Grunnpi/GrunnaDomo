return {
	on = {
		devices = {
			'THB'
		}
	},
	execute = function(domoticz, device)
		domoticz.log('Device ' .. device.name .. ' was changed', domoticz.LOG_INFO)
		
		temperature_24h_seuil = domoticz.variables('Temperature_24h_seuil').value
		
		
		if ( device.temperature < temperature_24h_seuil ) then
		    domoticz.devices('Detection_Gel24h').switchOn()
	    end
	end
}