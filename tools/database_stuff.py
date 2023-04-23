# Glob Watt
# python3 /home/pi/domoticz/scripts/python/Solaire/DomoticzDB-overflow/main.py --type=watt --action=clone --idx_src=228 --idx_dst=606 --option=full
# F1 Watt
# python3 /home/pi/domoticz/scripts/python/Solaire/DomoticzDB-overflow/main.py --type=watt --action=clone --idx_src=231 --idx_dst=607 --option=full
# F2 Watt
# python3 /home/pi/domoticz/scripts/python/Solaire/DomoticzDB-overflow/main.py --type=watt --action=clone --idx_src=235 --idx_dst=608 --option=full
# F3 Watt
# python3 /home/pi/domoticz/scripts/python/Solaire/DomoticzDB-overflow/main.py --type=watt --action=clone --idx_src=239 --idx_dst=609 --option=full

# F2 kwh
# python3 /home/pi/domoticz/scripts/python/Solaire/DomoticzDB-overflow/main.py --type=kwh --action=clonefix --idx_src=234 --idx_dst=588 --option=full
# python3 /home/pi/domoticz/scripts/python/Solaire/DomoticzDB-overflow/main.py --type=kwh --action=clonefix --idx_src=234 --idx_dst=588 --option=back
# F3 kwh
# python3 /home/pi/domoticz/scripts/python/Solaire/DomoticzDB-overflow/main.py --type=kwh --action=clonefix --idx_src=238 --idx_dst=589 --option=full
# python3 /home/pi/domoticz/scripts/python/Solaire/DomoticzDB-overflow/main.py --type=kwh --action=clonefix --idx_src=238 --idx_dst=589 --option=back
# F1 kwh
# python3 /home/pi/domoticz/scripts/python/Solaire/DomoticzDB-overflow/main.py --type=kwh --action=clonefix --idx_src=230 --idx_dst=587 --option=full
# python3 /home/pi/domoticz/scripts/python/Solaire/DomoticzDB-overflow/main.py --type=kwh --action=clonefix --idx_src=230 --idx_dst=587 --option=back
# Glob kwh
# python3 /home/pi/domoticz/scripts/python/Solaire/DomoticzDB-overflow/main.py --type=kwh --action=clonefix --idx_src=227 --idx_dst=590 --option=full
# python3 /home/pi/domoticz/scripts/python/Solaire/DomoticzDB-overflow/main.py --type=kwh --action=clonefix --idx_src=227 --idx_dst=590 --option=back

# Panneaux
# python3 /home/pi/domoticz/scripts/python/Solaire/DomoticzDB-overflow/main.py --type=watt --action=panneaux --idx_src=259 --idx_dst=594 --option=full
# Panneaux fix kWh cumulated
# python3 /home/pi/domoticz/scripts/python/Solaire/DomoticzDB-overflow/main.py --type=kwh --action=panneaux --idx_src=260 --idx_dst=593 --option=full
# Panneaux fix Watt cumulated
# python3 /home/pi/domoticz/scripts/python/Solaire/DomoticzDB-overflow/main.py --type=kwh --action=panneaux_auj --idx_src=590 --idx_dst=590 --option=full

# Panneaux fix Perdu
# python3 /home/pi/domoticz/scripts/python/Solaire/DomoticzDB-overflow/main.py --type=kwh --action=perdu --idx_src=611 --idx_dst=611 --option=fix
# python3 /home/pi/domoticz/scripts/python/Solaire/DomoticzDB-overflow/main.py --type=kwh --action=clonefix --idx_src=611 --idx_dst=611 --option=back

# Conso2
# python3 /home/pi/domoticz/scripts/python/Solaire/DomoticzDB-overflow/main.py --type=kwh --action=clonefix --idx_src=260 --idx_dst=260 --option=back

# Eau fix (marche pas)
# python3 /home/pi/domoticz/scripts/python/Solaire/DomoticzDB-overflow/main.py --type=eau --action=fix --idx_src=57 --idx_dst=57  --option=back

