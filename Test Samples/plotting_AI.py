import matplotlib.pyplot as plt
import numpy as np
import random

#a = np.random.random((10, 1))
a = np.linspace(0, 100, 50)
b = np.power(a, 0.5)
print(a)
print(b)
plt.plot(a, b, '+-')
plt.show()