# test2_filter14.py
# test for module filter14 with pytest

import pytest
import pandas as pd
import filter14 as f14

class build_testval:
        def __init__(self, testdict):
            self.testdict = testdict

        def init_df(self):
            testdata =
            test_df = pd.DataFrame(data=testdata)
            return test_df

# runs this function before the test starts;
# here a variable for testing is defined
@pytest.fixture
def test_wf():
    testval = build_testval({'col1': [1, 2], 'col2': [3, 4]})
    return obj.init_df()



def test_filterdata(testval):
     """Tests for filterdata"""
     assert calc_auto(testval) == refval
#
#         test1 = f14.filterdata(test_df)
#         self.assertEqual(len(test1.columns), len(test_df.columns))
#         test2 = f14.filterdata(test_df, 0.5)
#         self.assertLess(len(test2.columns), len(test_df.columns))
#         test3 = f14.filterdata(test_df, 0.5, ['col1', 'col2'])
#         self.assertEqual(len(test3.columns), len(test_df.columns))
#         test4 = f14.filterdata(test_df, 0.5, ['col1'])
#         self.assertGreater(len(test4.columns), len(test2.columns))
