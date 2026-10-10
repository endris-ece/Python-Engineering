
import numpy as np
from collections import Counter

def mean(signal):
    return np.mean(signal)

def median(signal):
    return np.median(signal)

def mode(signal):

    modes = Counter(signal).most_common()
    result = [modes[0][0]]
    for i in range(len(modes) - 1):
        if modes[0][1] == modes[i+1][1]:
            result.append(modes[i+1][0])
    return result[0] if len(result) == 1 else result

def standard_deviation(signal):
    return np.std(signal)

def variance(signal):
    return np.var(signal)

def minimum(signal):
    return np.min(signal)

def maximum(signal):
    return np.max(signal)

def find_range(signal):
    return np.ptp(signal)

def peak_amplitude(signal):
    return np.max(np.abs(signal))

def peak_to_peak(signal):
    return np.ptp(signal)

def rms(signal):
    return np.sqrt(np.mean(np.square(signal)))

def energy(signal):
    return np.sum(np.square(signal))

def average_power(signal):
    return np.mean(np.square(signal))

def percentile(signal, p):
    return np.percentile(signal, p)









