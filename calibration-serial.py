import serial
from datetime import datetime, timedelta


#serial port of Arduino
#on windows it will be "coma format #on mac it will be "/dev/cu.usbmodemxxx" format
arduino_port = "COM4" #für die drecksschweine
#arduino_port = "/dev/cu.usbmodem142201"
baud = 9600 #arduino uno runs at 9600 baud

ser = serial.Serial(arduino_port, baud)


list_values = []
while True:

    end_time = datetime.now() + timedelta(seconds=5)
    while datetime.now() < end_time:
        getData = str(ser.readline())
        data = getData[-8:][:-5]
        data = data.replace("'", "")
        list_values.append(int(data))

    average = float(sum(list_values) / len(list_values))
    list_values.clear()

