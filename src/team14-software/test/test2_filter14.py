# test2_filter14.py
# test for module filter14 with pytest

import pytest
import pandas as pd
import filter14 as f14

class build_df:
        def __init__(self):
            pass

        def init_df(self, testdict):
            test_df = pd.DataFrame(data=testdict)
            return test_df

# runs this function before the test starts;
# here a variable for testing is defined
@pytest.fixture()
def testval():
    obj = build_df()
    testval = obj.init_df({'col1': [1, 2], 'col2': [3, 4]})
    return testval

# runs this function before the test starts;
# here another variable for testing is defined
@pytest.fixture()
def refval():
    obj2 = build_df()
    refval = obj2.init_df({'col1': [1, 2], 'col2': [3, 4]})
    return refval

@pytest.fixture()
def emptyrefval():
    obj3 = build_df()
    emptyrefval = obj3.init_df({})
    return emptyrefval


@pytest.mark.parametrize("threshold, columns", [(  0, []),
                                                (0.5, ['col1', 'col2']),
                                                (0.5, ['col1']),
                                                (0.6, [])])
def test_filterdata(testval, refval, emptyrefval, threshold, columns):
    """Tests for filterdata"""
    if len(columns)== 1:
        assert len(f14.filterdata(testval,threshold, columns)) > len(emptyrefval)
    elif threshold == 0.6:
        assert len(f14.filterdata(testval,threshold, columns).columns) < len(refval.columns)
    else:
        assert len(f14.filterdata(testval,threshold, columns)) == len(refval)
