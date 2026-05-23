import matplotlib.pyplot as plt
import numpy as np

m = 3
c = 2

x = np.linspace(0,10,100)
y = m*x + c

print(y)

plt.title("y=mx+c")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x,y)
plt.grid(True)
plt.show()

