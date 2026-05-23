import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 20)
x = 20
learning_rate = 0.2
for i in range(20):
    grad = 2*x
    x -= learning_rate * grad
    print(f"Iteration {i+1} Value of x: {x}")

    plt.plot(x, grad, 'ro')
    plt.title(f"Iteration {i+1}")
    plt.xlabel('x')
    plt.ylabel('Gradient')
    plt.xlim(0, 10)
    plt.ylim(0, 20)
    plt.grid(True)
    plt.pause(0.1)
plt.show()