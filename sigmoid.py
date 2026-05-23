import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,100)
y = 1/(1+np.exp(-x))

plt.plot(x,y)
plt.title("Sigmoid Function")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()