# export energie
# python3 /home/pi/domoticz/scripts/python/Solaire/DomoticzDB-overflow/main.py --type=kwh --action=export

import sqlite3
import traceback
import sys
import argparse


def f_export_kwh(connect, data_type, option):
    cur = connect.cursor()
    sql_ok = True
    try:

        Value = [i[0] for i in cur.execute("SELECT Value FROM Meter WHERE DeviceRowID = '" + idx_src + "' ORDER BY Date DESC")] # litre cumulé
        Usage = [i[0] for i in cur.execute("SELECT Usage FROM Meter WHERE DeviceRowID = '" + idx_src + "' ORDER BY Date DESC")] # 0 toujours
        Date  = [i[0] for i in cur.execute("SELECT Date  FROM Meter WHERE DeviceRowID = '" + idx_src + "' ORDER BY Date DESC")]

        firstValueNeg = False
        index = 0
        cumulatedValue = int("0")
        for iUsage in Usage:
            iValue = Value[index]
            iDate = Date[index]


            # compute cumulated stuff on our own
            print("ori:" + str(iValue) + "," + str(iUsage) + "," + iDate)
            iValue = iValue + 2452
            print("fix:" + str(iValue) + "," + str(iUsage) + "," + iDate)
            cur.execute("UPDATE Meter SET Value = " + str(iValue) + " WHERE DeviceRowID = '" + idx_dst + "' and date = '" + str(iDate) + "'")

            index += 1
        connect.commit()
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
        connect.rollback()
        sql_ok = False
    if (sql_ok):
        print("export kwh success")
    else:
        print("export kwh failed")


def f_eau_fix(connect, data_type, idx_src, idx_dst, option):
    cur = connect.cursor()
    sql_ok = True
    try:


        # and date >= '2023-04-21'
        # and date >= '2023-04-21'
        # and date >= '2023-04-21'



        if ( option == "back" ):
            Value = [i[0] for i in cur.execute("SELECT Value FROM Meter WHERE DeviceRowID = '" + idx_src + "' ORDER BY Date DESC")] # litre cumulé
            Usage = [i[0] for i in cur.execute("SELECT Usage FROM Meter WHERE DeviceRowID = '" + idx_src + "' ORDER BY Date DESC")] # 0 toujours
            Date  = [i[0] for i in cur.execute("SELECT Date  FROM Meter WHERE DeviceRowID = '" + idx_src + "' ORDER BY Date DESC")]

            firstValueNeg = False
            index = 0
            cumulatedValue = int("0")
            for iUsage in Usage:
                iValue = Value[index]
                iDate = Date[index]


                # compute cumulated stuff on our own
                print("ori:" + str(iValue) + "," + str(iUsage) + "," + iDate)
                iValue = iValue + 2452
                print("fix:" + str(iValue) + "," + str(iUsage) + "," + iDate)
                cur.execute("UPDATE Meter SET Value = " + str(iValue) + " WHERE DeviceRowID = '" + idx_dst + "' and date = '" + str(iDate) + "'")

                index += 1

        connect.commit()
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
        connect.rollback()
        sql_ok = False
    if (sql_ok):
        print("eauFix success")
    else:
        print("eauFix failed")

