import serial

#serial port of Arduino
#on windows it will be "coma format #on mac it will be "/dev/cu.usbmodemxxx" format
arduino_port = "COM4" #für die drecksschweine
#arduino_port = "/dev/cu.usbmodem142201"
baud = 9600 #arduino uno runs at 9600 baud
samples = 10 #how many samples do you want to collect?

ser = serial.Serial(arduino_port, baud)
print((" Connected to Arduino port: " + arduino_port + " ").center(80, '#'))


list_values = []
while True:
# incoming = ser. read (9999)
# if len(incoming) > 0:

    ser_bytes = ser.readline()
    data = float(ser_bytes[0:len(ser_bytes) - 2].decode("utf-8"))

    if len(list_values) < 5:
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


