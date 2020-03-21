file_open = open("running.txt","r") #reads if the program is already runnning
num = int(file_open.read())
file_open.close()

file_open = open("running.txt","w")
from check_bat import check_batt, stop_check

if num == 0:
    file_open.write("1") #if not running it start running
    check_batt()


else:
    file_open.write("0") #shuts down the program
    stop_check()