def f_perdu(connect, data_type, idx_src, idx_dst, option):
    cur = connect.cursor()
    sql_ok = True
    try:

        if ( option == "fix" ):
            Value = [i[0] for i in cur.execute("SELECT Value FROM Meter WHERE DeviceRowID = '" + idx_src + "' ORDER BY Date ASC")]
            Usage = [i[0] for i in cur.execute("SELECT Usage FROM Meter WHERE DeviceRowID = '" + idx_src + "' ORDER BY Date ASC")]
            Date  = [i[0] for i in cur.execute("SELECT Date  FROM Meter WHERE DeviceRowID = '" + idx_src + "' ORDER BY Date ASC")]

            firstValueNeg = False
            index = 0
            cumulatedValue = int("0")
            for iUsage in Usage:
                iValue = Value[index]
                iDate = Date[index]

                if (iUsage > 0 ):
                    firstValueNeg = True

                if ( firstValueNeg ):
                    # compute cumulated stuff on our own
                    print("ori:" + str(iValue) + "," + str(iUsage) + "," + iDate)
                    cumulatedValue += int(iUsage*(5/60)/10)
                    print("fix:" + str(cumulatedValue) + "," + str(iUsage) + "," + iDate)
                    cur.execute("UPDATE Meter SET Value = " + str(cumulatedValue) + " WHERE DeviceRowID = '" + idx_dst + "' and date = '" + str(iDate) + "'")
                else:
                    print("xxx:" + str(iValue) + "," + str(iUsage) + "," + iDate)
                    cumulatedValue = int( int(iValue) / 10)
                index += 1

        connect.commit()
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
        connect.rollback()
        sql_ok = False
    if (sql_ok):
        print("CloneFix success")
    else:
        print("CloneFix failed")

def f_full_clone_fix(connect, data_type, idx_src, idx_dst, option):
    cur = connect.cursor()
    sql_ok = True
    try:

        if ( option == "back"  ):

            Value = [i[0] for i in cur.execute("SELECT Value FROM Meter WHERE DeviceRowID = '" + idx_dst + "' ORDER BY Date DESC")]
            Usage = [i[0] for i in cur.execute("SELECT Usage FROM Meter WHERE DeviceRowID = '" + idx_dst + "' ORDER BY Date DESC")]
            Date  = [i[0] for i in cur.execute("SELECT Date  FROM Meter WHERE DeviceRowID = '" + idx_dst + "' ORDER BY Date DESC")]

            firstValueNeg = False
            index = 0
            cumulatedValue = int("0")
            for iUsage in Usage:
                iValue = Value[index]
                iDate = Date[index]

                if ( firstValueNeg ):
                    # compute cumulated stuff on our own

                    print("ori:" + str(iValue) + "," + str(iUsage) + "," + iDate)
                    cumulatedValue -= int(iUsage*(5/60)/10)
                    print("fix:" + str(cumulatedValue) + "," + str(iUsage) + "," + iDate)
                    cur.execute("UPDATE Meter SET Value = " + str(cumulatedValue) + " WHERE DeviceRowID = '" + idx_dst + "' and date = '" + str(iDate) + "'")
                else:
                    print("zero:" + str(iValue) + "," + str(iUsage) + "," + iDate)
                    cumulatedValue = int(iValue)
                    firstValueNeg = True
                index += 1

        if ( option == "full" or option == "Meter" ):
            cur.execute("DELETE FROM Meter WHERE DeviceRowID = '" + idx_dst + "'") # empty target
            cur.execute("UPDATE Meter SET Usage = (((Usage/10) - 16777216)*10) WHERE DeviceRowID = '" + idx_src + "' AND Usage > 100000") # clean src for wrong values

            Value = [i[0] for i in cur.execute("SELECT Value FROM Meter WHERE DeviceRowID = '" + idx_src + "' ORDER BY Date ASC")]
            Usage = [i[0] for i in cur.execute("SELECT Usage FROM Meter WHERE DeviceRowID = '" + idx_src + "' ORDER BY Date ASC")]
            Date  = [i[0] for i in cur.execute("SELECT Date  FROM Meter WHERE DeviceRowID = '" + idx_src + "' ORDER BY Date ASC")]

            firstValueNeg = False
            index = 0
            cumulatedValue = int("0")
            for iUsage in Usage:
                iValue = Value[index]
                iDate = Date[index]

                if (iUsage < 0 or iUsage > 100000):
                    firstValueNeg = True

                if ( firstValueNeg ):
                    # compute cumulated stuff on our own

                    print("ori:" + str(iValue) + "," + str(iUsage) + "," + iDate)
                    cumulatedValue += int(iUsage*(5/60)/10)
                    print("fix:" + str(cumulatedValue) + "," + str(iUsage) + "," + iDate)
                    cur.execute("INSERT INTO Meter ( DeviceRowID, Usage, Value, Date ) VALUES ( " + idx_dst + "," + str(iUsage) + "," + str(cumulatedValue) + ",'" + iDate + "')")
                else:
                    print("xxx:" + str(iValue) + "," + str(iUsage) + "," + iDate)
                    cur.execute("INSERT INTO Meter ( DeviceRowID, Usage, Value, Date ) VALUES ( " + idx_dst + "," + str(iUsage) + "," + str(iValue) + "/10,'" + iDate + "')")
                    cumulatedValue = int( int(iValue) / 10)
                index += 1

        if ( option == "full" or option == "Calendar" ):
            cur.execute("DELETE FROM Meter_Calendar WHERE DeviceRowID = '" + idx_dst + "'")
            cur.execute("INSERT INTO Meter_Calendar ( DeviceRowID, Value, Counter, Date ) SELECT " + idx_dst + ", Value, Counter/10, Date FROM Meter_Calendar WHERE DeviceRowID = '" + idx_src + "'")

        connect.commit()
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
        connect.rollback()
        sql_ok = False
    if (sql_ok):
        print("CloneFix success")
    else:
        print("CloneFix failed")

