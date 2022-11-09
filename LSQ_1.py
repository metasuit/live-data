from itertools import count
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import special
from matplotlib.animation import FuncAnimation

# We want to fit data linearly for y = a*sin(wt + z)
# w = known
# Rewrite as: y = a*cos(z)*sin(wt) + a*sin(z)*cos(wt) := w_1*phi_1(t) + w_2*phi_2(t)
# Solve for weights and calculate a, z

# Read and store data
data = pd.read_csv('Trace 21-07-36 0.csv')
#data = pd.read_csv('data/Trace_1_174.csv')
#data = pd.read_csv('data/Trace_1_78.csv')
#data = pd.read_csv('data/Trace_1_43.csv')
#data = pd.read_csv('data/Trace_1_22.csv')
#data = pd.read_csv('data/Trace_1_12.csv')
T = data['Time (s)'].tolist()
V = data['1 (VOLT)'].tolist()
freq = 1000 # Hz [1/s] from AC generator

# Defining parameters
a = 0
z = 0
N = len(T)
M = 2
omega = 2*math.pi*freq

# Setting up matrices
A = np.zeros([N, M])
y = np.zeros([N, 1])
for i in range(0, N):
    A[i, 0] = np.sin(omega*T[i])
    A[i, 1] = np.cos(omega*T[i])
    y[i, 0] = V[i]

# Solve LSQ
w = np.linalg.lstsq(A, y, rcond=None)[0]
a = np.linalg.norm(w)
z = math.atan(w[1]/w[0])

# Generate noise free data
V_LSQ = [0]*len(T)
for i in range(0, len(T)):
    V_LSQ[i] = a*math.sin(omega*T[i]+z)

# Visualize data
plt.title('Voltage of HASEL Sensor')
plt.xlabel('Time [s]')
plt.ylabel('Voltage [V]')
plt.plot(T, V, color='gray', linewidth=1, label='Noisy Data')
plt.plot(T, V_LSQ, color='blue', linewidth=2, alpha=1, label='LSQ fit: ' + str(round(a, 5)) + '*sin(2*pi*' + str(freq) + '*t + ' + str(round(z, 5)) + ')')
plt.legend()
plt.show()

# Gaussian Check
E = [0]*len(T)
for i in range(0, len(T)):
    E[i] = V_LSQ[i] - V[i]
plt.title('Error')
plt.xlabel('Time [s]')
plt.ylabel('Error [V]')
plt.plot(T, E, color='gray', linewidth=1, label='Error')
plt.show()

X = []
P = []
e = -0.02
count_old = 0
count = 0
while e < 0.02:
    count = 0
    for i in range(0, len(E)):
        if E[i] < e:
            count = count+1
    X.append(e)
    P.append(count)
    e = e + 0.0001

plt.title('Cumulative Error Distribution')
plt.title('Cumulative Error Distribution')
plt.xlabel('Error [V]')
plt.ylabel('Number of Samples')
plt.plot(X, P, color='blue', linewidth=1, label='Error')
plt.show()
print(X)





