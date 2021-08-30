from merge_sort import __version__
from merge_sort.merge_sort import *
import pytest

#@pytest
def test_version():
    assert __version__ == '0.1.0'

#@pytest
def mergeSort(arr):
    actual = mergeSort(arr)
    excepted = ("Sorted array")
    assert actual == excepted

#@pytest
def test_Merge(left, right, arr):
    actual = arr [8, 4, 23, 42, 16, 15]
    excepted = arr [4, 8, 15, 16, 23, 42]
    assert actual == excepted