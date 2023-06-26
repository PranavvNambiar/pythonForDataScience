import numpy as np

climate_data = np.array(
    [[73, 67, 43], [91, 88, 64], [87, 134, 58], [102, 43, 37], [69, 96, 70]]
)

print(climate_data)
print(climate_data.shape)

w1, w2, w3 = 0.3, 0.2, 0.5
weights = np.array([w1, w2, w3])

print(weights)
print(weights.shape)

arr3 = np.array([[[11, 12, 13], [13, 14, 15]], [[15, 16, 17], [17, 18, 19]]])
print(arr3.shape)
print(arr3)

print(arr3.dtype)
print(weights.dtype)
# *If an array contains even a single floating point number, all the rest are also converted to a floating point number

x = np.matmul(climate_data, weights)
print(x)
# This can also be done to do matrix multiplication '@'
print(climate_data @ weights)
