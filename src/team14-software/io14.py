#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
# io14.py
# docstring with sphinx and napoleon

"""
Input and output for team14-software.

Function readfile reads files.
Function writefile writes given data to file.
"""


import pandas as pd
import numpy as np


def readfile(filepath, mode, separator='\t', datatype=float, skiprows=1):
    """Read a given (csv) file with the indicated separator.

    Args:
        filepath (str): path to the file including the filename
        mode (str): indicates if data should be read into a Pandas\
                    dataframe ('df') or into a NumPy array ('npa')
        separator (str): optional, separator used in the file\
                         (e.g. '\t'), can also be a\
                         regular expression like '    |   |  '
        datatype (type): optional,
        skiprows (int): optional

    Returns:
        dataframe, array: A structured data object, either \
                          Pandas dataframe or NumPy array
    """
    if mode == 'df':
        data = pd.read_table(filepath, separator, engine='python')
    if mode == 'npa':
        data = np.loadtxt(filepath, dtype=datatype, skiprows=skiprows)
    return data


def writefile(data, filepath, encoding='utf-8', header=False):
    """Write a given dataframe to a csv file.

    Args:
        data: A dataframe to be parsed into a file
        filepath (str): Path to the file including the filename
        encoding (str): Encoding to be used for the file, defaults to 'utf-8'
        header (boolean): Indicates if a header is included
    """
    data.to_csv(filepath, encoding=encoding, header=header)
