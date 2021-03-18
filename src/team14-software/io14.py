# I/O module for team14-software

import pandas as pd
import numpy as np

def readfile(filepath, mode, separator='\t', datatype=float, skiprows=1):
    """Reads a given (csv) file with the indicated separator.

    Arguments:
        filepath: path to the file including the filename
        mode:  indicates if data should be read into a dataframe ('df') or into a NumPy array ('npy')
        separator: optional, separator used in the file (e.g. '\t'), can also be a regular expression like '    |   |  '
        datatype: optional,
        skiprows: optional
    """
    if mode == 'df':
        data = pd.read_table(filepath, separator, engine='python')
    if mode == 'npa':
        data = np.loadtxt(filepath,datatype,skiprows)
    return data
