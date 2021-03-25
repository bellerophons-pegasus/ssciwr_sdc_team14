# test2_filter14.py
# test for module filter14 with pytest

import pytest
import pandas as pd
import filter14 as f14

class DF:
        def __init__(self, testdict):
            self.testdict = testdict

        def init_df(self):
            test_df = pd.DataFrame(data=testdict)
            return test_df

# runs this function before the test starts;
# here a variable for testing is defined
@pytest.fixture(testval)
def test_df():
    testval = build_testval({'col1': [1, 2], 'col2': [3, 4]})
    return DF.init_df(testval)



def test_filterdata(testval, refval):
     """Tests for filterdata"""
     assert len(filterdata(testval)) == len(refval)
#
#         test1 = f14.filterdata(test_df)
#         self.assertEqual(len(test1.columns), len(test_df.columns))
#         test2 = f14.filterdata(test_df, 0.5)
#         self.assertLess(len(test2.columns), len(test_df.columns))
#         test3 = f14.filterdata(test_df, 0.5, ['col1', 'col2'])
#         self.assertEqual(len(test3.columns), len(test_df.columns))
#         test4 = f14.filterdata(test_df, 0.5, ['col1'])
#         self.assertGreater(len(test4.columns), len(test2.columns))
