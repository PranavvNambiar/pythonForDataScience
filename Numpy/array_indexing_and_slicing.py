import numpy as np

arr1 = np.array(
    [
        [[11, 12, 13, 14], [13, 14, 15, 19]],
        [[15, 16, 17, 21], [63, 92, 36, 18]],
        [[98, 32, 81, 23], [17, 18, 19.5, 43]],
    ]
)

print(arr1.shape)

print(arr1[1])
print(arr1[1, 1])
print(arr1[0, 0, 0])
print(arr1[1, 1, 2])
# In the 1st dimension
print(arr1[1:])
# Inside the second dimension, only keep the 1st array of number, the rest will not be printed
# This is for all the arrays inside the 2nd dimension
print(arr1[1:, 0:1])
# Will only  print all the numbers till index  2 but not including 2
print(arr1[1:, 0:1, :2])

# Null matrices can be created by so:
# In the parenthese we give the shape of the matrix we want to create.
print(np.zeros((3, 2)))

# To print a matrix with all elements as 1(unit matrix), we do:
print(np.ones([3, 2]))
print(np.ones([0, 2, 3]), end="\n\n")
print(np.ones([1, 2, 3]), end="\n\n")
print(np.ones([2, 2, 3]), end="\n\n")
print(np.ones([3, 2, 3]), end="\n\n")

# An identity matrix is created as so:
print(np.eye(3))

print(np.random.randint(0, 100))
print(np.random.randint(100))

# Random Vector
print(np.random.rand(5))

# Random Matrix
# *We need to pass the shape as the arguement, a tuple will cause an error
print(np.random.randn(2, 3))

#!Difference between rand & randn
# * Rand picks uniformly any values from 0 to 1 but randn picks the numbers from a gaussian distribution
# *Generally the values in randn are from (-2,2), its values are mostly revolving around 0
# *Mean of 0 and standard deviation of 1

# Matrix with a fixed Value
print(np.full([2, 4], 69))

# Range with a start, end and increments from the start till the end is reached
print(np.arange(10, 90, 3))
print(np.arange(10, 90, 3).shape)
print(np.arange(10, 90, 3).sum())

# Now we can also reshape these range of values by using a reshape command and passing the required shape in the parentheses.
print(np.arange(10, 90, 3).shape)
print(np.arange(10, 90, 3).reshape(3, 3, 3))
print(np.arange(10, 90, 3).reshape(3, 9))
print(np.arange(10, 90, 3).reshape(1, 27))
#!To reshape the array the reshape size should be divisible by the shape
# For e.g: is shape is (27,)
# Then the reshape can be (3,3,3) or (9,3),(3,9)
# NOT (3,4)

# While reshaping we can leave out one of the indices, numpy will calculate the reshape value from the fixed value
print(np.arange(10, 90, 3).reshape(3, 3, -1))

# In this unlike arange in which we provide the increments to reach the end, in linspace, we provide the number of steps to reach the end
# For eg: from 3 to 27, it will give us 9 equally spaced steps from 3 to 27
print(np.linspace(3, 27, 9))
