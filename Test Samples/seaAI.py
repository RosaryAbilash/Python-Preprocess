import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0, 100, 50)
b = np.power(a, 0.5)
print(a)
print(b)

sns.set()
sns.lineplot(a, b)
plt.show()