import h5py
import scipy.io
import numpy as np
import matplotlib.pyplot as plt

file_path = "am.ra461_unfilt.h5"
dataset_name = "waveforms/000_AM.RA461.00.HDF_2022-01-15T04:00:00_72000.0s"
filter_file_path = "window.mat"

#a)
with h5py.File(file_path, "r") as f:
    data = f[dataset_name][:]

# c)
mat_data = scipy.io.loadmat(filter_file_path)
filter_sequence_name = "my_window"
filter_sequence = mat_data[filter_sequence_name].squeeze()

# e)
convolved_data = np.convolve(data, filter_sequence, mode='same')

# b), d) and f) (plotting)
plt.figure(figsize=(12, 9))

plt.subplot(3, 1, 1)
plt.plot(data)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Raw Data")

plt.subplot(3, 1, 2)
plt.plot(filter_sequence)
plt.title("Filter Sequence")

plt.subplot(3, 1, 3)
plt.plot(convolved_data)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Convolved Data")

plt.tight_layout()
plt.show()

"""
g)
This looks like a high-pass filter. In particular it looks like it 
removed one major low-frequency event right before 1 second.

h)
In the filtered signal we now see that something big occured right before 
3 seconds in, so I would assume that's when the sound wave arrived.
"""



