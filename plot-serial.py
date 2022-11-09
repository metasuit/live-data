import time
import serial
from datetime import datetime, timedelta
import math
import matplotlib.pyplot as plt
import numpy as np
import csv

def read_serial(log_time, sampling_time):
    ser.flushInput()
    end_time = datetime.now() + timedelta(seconds=log_time)
    t = 0
    while datetime.now() < end_time:
        ser_bytes = ser.readline()
        if ser_bytes[0:len(ser_bytes) - 2].decode("utf-8") != '':
            decoded_bytes = float(ser_bytes[0:len(ser_bytes) - 2].decode("utf-8"))
            print(decoded_bytes)
            V.append(decoded_bytes)
            T.append(t*sampling_time)
            t = t + 1


    average = float(sum(V) / len(V))
    print("Average:", average, "Length: ", len(V))
    return average

def plot_serial(log_time, sampling_time):
    print(V)
    plt.title('Voltage of HASEL Sensor')
    plt.xlabel('Time [ms]')
    plt.ylabel('Voltage [V]')
    plt.plot(T, V, color='blue', linewidth=1, label='Noisy Data')
    plt.legend()
    plt.xlim([0, 1000])
    plt.show()



arduino_port = "COM4" #für die drecksschweine
#arduino_port = "/dev/cu.usbmodem142201"
baud = 9600 #arduino uno runs at 9600 baud
ser = serial.Serial(arduino_port, baud)
V = []
T = []
log_time = 10 #s
sampling_time = 0.1 #ms


read_serial(log_time, sampling_time)
plot_serial(log_time, sampling_time)