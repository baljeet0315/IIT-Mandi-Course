import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,100)
y = np.maximum(0,x)

plt.plot(x,y)
plt.grid(True)
plt.show()