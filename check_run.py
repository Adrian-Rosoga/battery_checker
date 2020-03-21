file_open = open("running.txt","r") #reads if the program is already runnning
num = int(file_open.read())
file_open.close()

file_open = open("running.txt","w")

if num == 0:
    file_open.write("1") #if not running it start running
    file_open.close()

        
else:
    file_open.write("0") #shuts down the program
    file_open.close()

