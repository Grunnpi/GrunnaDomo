return {
	on = {
		timer = {
		--	'at 15:17',                  -- specific time
			'at 01:00',                  -- specific time
	   },
    },
	execute = function(domoticz, timer)
		
		local domoticz_ip = '192.168.1.110'
		local domoticz_port = '8180'
		local domoticz_alias = 'BOB'
		
		domoticz.log('Backup to HAL event was triggered by ' .. timer.trigger, domoticz.LOG_INFO)
		
		local ts = os.time()
		local backup_name_targz = os.date('%Y-%m-%d_%H%M%S', ts) .. '_domoticz_backup.tar.gz'
		
		-- create dir tree
		io.popen('mkdir /var/tmp/domoticz_backup')
		io.popen('mkdir /var/tmp/domoticz_backup/scripts')
		io.popen('mkdir /var/tmp/domoticz_backup/scripts/lua')
		io.popen('mkdir /var/tmp/domoticz_backup/scripts/lua_parsers')
		io.popen('mkdir /var/tmp/domoticz_backup/scripts/python')
		
		-- copy 
        local file1 = assert(io.popen('/usr/bin/curl -s http://' .. domoticz_ip ..':' .. domoticz_port .. '/backupdatabase.php > /var/tmp/domoticz_backup/domoticz.db', 'r'))
        local output1 = file1:read('*all')
        file1:close()
        print('backup db:' .. output1)
        
        io.popen('cp -R /home/pi/domoticz/scripts/lua/*.* /var/tmp/domoticz_backup/scripts/lua')
        io.popen('cp -R /home/pi/domoticz/scripts/lua_parsers/*.* /var/tmp/domoticz_backup/scripts/lua_parsers')
        io.popen('cp -R /home/pi/domoticz/scripts/python/*.py /var/tmp/domoticz_backup/scripts/python')
        
        os.execute('sleep 5')
        
        -- compress stuff        
        local file2 = assert(io.popen('tar cvzf "/var/tmp/'.. backup_name_targz ..'" /var/tmp/domoticz_backup', 'r'))
        local output2 = file2:read('*all')
        file2:close()
        print('tar :' .. output2)
        
        -- push to HAL/ftp
        local file3 = assert(io.popen('/usr/bin/curl -s --disable-epsv -v -T"/var/tmp/'.. backup_name_targz ..'" -u papa:rtrtrt ftp://192.168.1.100//media/HDD1_1To/home/Domoticz/' .. domoticz_alias .. '/', 'r'))
        local output3 = file3:read('*all')
        file3:close()
        print('ftp put:' .. output3)

        -- cleanup
        io.popen('rm /var/tmp/'.. backup_name_targz)
        io.popen('rm -r /var/tmp/domoticz_backup')
	end
}
