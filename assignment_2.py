# 5 Important Numpy Functions
import numpy
from numpy.polynomial import Polynomial as Poly

# 1st Function
# Create a polynomial from coefficients
b = Poly([4, 2, 1])  # 4 + 2x + x^2
print(b)
"""
We notice that this polynomial is in reverse order
To convert this in to normal ordering, we need to use the legacy polynomial API.
"""
print(numpy.poly1d(b.coef[::1]))

# Converting the normal ordering of the legacy to the reverse ordering
a = numpy.poly1d([1, 2, 2])
a1 = Poly(a.coef[::1])
print(a)
print(a1)

# 2nd Function
# Creates a polynomial objectt from roots
print(Poly.fromroots([-1, 3]))

# 3rd Function
# print(Poly.fit(x, y, deg=))
