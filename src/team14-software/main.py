#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
# main.py

"""Executes all tasks and uses modules.

If the package shall be run as a script, then this can be used.
"""

import os.path as path
import numpy as np
import pandas as pd
import io14 as io14
import filter14 as f14
import statistics14 as s14
import visualise14 as v14
# import numeric_methods as nm


if __name__ == "__main__":
    threshold = 1.0e-5
    fileDir = path.join('..', '..', 'data')
    outDir = path.join('..', 'pdfPlots')
    # task 1
    df_expect = io14.readfile(path.join(fileDir, 'expec.t'), 'df', '   ')
    v14.plotlinlog(df_expect, 'Linear scale above, logarithmic scale below',
                   outFile=path.join(outDir, 'task1Fig_unfiltered.pdf'))
    filter_expect = f14.filterdata(df_expect, threshold)
    # task 2
    v14.plotlinlog(filter_expect, 'Linear scale above, logarithmic scale below',
                   outFile=path.join(outDir, 'task2Fig_filtered.pdf'))
    # task 3
    df_npop = io14.readfile(path.join(fileDir, 'npop.t'), 'df',
                            '    |   |  ')
    filter_npop = f14.filterdata(df_npop, threshold, ['time'])
    long_filter_npop = pd.melt(filter_npop, id_vars=['time'])
    v14.plotseaborn(long_filter_npop, 'npop, filtered',
                    outFile=path.join(outDir, 'task3Fig_filtered.pdf'))
    corr_npop = s14.correlatedata(filter_npop, 'pearson', ['time'])
    # task 4
    io14.writefile(corr_npop, path.join(fileDir, 'npop_processed.csv'))
    # task 5 (not complete)
    arr = io14.readfile(path.join(fileDir, 'table.dat'), 'npa')
    arr = np.nan_to_num(arr)
    # main('efield.t', 'data/', 'output/')
    # main('nstate_i.t', 'data/', 'output/')
