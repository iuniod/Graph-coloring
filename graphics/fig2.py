import matplotlib.pyplot as plt
import numpy as np 

plt.title("Grafuri complete") 
plt.xlabel("numărul de noduri") 
plt.ylabel("timpul(ms)")

data = np.array([
    [0, 0],
    [10, 41215.1],
])

data2 = np.array([
    [0, 0],
    [10, 0.9],
    [50, 1.6],
    [100, 3.4],
    [500, 83.1],
    [1000, 443.5],
    [2000, 1968.1],
])

data3 = np.array([
    [0, 0],
    [10, 1.1],
    [50, 4.9],
    [100, 18.5],
    [500, 602.6],
    [1000, 2639.5],
    [2000, 12453.2],
])

data4 = np.array([
    [0, 0],
    [10, 1.6],
    [50, 2.5],
    [100, 4.4],
    [500, 263.7],
    [1000, 1338.8],
    [2000, 8119.9],
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
plt.savefig('fig2.png')