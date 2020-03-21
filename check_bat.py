import psutil

battery = psutil.sensors_battery()
print(battery)

remaining = battery.precent
plugged = battery.power_plugged

if remaining <=20 and plugged == False:
    print ("test")