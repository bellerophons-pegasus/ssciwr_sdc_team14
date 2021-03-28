# filter14.py
# Module filter for team14-software

import pandas as pd

def filterdata(data, threshold=0, keeplist=[]):
    """Filters data based on variance. If variance is below a given threshold, column is discarded

    :param data: The data to be filtered.
    :type data: pandas dataframe (dict)
    :param threshold: Threshold used as limit.
    :type threshold: float , optional
    :param keeplist: List with names of columns to keep.
    :type keeplist: list, optional
    :returns: A filtered dataframe, where columns with variance below the threshold were removed
    :rtype: dataframe
    """

    for i in data.keys():
        if i in keeplist:
            continue
        if data[i].var() <= threshold:
            print('Removing column: {}'.format(i))
            data = data.drop(i, axis=1)
    return data
