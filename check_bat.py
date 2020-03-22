
def work():
    import psutil
    import time
    import play_sound

    temp = 0
    while temp == 0:
        time.sleep(60)
        battery = psutil.sensors_battery()
        print(battery)

        remaining = battery.precent
        plugged = battery.power_plugged

        played = 0

        if remaining <= 20 and plugged == False and played == 0:
            play_sound.play_bat_low()
            played = 1

        elif played == 1:
            time.sleep(300)
            played = 0

        else:
            pass

work()
