return {
	on = {
		timer = {
			'at 18:00'
	   },
    },
	execute = function(domoticz, timer)
	    local Dir_01_Photo = domoticz.devices('Dir_01_Photo')
        domoticz.helpers.myJenkinsCheckFunction(domoticz, Dir_01_Photo, 'boo')
	    
	    local Dir_08_Photo_USB1 = domoticz.devices('Dir_08_Photo_USB1')
        domoticz.helpers.myJenkinsCheckFunction(domoticz, Dir_08_Photo_USB1, 'boo')
        
        local Dir_08_Photo_USB2 = domoticz.devices('Dir_09_Photo_USB2')
        domoticz.helpers.myJenkinsCheckFunction(domoticz, Dir_08_Photo_USB2, 'boo')
        
        local Dir_08_Photo_USB3 = domoticz.devices('Dir_10_Photo_USB3')
        domoticz.helpers.myJenkinsCheckFunction(domoticz, Dir_08_Photo_USB3, 'boo')
        
		domoticz.log('Timer event was triggered by ' .. timer.trigger, domoticz.LOG_INFO)
	end
}