def f_panneaux(connect, data_type, idx_src, idx_dst, option):
    cur = connect.cursor()
    sql_ok = True
    try:
        if ( option == "full" or option == "Meter" ):
            if ( data_type == "watt" ):
                cur.execute("INSERT INTO Meter ( DeviceRowID, Usage, Value, Date ) SELECT " + idx_dst + ", Usage, Value, Date FROM Meter WHERE DeviceRowID = '" + idx_src + "' and date < '2023-02-21'")
            else:
                cur.execute("INSERT INTO Meter ( DeviceRowID, Usage, Value, Date ) SELECT " + idx_dst + ", Usage, Value, Date FROM Meter WHERE DeviceRowID = '" + idx_src + "' and date < '2023-02-21'")
        if ( option == "full" or option == "Calendar" ):
            if ( data_type == "watt" ):
                cur.execute("INSERT INTO MultiMeter_Calendar ( DeviceRowID, Value1, Value2, Value3, Value4, Value5, Value6, Counter1, Counter2, Counter3, Counter4, Date ) SELECT " + idx_dst + ", Value1, Value2, Value3, Value4, Value5, Value6, Counter1, Counter2, Counter3, Counter4, Date FROM MultiMeter_Calendar WHERE DeviceRowID = " + idx_src + " and date < '2023-02-21';")
            else:
                cur.execute("INSERT INTO Meter_Calendar ( DeviceRowID, Value, Counter, Date ) SELECT " + idx_dst + ", Value, Counter/10, Date FROM Meter_Calendar WHERE DeviceRowID = " + idx_src + " and date < '2023-02-21';")
        connect.commit()
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
        connect.rollback()
        sql_ok = False
    if (sql_ok):
        print("Clone success")
    else:
        print("Clone failed")

