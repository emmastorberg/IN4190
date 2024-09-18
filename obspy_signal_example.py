# For interactive plotting in Ipython: remember to issue %matplotlib

import numpy as np
import matplotlib.pyplot as plt

import obspy

import scienceplots

plt.style.use('science') # Or you can use RCparams instead to set your plotting defaults


# Read the seismogram
st = obspy.read() # ObsPy default example. From a seismic station in Schwartzwald (Black Forest)


starttime = st[0].meta.starttime
endtime = st[0].meta.endtime
my_len = endtime-starttime
print(starttime)
print(endtime)

print(st[0].meta.starttime)

# There is only one trace in the Stream object, let's work on that trace...
tr = st[0]

# Time axis
t = np.arange(0, tr.stats.npts / tr.stats.sampling_rate, tr.stats.delta)

## Filtering with a lowpass on a copy of the original Trace
tr_filt = tr.copy()
tr_filt.filter('lowpass', freq=0.8, corners=2, zerophase=True)

## Highpass
tr_filt_bp1 = tr.copy()
tr_filt_bp1.filter('highpass', freq=0.8, corners=2, zerophase=True)

## Bandpass
tr_filt_bp2 = tr.copy()
tr_filt_bp2.filter('bandpass', freqmin=1.5, freqmax=5.0, corners=2, zerophase=True)


## --- Plot a spectrogram
fig_spect, axes_spect = plt.subplots(nrows=1, ncols=1,
                           sharex=True, 
                           figsize=(6,3))

st.spectrogram(log=True, title='BW.RJOB ' + str(st[0].stats.starttime), axes=axes_spect, cmap='turbo')
plt.xlim(5, my_len-5)
axes_spect.set_xlabel('Time [s]')
axes_spect.set_ylabel('Frequency [Hz]')
axes_spect.tick_params(axis='both', direction='out', length=3, width=0.7, colors='black', grid_color='w', grid_alpha=0.5, which='major')
axes_spect.tick_params(axis='both', direction='out', length=1, width=0.7, colors='black', grid_color='w', grid_alpha=0.5, which='minor')
cbar = fig_spect.colorbar(axes_spect.collections[-1], ax=axes_spect, label='Rel. power')

plt.tight_layout()



## ---- Plotting the signal traces
fig_traces, axes_traces = plt.subplots(nrows=4, ncols=1,
                           sharex=True, 
                           figsize=(6,5))

fig_traces.suptitle(tr.stats.starttime)

axes_traces[0].autoscale(enable=True, axis='x', tight=True)
axes_traces[0].plot(t, tr.data, 'k')
axes_traces[0].set_ylabel('Raw')

axes_traces[1].plot(t, tr_filt.data, 'k')
axes_traces[1].set_ylabel('Lowpassed')

axes_traces[2].plot(t, tr_filt_bp1.data, 'k')
axes_traces[2].set_ylabel('Highpassed')

axes_traces[3].plot(t, tr_filt_bp2.data, 'k')
axes_traces[3].set_ylabel('Bandpassed')

#fig_traces.tight_layout(rect=[0, 0.03, 1, 0.9])
axes_traces[-1].set_xlabel('Time [s]')
fig_traces.tight_layout()

plt.show()