import matplotlib.pyplot as plt
import numpy as np 

plt.title("Grafuri goale") 
plt.xlabel("numărul de noduri") 
plt.ylabel("timpul(ms)")

data = np.array([
    [0, 0],
    [887, 3.1],
    [1384, 2.5],
])

data2 = np.array([
    [0, 0],
    [887, 1],
    [1384, 1],
])

data3 = np.array([
    [0, 0],
    [887, 4],
    [1384, 5.2],
])

data4 = np.array([
    [0, 0],
    [887, 17],
    [1384, 23.9],
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
plt.savefig('fig1.png')