#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
# test_filter14.py

"""
Test module filter14.

Uses unittest.
"""

import unittest
import filter14 as f14
import pandas as pd


class test_filterdata(unittest.TestCase):
    """Tests for filterdata.
    """
    def test_filterdata(self):
        testdata = {'col1': [1, 2], 'col2': [3, 4]}
        test_df = pd.DataFrame(data=testdata)
        test1 = f14.filterdata(test_df)
        self.assertEqual(len(test1.columns), len(test_df.columns))
        test2 = f14.filterdata(test_df, 0.5)
        self.assertLess(len(test2.columns), len(test_df.columns))
        test3 = f14.filterdata(test_df, 0.5, ['col1', 'col2'])
        self.assertEqual(len(test3.columns), len(test_df.columns))
        test4 = f14.filterdata(test_df, 0.5, ['col1'])
        self.assertGreater(len(test4.columns), len(test2.columns))
