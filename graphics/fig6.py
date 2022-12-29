import matplotlib.pyplot as plt
import numpy as np 

plt.title("Grafuri cu număr de muchii fix") 
plt.xlabel("numărul de muchii") 
plt.ylabel("timpul(ms)")

data = np.array([
    [0, 0],
    [10, 25.6],
    [100, 112.5],
    [500, 8000],
])

data2 = np.array([
    [0, 0],
    [10, 1],
    [100, 1],
    [500, 1.3],
    [1000, 1.6],
    [10000, 6.7],
    [100000, 65.2],
    [500000, 455.6],
    [1000000, 925.4],
])

data3 = np.array([
    [0, 0],
    [10, 5.5],
    [100, 4.2],
    [500, 5.6],
    [1000, 8.6],
    [10000, 59.2],
    [100000, 498.3],
    [500000, 2387.9],
    [1000000, 4978.7],
])

data4 = np.array([
    [0, 0],
    [10, 27.8],
    [100, 12.5],
    [500, 10.5],
    [1000, 14.2],
    [10000, 56.4],
    [100000, 214.1],
    [500000, 619.7],
    [1000000, 1343.8],
])

x, y = data.T
plt.plot(x, y, label='Brute Force')

x, y = data2.T
plt.plot(x, y, label='Greedy')

x, y = data3.T
plt.plot(x, y, label='DSatur')

x, y = data4.T
plt.plot(x, y, label='RLF')

plt.legend()


# Save the figure as a png file
plt.savefig('fig6.png')