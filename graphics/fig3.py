import matplotlib.pyplot as plt
import numpy as np 

plt.title("Grafuri bipartite complete") 
plt.xlabel("numărul de noduri") 
plt.ylabel("timpul(ms)")

data = np.array([
    [0, 0],
    [10, 1.1],
    [50, 3.2],
    [100, 10.1],
    [500, 334.6],
    [1000, 2224.6],
    [2000, 14255.2],
])

data2 = np.array([
    [0, 0],
    [10, 1],
    [50, 1.2],
    [100, 2.2],
    [500, 19.8],
    [1000, 111],
    [2000, 519.3],
])

data3 = np.array([
    [0, 0],
    [10, 2.4],
    [50, 3.3],
    [100, 8.2],
    [500, 183.7],
    [1000, 854.9],
    [2000, 3223.1],
])

data4 = np.array([
    [0, 0],
    [10, 2.4],
    [50, 2.6],
    [100, 2.5],
    [500, 18.4],
    [1000, 75.6],
    [2000, 336.1],
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
plt.savefig('fig3.png')