def f_panneaux_kwh(connect, data_type, idx_src, idx_dst, option):
    cur = connect.cursor()
    sql_ok = True
    try:
        Value   = [i[0] for i in cur.execute("SELECT Value FROM Meter_Calendar WHERE DeviceRowID = '" + idx_src + "' ORDER BY Date ASC")]
        Counter = [i[0] for i in cur.execute("SELECT Counter FROM Meter_Calendar WHERE DeviceRowID = '" + idx_src + "' ORDER BY Date ASC")]
        Date    = [i[0] for i in cur.execute("SELECT Date  FROM Meter_Calendar WHERE DeviceRowID = '" + idx_src + "' ORDER BY Date ASC")]

        index = 0
        cumulatedValue = int("0")
        firstValueNeg = False
        for iUsage in Counter:
            iValue = Value[index]
            iDate = Date[index]


            if ( firstValueNeg ):
                # compute cumulated stuff on our own

                print("ori:" + str(iValue) + "," + str(iUsage) + "," + iDate)
                cumulatedValue += int(iValue)
                print("fix:" + str(iValue) + "," + str(cumulatedValue) + "," + iDate)
                cur.execute("UPDATE Meter_Calendar SET Counter = " + str(cumulatedValue) + " WHERE DeviceRowID = " + idx_dst + " and date = '" + str(iDate) + "'")
            else:
                print("xxx:" + str(iValue) + "," + str(iUsage) + "," + iDate)
                cumulatedValue = int(iUsage)

            if (iUsage == 136230):
                firstValueNeg = True
            index += 1
        connect.commit()
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
        connect.rollback()
        sql_ok = False
    if (sql_ok):
        print("Panneaux kWh success")
    else:
        print("Panneaux kWh failed")

def f_panneaux_auj(connect, data_type, idx_src, idx_dst, option):
    cur = connect.cursor()
    sql_ok = True
    try:
        Value   = [i[0] for i in cur.execute("SELECT Value FROM Meter WHERE DeviceRowID = '" + idx_src + "' ORDER BY Date ASC")]
        Usage = [i[0] for i in cur.execute("SELECT Usage FROM Meter WHERE DeviceRowID = '" + idx_src + "' ORDER BY Date ASC")]
        Date    = [i[0] for i in cur.execute("SELECT Date  FROM Meter WHERE DeviceRowID = '" + idx_src + "' ORDER BY Date ASC")]

        index = 0
        cumulatedValue = int("0")
        firstValueNeg = False
        for iUsage in Usage:
            iValue = Value[index]
            iDate = Date[index]


            if ( firstValueNeg ):
                # compute cumulated stuff on our own

                print("ori:" + str(iValue) + "," + str(iUsage) + "," + iDate)
                cumulatedValue += int( int(iUsage) * (5/60) )
                print("fix:" + str(cumulatedValue) + "," + str(iUsage) + "," + iDate)
                cur.execute("UPDATE Meter SET Value = " + str(cumulatedValue) + " WHERE DeviceRowID = " + idx_dst + " and date = '" + str(iDate) + "'")
            else:
                print("xxx:" + str(iValue) + "," + str(iUsage) + "," + iDate)
                cumulatedValue = int(iValue)

            if (iValue > 0):
                firstValueNeg = True
                cumulatedValue = int(iValue)
            index += 1
        connect.commit()
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
        connect.rollback()
        sql_ok = False
    if (sql_ok):
        print("f_panneaux_auj success")
    else:
        print("f_panneaux_auj failed")


def f_full_clone(connect, data_type, idx_src, idx_dst, option):
    cur = connect.cursor()
    sql_ok = True
    try:
        if ( option == "full" or option == "Meter" ):
            cur.execute("DELETE FROM Meter WHERE DeviceRowID = '" + idx_dst + "'")
            if ( data_type == "watt" ):
                cur.execute("INSERT INTO Meter ( DeviceRowID, Usage, Value, Date ) SELECT " + idx_dst + ", Usage, Value, Date FROM Meter WHERE DeviceRowID = '" + idx_src + "'")
            else:
                cur.execute("INSERT INTO Meter ( DeviceRowID, Usage, Value, Date ) SELECT " + idx_dst + ", Usage, Value/10, Date FROM Meter WHERE DeviceRowID = '" + idx_src + "'")
        if ( option == "full" or option == "Calendar" ):
            if ( data_type == "watt" ):
                cur.execute("DELETE FROM MultiMeter_Calendar WHERE DeviceRowID = '" + idx_dst + "'")
                cur.execute("INSERT INTO MultiMeter_Calendar ( DeviceRowID, Value1, Value2, Value3, Value4, Value5, Value6, Counter1, Counter2, Counter3, Counter4, Date ) SELECT " + idx_dst + ", Value1, Value2, Value3, Value4, Value5, Value6, Counter1, Counter2, Counter3, Counter4, Date FROM MultiMeter_Calendar WHERE DeviceRowID = " + idx_src + ";")
            else:
                cur.execute("DELETE FROM Meter_Calendar WHERE DeviceRowID = '" + idx_dst + "'")
                cur.execute("INSERT INTO Meter_Calendar ( DeviceRowID, Value, Counter, Date ) SELECT " + idx_dst + ", Value, Counter/10, Date FROM Meter_Calendar WHERE DeviceRowID = " + idx_src + ";")
        connect.commit()
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
        connect.rollback()
        sql_ok = False
    if (sql_ok):
        print("Clone success")
    else:
        print("Clone failed")



