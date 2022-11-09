import serial
import csv

#serial port of Arduino
#on windows it will be "coma format #on mac it will be "/dev/cu.usbmodemxxx" format
arduino_port = "COM4" #für die drecksschweine
#arduino_port = "/dev/cu.usbmodem142201"
baud = 9600 #arduino uno runs at 9600 baud
fileName="analog-data.csv" #name of the CSV file generated
samples = 10 #how many samples do you want to collect?

ser = serial. Serial(arduino_port, baud)
print ("Connected to Arduino port:" + arduino_port)
file = open(fileName, "a")
print ("Created file")

list_values = []
while True:
# incoming = ser. read (9999)
# if len(incoming) > 0:

   getData=str(ser.readline( ))
   print(getData)
   data = getData[-8:][:-5]
   data = data.replace("'", "")
   print(data)

   if len(list_values) < 50:
       list_values.append(data)
       continue

   list_values.pop(0)
   list_values.append(data)


   #file1 = open("analog-data.txt","a")
   #L = [1, 2, 3]
   #file1.writelines(data)

   # with is like your try .. finally block in this case
   with open('analog-data.txt', 'r') as file:
       # read a list of lines into data2
       data2 = file.readlines()

   # now change the 2nd line, note that you have to add a newline
   data2[0] = str(list_values)

   # and write everything back
   with open('analog-data.txt', 'w') as file:
       file.writelines(data2)



