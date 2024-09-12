"""
def my_convolve(a, b):
    c = []

    for n in range(len(a)):
        c_value = 0

        for k in range(len(a)):
            c_value += a[k]*b[n-k]
        
        c.append(c_value)

    return np.array(c)

import numpy as np

tol = 1e-12

def my_convolve(a, b):
    n = len(a) + len(b) - 1
    result = np.zeros(n)
    for i in range(len(a)):
        for j in range(len(b)):
            result[i + j] += a[i] * b[j]
    return result"""

import numpy as np

tol = 1e-12

def my_convolve(a, b):
    # Padding size is half the kernel length (assuming the kernel length is odd, if even we can use different padding logic)
    pad_size = len(b) // 2
    
    # Pad the signal with zeros
    padded_a = np.pad(a, (pad_size, pad_size), 'constant', constant_values=(0, 0))
    
    # Prepare an output array for the result of the convolution
    y = np.zeros(len(a))
    
    # Perform the convolution using the sliding window approach
    for i in range(len(a)):
        # Extract the segment of the padded signal
        segment = padded_a[i:i + len(b)]
        
        # Perform element-wise multiplication and sum the result
        y[i] = np.sum(segment * b)
        
    return y

b = [0, 0, 1, 2, 5]
a = [0.5, 0.5]

assert np.all(np.abs(my_convolve(a,b) - np.convolve(a,b)) < tol), "Convolution results do not match within tolerance"