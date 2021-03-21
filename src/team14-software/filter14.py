# filter14.py
# Module filter for team14-software

import pandas as pd

def filterdata(data, treshhold=0, keeplist=[]):
    """Filters data based on variance. If variance is below a given threshold, column is discarded

        Arguments:
            data: data to be filtered, as dataframe
            treshhold: xx
            keeplist: optional, a list with column names to keep
    """

    for i in data.keys():
        if i in keeplist:
            continue
        if data[i].var() <= treshhold:
            print('Removing column: {}'.format(i))
            data = data.drop(i, axis=1)
    return data
