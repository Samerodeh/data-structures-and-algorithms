from quick_sort import __version__
from quick_sort.quick_sort import *
import pytest

#@pytest
def test_version():
    assert __version__ == '0.1.0'

#@pytest
def test_QuickSort(arr):
    array = [8,4,23,42,16,15]
    actual = array
    excepted = [4, 8, 15, 16, 23, 42]
    assert actual == excepted
