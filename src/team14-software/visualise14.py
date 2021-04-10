#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
# visualise.py
# docstring with sphinx and napoleon

"""
A module to visualise data.

A collection of functions to plot data and save the resulting figure as a pdf.
"""

import matplotlib.pyplot as plt
import seaborn as sb


def plotlinlog(data, caption, figsize=(6, 9), outFile='linlogFig.pdf'):
    """Plot data in linear scale and logarithmic scale.

    Args:
        data (pandas dataframe (dict)): The data to be plotted.
        caption (str): The caption for the figure.
        figsize (tuple): optional, The size for the figure.
        outFile (str): optional, Path to the output file.
    """
    fig, ax = plt.subplots(2, figsize=figsize)
    fig.suptitle(caption)
#    fig.suptitle('Linear scale above, logarithmic scale below')
# for i in range(len(df_expect.keys())):

    for i in range(len(data.keys())):
        ax[0].plot(data[data.keys()[i]], label=data.keys()[i])

    ax[0].legend()
    ax[1].plot(data)
    ax[1].set_yscale('symlog')

#    fig.savefig('../pdfPlots/expect.pdf',format='pdf')
    fig.savefig(outFile, format='pdf')


def plotseaborn(data, caption, x='time', y='value', hue='variable',
                outFile='sbFig.pdf'):
    """Plot data with seaborn.

    Args:
        data (pandas dataframe, long format): Data to be plotted.
        caption (str): The caption for the figure.
        x (str): optional, column for x-axis
        y (str): optional, column for y-axis
        hue (str): optional, column for grouping to produce lines in different \
        colors.
        outFile (str): optional, Path to the output file.
    """
# TODO
# Plot the remaining columns. Seaborn prefers "long format" (one column for \
# all measurement values, one column to indicate the type) as input, whereas\
# the cvs is in "wide format" (one column per measurement type).

# wide to long format
#    npop_longFormat = pd.melt(df_npopfiltered, id_vars=['time'])
# sb.lineplot(x='time', y='value', hue='variable', data = npop_longFormat)

    sb.lineplot(x=x, y=y, hue=hue, data=data)
    # place legend
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()
    plt.savefig(outFile)

# plt.bar(x, out_dist)
# plt.xticks(x, ('x', 'y', 'z'))
# plt.xlabel("table index")
# plt.ylabel("euclidean distance")
# plt.legend()
# plt.show()
# plt.savefig("euclideandistance.pdf")
