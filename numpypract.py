### What is numpy?

# NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more
# At the core of the NumPy package, is the ndarray object. This encapsulates n-dimensional arrays of homogeneous data types




import numpy as np

a = np.array([1,2,3])
d = np.array([12,3,4])
b = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a)
print(b)

print(np.arange(1,11))
print(np.arange(1,11).reshape(5,2))
print(np.ones((3,4)))
print(np.zeros((3,4)))
print(np.random.random((3,4)))


print(np.linspace(1,11,9)) #equal space between the given range

print(a.ndim)#dimension of array
print(b.shape)#rows and colmns
print(a.size)#total elements in the array
print(a.itemsize)#how much space it occupies (items)
print(a.dtype)#dtype of array

c=a.astype(np.int32)
print(c.dtype)


#scalar op
print(2*a)

#vect op
print (a*d)

print(np.max(a))
print(np.sum(a))
print(np.prod(a))


print(np.max(b,axis=1)) #1  -> row 0 -> column

m1= np.arange(10).reshape(2,5)
m2= np.arange(10).reshape(5,2)

print(np.dot(m1,m2))


#to print each element of nD ARRAY:
for i in np.nditer(b):
    print(i)


#TRANSPOSE
print(b.T)

#RAVEL- CONVERT ND IN 1D
print(b.ravel())


arr = np.random.randint(1,100,24).reshape(6,4)
print(arr)
print(arr[arr>50])


# Broadcasting
# The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations.

# The smaller array is “broadcast” across the larger array so that they have compatible shapes.ts so goated actually