#will add final code  here

import check_run
import subprocess

file_open = open("running.txt","r") #reads if the program is already runnning
num = int(file_open.read())
file_open.close()


if num == 1:
    p = subprocess.Popen(['python', 'check_bat.py'])
    close = input("")

else:
    try:
        p.terminate
    except:
        pass