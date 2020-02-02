return {
    active = true,
	on = {
		devices = {
			'Cuve_distance'
		}
	},
	execute = function(domoticz, device)
	    
	    local verbose = true
	    
	    -- entre capteur et fond de la cuve
	    local distanceMax = 204
	    -- entre capteur et niveau de l'eau max de la cuve
	    local distanceMin = 60
	    
	    local pourcentageCuve = 0
	    
	    local distanceMesure = device.distance
	    -- distanceMesure = distanceMesure * 1.7
	    
	    pourcentageCuve = 1 - ( (distanceMesure - distanceMin) / (distanceMax - distanceMin))
	    pourcentageCuve = pourcentageCuve * 100
	    
		if ( verbose ) then
	        domoticz.log('distance ' .. device.name .. ' mise à jour :  ' .. device.distance .. '/' .. distanceMesure .. ' : cuve pourcentage ' .. pourcentageCuve, domoticz.LOG_INFO)
		end
		
		domoticz.devices("Cuve_pourcentage").updatePercentage(pourcentageCuve)
	end
}