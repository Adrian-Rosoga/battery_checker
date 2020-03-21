file_open = open("running.txt","r") #reads if the program is already runnning
num = int(file_open.read())
file_open.close()

file_open = open("running.txt","w")
import check_bat as bat

if num == 0:
    file_open.write("1") #if not running it start running
    bat.check_bat()


else:
    file_open.write("0") #shuts down the program
    bat.stop_check()