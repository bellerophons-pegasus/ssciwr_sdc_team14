import numpy as np


def get_time_and_update_data(data):
    
    time = data[:, 0]
    new_data = np.delete(data, 0, 1)

    return time, new_data


def get_complex_array(array):

    complex_array = array[:, 0::2] + 1j * array[:, 1::2]

    return complex_array


def get_autocorrelation(array):

    auto_corr_matrix = []
    for i in range(1, len(array)):
        corr = np.multiply(array[0, :], array[i, :])
        auto_corr_matrix.append(np.array(corr))
    auto_correlation = np.sum(auto_corr_matrix, axis=1)

    return auto_correlation


def get_power_spectrum(fourier):

    return abs(fourier)**2