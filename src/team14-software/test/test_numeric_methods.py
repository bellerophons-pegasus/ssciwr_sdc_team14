#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

import pytest
import numpy as np
import numeric_methods as nl

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@pytest.fixture
def test():
    return np.fft.fft(array)


@pytest.fixture
def ref():
    return abs(np.fft.fft(array)**2)


def test_get_autocorrelation():
    """
    test auto correlation function

    """

    assert np.array_equal(nl.get_power_spectrum(array), ref)
