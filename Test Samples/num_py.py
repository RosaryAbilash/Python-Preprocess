import numpy as np
import random

from numpy.core.shape_base import hstack

a = np.array([[1, 2, 3, 4], [23, 24, 25, 26]])
b = np.array([[11, 12, 13, 14], [13, 14, 15, 16]])
#print(a)
#print(a.shape)
#print(type(a))
#print(a[1, 3])
#b =np.random.randint((4, 4))
#c = np.random.randint((4, 4))
#print(type(c))
axis_0 = np.concatenate((a, b), axis=0)
axis_1 = np.concatenate((a, b), axis=1)
print(axis_0)
print(axis_1)
h_stack = np.hstack((a, b))
v_stack = np.vstack((a, b))
print(v_stack)
print(h_stack)
#f = np.reshape(a, (3, 0))
#print(f)
# np.ravel(a)
#a.flatten()
print(a.flatten())