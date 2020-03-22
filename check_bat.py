
import psutil
import time
import play_sound


def work():
    
    while True:
        
        battery = psutil.sensors_battery()
        print("Battery:", battery)

        remaining = battery.percent
        plugged = battery.power_plugged

        if remaining < 20 and not plugged:
            play_sound.play('Battery_Alert.wav', 3)

        time.sleep(60)
        

work()
