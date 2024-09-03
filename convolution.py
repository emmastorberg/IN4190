"""
def my_convolve(a, b):
    c = []

    for n in range(len(a)):
        c_value = 0

        for k in range(len(a)):
            c_value += a[k]*b[n-k]
        
        c.append(c_value)

    return np.array(c)"""

import numpy as np

tol = 1e-12

def my_convolve(a, b):
    n = len(a) + len(b) - 1
    result = np.zeros(n)
    for i in range(len(a)):
        for j in range(len(b)):
            result[i + j] += a[i] * b[j]
    return result

b = [0, 0, 1, 2, 5]
a = [0.5, 0.5]

assert np.all(np.abs(my_convolve(a,b) - np.convolve(a,b)) < tol), "Convolution results do not match within tolerance"