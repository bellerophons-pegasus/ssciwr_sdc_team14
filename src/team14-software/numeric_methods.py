import numpy as np


def get_time_and_update_data(data):
    """"Outputs a time column vector and the updated data array without time column

    :param data: Input data array that contains time column with corresponding data for each time step
    :return: 1D time array with the corresponding 2D updated data array
    """

    time = data[:, 0]
    new_data = np.delete(data, 0, 1)

    return time, new_data


def get_complex_array(array):
    """Outputs a complex array from the input array.

    :param array: array that has real parts in columns 0, 2, 4,... and imaginary part in columns 1, 3, 5,...
    :return: An array with complex data type
    """

    complex_array = array[:, 0::2] + 1j * array[:, 1::2]

    return complex_array


def get_autocorrelation(array):
    """ Calculates the auto-correlation function for a given array

    :param array: a 2D array
    :return: auto-correlation vector
    """

    auto_corr_matrix = []
    for i in range(1, len(array)):
        corr = np.multiply(array[0, :], array[i, :])
        auto_corr_matrix.append(np.array(corr))
    auto_correlation = np.sum(auto_corr_matrix, axis=1)

    return auto_correlation


def get_power_spectrum(array):
    """" Calculates DFT and power spectrum from the given array.

    :param array: a 2D array
    :return: DFT array and the power spectrum
    """

    fourier = np.fft.fft(array)
    power = abs(fourier)**2

    return fourier, power