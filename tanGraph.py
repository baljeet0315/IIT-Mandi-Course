import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.tan(x)

plt.plot(x,y)
plt.title("Tan Graph")
plt.xlabel("X")
plt.xlabel("Y")
plt.grid(True)
plt.show()