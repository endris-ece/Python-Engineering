
import numpy as np

rng = np.random.default_rng()

def signal_addition(signal1, signal2):
    return np.add(signal1, signal2)

def add_noise(noise_level, signal):
    return signal + noise_level*rng.standard_normal(signal.shape)

def scaling(scaling_factor, signal):

    return scaling_factor * signal

def amplitude_shifting(shifting_factor, signal):

    return signal + shifting_factor

def reversing(signal):

    return np.flip(signal)


