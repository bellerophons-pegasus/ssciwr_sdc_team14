import pytest
import numpy as np
from team14-software import numeric_methods as nl

class build_wf:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

def test_get_autocorrelation():
    """
    test auto correlation function

    """