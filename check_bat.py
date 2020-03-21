def check_bat():
    import psutil
    import time
    import play_sound

    temp = 0
    
    while temp == 0: #every minute it checks the battery
        
        time.sleep(60)
        battery = psutil.sensors_battery()
        print(battery)

        remaining = battery.precent
        plugged = battery.power_plugged

        if remaining <=20 and plugged == False:
            play_sound.play_bat_low()

def stop_check():
    temp = 1