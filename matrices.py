import numpy as np

x = np.array([
    [1, 2],
    [3, 4]
    ])

y = np.array([
    [2, 1],
    [4, 3]
])
print(x)
print(y)

A = x+y
B = np.dot(x,y)
C = x@y

print(A)
print(B)
print(C)