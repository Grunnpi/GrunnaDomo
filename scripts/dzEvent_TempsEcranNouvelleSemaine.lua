return {
	on = {
		timer = {
			'at 1:00 on mon' -- lundi 1h
	   },
    },
	execute = function(domoticz, timer)
		domoticz.log('Reset temps écran pour nouvelle semaine by ' .. timer.trigger, domoticz.LOG_INFO)
		
		local minutesParSemaine = domoticz.variables("TempsEcranSemaineJeremie").value
		domoticz.variables("TempsEcranJeremie").set(minutesParSemaine)
		
		minutesParSemaine = domoticz.variables("TempsEcranSemaineMatthieu").value
		domoticz.variables("TempsEcranMatthieu").set(minutesParSemaine)
	end
}