parser=argparse.ArgumentParser(description='Domoticz DB tool')

parser.add_argument('--db', help='DB full path : kwh, watt', type=str, required=False, default="/home/pi/domoticz/domoticz.db")
parser.add_argument('--type', help='Type : kwh, watt', type=str, required=True)
parser.add_argument('--action', help='Action : clone', type=str, required=True)
parser.add_argument('--option', help='Option : full, Meter, Meter_Calendar', type=str, required=True)
parser.add_argument('--idx_src', help='IDX source : dz device idx', type=str, required=True)
parser.add_argument('--idx_dst', help='IDX target destination : dz device idx', type=str, required=True)
parser.print_help()

args=parser.parse_args()


print("************************************************************************")
print("db[" + args.db + "] type:" + args.type + " action:" + args.action + " src/dst:" + args.idx_src + "/" + args.idx_dst)

connect = sqlite3.connect(args.db)

if (args.action == "clone"):
    f_full_clone(connect,args.type,args.idx_src,args.idx_dst,args.option)
elif (args.action == "fix" ):
    if ( args.type == "eau" ):
        f_eau_fix(connect,args.type,args.idx_src,args.idx_dst,args.option)
elif (args.action == "clonefix" ):
    f_full_clone_fix(connect,args.type,args.idx_src,args.idx_dst,args.option)
elif (args.action == "perdu" ):
    f_perdu(connect,args.type,args.idx_src,args.idx_dst,args.option)
elif (args.action == "export" ):
    if ( args.type == "kwh" ):
        f_export_kwh(connect,args.type,args.option)
elif (args.action == "panneaux" ):
    if ( args.type == "kwh" ):
        f_panneaux_kwh(connect,args.type,args.idx_src,args.idx_dst,args.option)
    else:
        f_panneaux(connect,args.type,args.idx_src,args.idx_dst,args.option)
elif (args.action == "panneaux_auj" ):
    f_panneaux_auj(connect,args.type,args.idx_src,args.idx_dst,args.option)
else:
    c = connect.cursor()

    # Correct overflow values
    c.execute("UPDATE Meter SET Usage = (((Usage/10) - 16777216)*10) WHERE DeviceRowID = 230 AND Usage > 100000")
    connect.commit()

    Value = [i[0] for i in c.execute("SELECT Value FROM Meter WHERE DeviceRowID = 230 ORDER BY Date ASC")]
    Usage = [i[0] for i in c.execute("SELECT Usage FROM Meter WHERE DeviceRowID = 230 ORDER BY Date ASC")]
    BaseValue = 2497359

    tmp = 0
    ValueClear = []

    for i in Usage:
        ValueClear.append(BaseValue + tmp)
        tmp += int(i*(5/600))

    # Printing edited values in a txt file
    r = c.execute("SELECT * FROM Meter WHERE DeviceRowID = 230")

    merged = []
    for i in range(len(Value)):
        merged.append((Value[i], ValueClear[i]))

    with open("tmp.txt", "w+") as f:
        for i in merged:
            txt = f"{i[0]}, {i[1]}\n"
            f.write(txt)

    #print(merged)

print("End of prog")