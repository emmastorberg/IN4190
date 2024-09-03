import h5py
import matplotlib.pyplot as plt

file_path = "2023-05-19t025705.349000.h5"
dataset_name = "waveforms/000_NS.OSL.00.HHZ_2023-05-19T02:52:10_7495.0s"

#a) Plot the full dataset
with h5py.File(file_path, 'r') as f:
    data = f[dataset_name][:]

plt.figure(figsize=(10, 6))
plt.plot(data)
plt.xlabel(r"$n$")
plt.ylabel(r"$x(n)$")
plt.title('Seismic Data 2023-05-19')
plt.show()

#b) Plot 40000 data points in an interesting region
start_index = 60000
end_index = 100000
x_values = range(start_index, end_index)
sliced_data = data[start_index:end_index]

plt.figure(figsize=(10, 6))
plt.plot(x_values, sliced_data)
plt.xlabel(r"$n$")
plt.ylabel(r"$x(n)$")
plt.title(fr"Seismic Data 2023-05-19 (${start_index} \leq n < {end_index}$)")
plt.show()

#c) Plot 40000 data points shifted by an index n_0 = 20000
n0 = 20000
x_values_shifted = range(start_index-n0, end_index-n0)
shifted_and_sliced_data = data[start_index-n0:end_index-n0]

plt.figure(figsize=(10, 6))
plt.plot(x_values_shifted, shifted_and_sliced_data)
plt.xlabel(r"$n$")
plt.ylabel(r"$x(n)$")
plt.title(fr"Seismic Data 2023-05-19 (${start_index-n0} \leq n < {end_index-n0}$)")
plt.show()