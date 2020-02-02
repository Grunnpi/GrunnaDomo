return {
	on = {
		variables = {
			'LCD_Message'
		}
	},
	execute = function(domoticz, variable)
		domoticz.log('Variable ' .. variable.name .. ' was changed', domoticz.LOG_INFO)
		if ( domoticz.variables('LCD_Message').value ~= domoticz.variables('LCD_Message_buffer').value ) then
		    if ( domoticz.variables('LCD_Message').value == 'off' ) then
		        domoticz.variables('Bouton_Etat').set('off')
	        end
		    domoticz.helpers.lcd_writeMessage(domoticz,variable.value)
	    end
		-- code
	end
}