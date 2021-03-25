# statistics14.py
# Module statistics for team14-software

import pandas as pd

def correlatedata(data, corrmethod='pearson', dropcols=[]):
    """Compute pairwise correlation of data with pandas.DataFrame.corr
    :param data: Data to be correlated.
    :type data: pandas dataframe (dict)
    :param corrmethod: Method to be used for correlation (pandas: pearson, kendall, spearman).
    :type corrmethod: string, optional
    """

    # correlate data
    data = data.corr(method=corrmethod)

    # drop given columns
    for i in dropcols:
        print('Removing column: {}'.format(i))
        datadrop = data.drop([i], axis=1)
        data = datadrop

    # now collect superfluous cells to be removed
    drop_values = set() # an unordered collection of items
    cols = data.columns # get the column labels
    for i in range(0, data.shape[1]):
        for j in range(0, i+1): # get rid of all diagonal entries and the lower triangle
            drop_values.add((cols[i], cols[j]))
    print('Values to drop')
    print(drop_values)

    data = data.corr(method=corrmethod).unstack() # pivot the correlation matrix
    data = data.drop(labels=drop_values).sort_values(ascending=False, key=lambda col: col.abs()) # sort by absolute values but keep sign
   # display(data)

    return data
