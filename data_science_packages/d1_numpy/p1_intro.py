# list of same type objects
# so faster than normal list

import numpy as np
import matplotlib.pyplot as plt
a = np.array([1, 2, 3, 4, 5, 6, 7])
b = np.array((34, 54, 6), dtype=float)
print(type(a))
print(type(b))
print(a.dtype)
print(b.dtype)


# dimension -> ndim
a1 = np.array([[1, 2, 3], [43, 43, 54]])
b1 = np.array([[[1, 2, 3], [4, 5, 6]], [[65, 65, 45], [46, 65, 76]]])
c1 = np.array([[23, 43, 544, 54], [3, 45, 6, 65, 76]], dtype=object)
print(a1.ndim)
print(b1.ndim)
print(c1.ndim)

# shape -> shape
a2 = np.array([[[1, 2, 3], [4, 5, 6], [0, 0, -1]], [[-1, -2, -3], [-4, -5, -6], [0, 0, 1]]])
print(a2.shape)
# (2, 3, 3) -> 2=no. of 2d array, 3=no. of 1d array inside each 2d array, 3=no. of elements in each 1d array
print(a2.size)      # total no. of elements in np array
print(a2.nbytes)    # space taken in memory (in bytes)


# numpy important functions
# np.zeros(), np.ones()
# np.arange(), np.reshape()
# np.random.permutation()


a3 = np.arange(20, 100, 2)     # list of numbers from 20 to 99 with a jump of 2
print(a3)

b3 = np.random.permutation(np.arange(10))   # returns random permutation of list of numbers from 0 to 9
print(b3)

print(np.random.randint(23, 100))   # returns a random number btw 23, 99
print(np.random.rand(5))    # list of 5 random numbers
c3 = np.random.rand(1000)
plt.hist(c3, bins=100)
plt.show()
d3 = np.random.randn(1000000)
plt.hist(d3, bins=200, color='orange')
plt.show()

e3 = np.random.rand(2, 3)       # matrix of random numbers of dimension 2*3
print(e3)
print()

a4 = np.arange(50).reshape(5, 10)
print(a4)
