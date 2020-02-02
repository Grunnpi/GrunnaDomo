--[[
    active when function returns true ( domoticz started less then 180 seconds ago )  
    
    The defined tasks will only execute once after domoticz started.
    Please note that in theory this is not a failsafe way of handling this. 
    
    If domoticz crashes / is stopped after the first excution of this script and before 120 seconds after 
    it started, the Executed value is not set back to 0 and the script needs to be reloaded to reset the persistent data.
    
    If domoticz starts extremely slow, in theory it could be that this script will not be evaluated before the 180 seconds 
    after startup has passed. On my test system (PI-3), first execution is well within that window. (somewhere between 13 and 60 seconds)
    
 ]]-- 
 
 
return {
    active = function(domoticz)
              return domoticz.startTime.secondsAgo < 180
            end,
    
    on       = {      timer     = { 'every minute'  } },
    
    data     = {     Executed     = { initial = 0 } },
           
    execute = function(domoticz)
        if domoticz.data.Executed == 0 then
            myName = domoticz.variables('TelegramBotName').value
            domoticz.notify("Domoticz startup", "Domoticz ["..myName.."] restarted !", domoticz.PRIORITY_NORMAL, domoticz.SOUND_ALIEN, nil, domoticz.NSS_TELEGRAM)           
        else
            print ("Älready executed; " .. tostring(domoticz.data.Executed) .. " seconds after domoticz started.")
            if domoticz.startTime.secondsAgo > 119 then
                domoticz.data.Executed = 0
            end    
        end            
    end
}