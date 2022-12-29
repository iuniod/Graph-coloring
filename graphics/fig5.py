import matplotlib.pyplot as plt
import numpy as np 

plt.title("Grafuri planare") 
plt.xlabel("numărul de noduri") 
plt.ylabel("timpul(ms)")

data = np.array([
    [0, 0],
    [10, 1.2],
    [50, 100],
])

data2 = np.array([
    [0, 0],
    [10, 1],
    [50, 0.9],
    [100, 1],
    [500, 1.5],
    [1000, 2.2],
    [2000, 3.6],
])

data3 = np.array([
    [0, 0],
    [10, 1.2],
    [50, 1.4],
    [100, 2.2],
    [500, 6.8],
    [1000, 13.1],
    [2000, 27.9],
])

data4 = np.array([
    [0, 0],
    [10, 1.9],
    [50, 2],
    [100, 2.2],
    [500, 6.2],
    [1000, 18.9],
    [2000, 62.6],
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
plt.savefig('fig5.png')