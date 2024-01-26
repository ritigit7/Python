import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array((1, 2, 3, 4))
print(a)
print(type(b))
print(np.__version__)  # check version of numpy

c1 = np.array(23)  # 0 dimention array
c2 = np.array([1, 2, 3])  # 1-D array
c3 = np.array([[1, 2, 3], [4, 5, 6]])  # 2-D array
c4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [0, 1, 2]]])  # 3-D array
# ndmin is used for making array array by given number
c5 = np.array([1, 2, 3], ndmin=5)

print(c5)
print(c5.ndim)  # ndim is used for checking array dimention
print(c3[0][0])
print(c3[0, 2])

d1 = np.array([1, 2, 3, 4])
d2 = np.array([5,6,7],dtype='O')
d3 = d1.astype('S')
print(d1.dtype,d2.dtype,d3.dtype)