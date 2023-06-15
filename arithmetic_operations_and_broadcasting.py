import numpy as np

arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3]])
arr3 = np.array([[11, 12, 13, 14], [15, 16, 17, 18], [19, 11, 12, 13]])

# Elementwise Operations, they need to be the same shape to perform addition of 2 arrays
print(arr2 + arr3)

# Adding a scalar
print(arr2 + 3)

# Elementwise Subtraction
print(arr3 - arr2)

# Division by Scalar
print(arr2 / 2)

# Elementwise Multiplication
print(arr2 * arr3)

# Modulus with scalar
print(arr2 % 4)

"""
! Broadcasting
Numpy arrays also support broadcasting, which allows arithmetic operations between two arrays having a different number of dimensions, but compatible shapes.
"""
arr4 = np.array([4, 5, 6, 7])
print(arr4.shape)

# This operation is legal in numpy
# In this the array with the lesser number of lists
# gets replicated to match the the other rows or columns with the existing list
# In this arr4 will become ([4,5,6,7],[4,5,6,7],[4,5,6,7]) and be added with arr2
# * Broadcasting only works if one of the arrays can be replicated to EXACTLY match the shape of the other array.
print(arr2 + arr4)

"""
arr5 = np.array([7,8])
This array cannot be broadcasted as the shape of arr2 cannnot be matched with the current shape of arr5
arr5_replicated = np.array([7,8],[7,8],[7,8])-->Does not match the shape of arr2

print(arr2+arr5)
print(arr2+arr5_replicated)
These funtions will not work and wil show an error(ValueError)
"""

arr6 = np.array([[1, 2, 3], [3, 4, 5]])
arr7 = np.array([[1, 2, 3], [1, 2, 5]])

print(arr6 == arr7)
# Will compare each element in each array with each other and will show True or False if they are similar or not

print(arr6 != arr7)

print(arr6 >= arr7)

print(arr6 <= arr7)

print(arr6 > arr7)

print(arr6 < arr7)

# All these will give an 'array' of booleans, not 'booleans'

print((arr6 == arr7).sum())
# Will give a sum of all the elements that are equal in the array
