import numpy as np

w1, w2, w3 = 0.3, 0.2, 0.5
kanto = np.array([73, 67, 43])
weights = np.array([w1, w2, w3])
print(kanto)
# This no longer an 'array', this is a numpy array
print(type(kanto))

# Performs a dot operation of the 2 arrays like in linear algebra
print(np.dot(kanto, weights))
# np.cross(kanto,weights)

# Can also be done by:
print(kanto * weights)
print((kanto * weights).sum())
