# NumPy
import numpy as np

#Convert an array of elements to Float
a = np.array([1,4,5,8],float)
print(a)
type(a)

# array manipulations -- overriding a value
a[:2]
a[0]=3.
print(a)

# multidimensional & Slicing
a = np.array([[1,2,3],[4,5,6]], float)
print(a)
print(a.shape)
print(a[0,1:])
print(a[0:,2:])

# shape to define array elements & dimension

print(a.shape)
print(a.dtype)

# len of an array -- number of Rows

print(len(a))

# Reshaping the arrays -- single to multi-dimensional

b = np.array(range(10), int)
print(b)
b = b.reshape((5,2))
print(b)

# Name Binding

c = b
d = b.copy()
b[0] = 10
print(b)
print(c)
print(d)

# flatten the array (multi -to single) & Transpose

print(c.flatten())
print(c.transpose())

# ToString & From String -- check the alogrithm for String conversion

s=a.tostring()
print(s)
t=np.fromstring(s)
print(t)

# Concatenating Arrays -- 3 Dimensional

a = np.array([[1, 2, 3], [4, 5, 6], [1, 2, 3]], int)
b = np.array([[7, 8, 9], [10, 11, 12], [1, 2, 3]], int)

c1 = np.concatenate((a,b), axis=0)
c2 = np.concatenate((a,b), axis=1)

print(c1)
print(c2)

# New Axis Creation -- create axis 

print(a.shape)
print(a[:,np.newaxis].shape)

# More ways to create Arrays

print(np.ones((2,3), dtype=int))
print(np.zeros_like(a))

print(np.identity(3, dtype=int))
print(np.eye(3, k=1, dtype=int))

# Array Math & Stats

    # Addition, Substraction & Multiplication

print(a+b)
print(b-a)
print(a*b)
print(a.sum())
print(a.prod())

    # Min, Max, Mean, Variance & Standard Deviation

print(a.min())
print(a.max())
print(a.mean())
print(a.var())
print(a.std())
    
# For Loop

for (x, y, z) in a:
    print(x+y+z)
    print(a.argmin())
    print(a.argmax())
