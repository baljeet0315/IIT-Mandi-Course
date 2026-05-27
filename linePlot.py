import matplotlib.pyplot as plt
import numpy as np

accuracy = 0.5
acc_list = []
epoch_list = range(1,31)

for epoch in range (1,31):
    accuracy = accuracy + (epoch*0.015)
    acc_list.append(accuracy)

plt.plot(epoch_list, acc_list)
plt.title("Training Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.axhline(0.9, color='red', linestyle='--', label='Target')
plt.grid(True)
plt.show()