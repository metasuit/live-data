from itertools import count
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import special
from matplotlib.animation import FuncAnimation

# We want to fit data linearly for y = b + a*sin(wt + z) for each period
# w = known
# Rewrite as: y = b + a*cos(z)*sin(wt) + a*sin(z)*cos(wt) := w_0 + w_1*phi_1(t) + w_2*phi_2(t)
# Solve for weights and calculate a, z

# Read and store data
data = pd.read_csv('data/EDU-X 1002A Trace Data Log 2022-10-27 18-05-49 1.csv')
T = data['Time (s)'].tolist()
V = data['1 (VOLT)'].tolist()
freq = 1000 # Hz [1/s] from AC generator

# Defining parameters
a = 0
z = 0
M = 3
interval_size = 150 # Amount of samples per sub-interval (the higher, the larger the sub-interval)
A_list = [] # This is the list which will contain all the amplitudes in each sub-interval
Z_list = []
V_LSQ = [0]*len(T)
omega = 2*math.pi*freq

print(int(len(T)/interval_size) + 1)
# Setting up matrices
print(int(len(T)/interval_size))
for interval in range(0, int(len(T)/interval_size) + 1):
    A = np.zeros([interval_size, M])
    y = np.zeros([interval_size, 1])
    for i in range(interval_size*interval, min(interval_size*interval + interval_size, len(T))):
        A[i - interval_size * interval, 0] = 1
        A[i - interval_size*interval, 1] = np.sin(omega*T[i])
        A[i - interval_size*interval, 2] = np.cos(omega*T[i])
        y[i - interval_size*interval, 0] = V[i]


    # Solve LSQ
    w = np.linalg.lstsq(A, y, rcond=None)[0]
    a = math.sqrt(w[1]**2 + w[2]**2)
    z = math.atan(w[2]/w[1])
    b = w[0]

    print(w)

    for i in range(interval_size*interval, min(interval_size*interval + interval_size, len(T))):
        A_list.append(a + b)
        Z_list.append(z)
        V_LSQ[i] = (a * math.sin(omega * T[i] + z) + b)


# Generate noise free data
#V_LSQ = [0]*len(T)
#for i in range(0, len(T)):
   # V_LSQ[i] = a*math.sin(omega*T[i]+z)

# Visualize data
plt.title('Voltage of HASEL Sensor')
plt.xlabel('Time [s]')
plt.ylabel('Voltage [V]')
plt.plot(T, V, color='gray', linewidth=1, label='Noisy Data')
ZERO = [0]*len(T)
plt.plot(T, ZERO, color='black', linewidth=1, label='Zero Line')
plt.plot(T, V_LSQ, color='blue', linewidth=2, alpha = 0.7, label='Sine Approx of Sub-Interval')
plt.plot(T, A_list, color='green', linewidth=2, label='Voltage of corresponding Sub-Interval')

plt.legend()
plt.show()





