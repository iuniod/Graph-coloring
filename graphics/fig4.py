import matplotlib.pyplot as plt
import numpy as np 

plt.title("Arbori binari") 
plt.xlabel("numărul de noduri") 
plt.ylabel("timpul(ms)")

data = np.array([
    [0, 0],
    [10, 8.8],
    [50, 40],
])

data2 = np.array([
    [0, 0],
    [10, 1],
    [50, 1],
    [100, 1.1],
    [500, 1.2],
    [1000, 1.5],
    [2000, 2.2],
])

data3 = np.array([
    [0, 0],
    [10, 1.1],
    [50, 1.8],
    [100, 1.9],
    [500, 4.8],
    [1000, 9.2],
    [2000, 18.3],
])

data4 = np.array([
    [0, 0],
    [10, 6.7],
    [50, 2.8],
    [100, 2.2],
    [500, 6.4],
    [1000, 17.4],
    [2000, 57.1],
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
plt.savefig('fig4.png')