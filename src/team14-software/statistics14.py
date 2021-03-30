#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
# statistics14.py

"""
Module for statistic analyses.

Does correlation and euclidean distance.
"""

import pandas
import numpy as np


def correlatedata(data, corrmethod='pearson', dropcols=[]):
    """Compute pairwise correlation of data with \
       pandas.DataFrame.corr.

    Args:
        data (pandas dataframe): Data to be correlated.
        corrmethod (str): Method to be used for correlation \
                          (pandas: pearson, kendall, spearman), \
                          defaults to 'pearson'
        dropcols (list): A list with labels of columns to be dropped\
                         from the dataframe, defaults to []
    """
    #  correlate data
    data = data.corr(method=corrmethod)

    #  drop given columns
    for i in dropcols:
        print('Removing column: {}'.format(i))
        datadrop = data.drop([i], axis=1)
        data = datadrop

    #  now collect superfluous cells to be removed
    drop_values = set()  # an unordered collection of items
    cols = data.columns  # get the column labels
    for i in range(0, data.shape[1]):
        # get rid of all diagonal entries and the lower triangle
        for j in range(0, i + 1):
            drop_values.add((cols[i], cols[j]))
    print('Values to drop')
    print(drop_values)

    #  pivot the correlation matrix
    data = data.corr(method=corrmethod).unstack()
    #  sort by absolute values but keep sign
    data = data.drop(labels=drop_values).sort_values(ascending=False,
                                                     key=lambda col: col.abs())

    return data


#  used from team0
def euclidean_distance(list_ref, list_comp, vectors):
    """Calculate the Euclidean distance (L2 norm) between pairs of\
     vectors.

    Args:
        list_ref (integer list): A list with the indices of the\
         reference vectors.
        list_comp (integer list): A list with the indices of the\
        vectors to compare to.
        data (numpy array): The data object.

    Returns:
        numpy array: The Euclidean distance (L2 norm) for comparison\
         vs. reference vectors.
    """
    distances = np.zeros(len(list_ref))
    for i in range(len(list_ref)):
        distances[i] = np.linalg.norm(
            vectors[list_comp[i]] - vectors[list_ref[i]])
    return distances
