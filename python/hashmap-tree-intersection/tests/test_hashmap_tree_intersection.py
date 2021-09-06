from hashmap_tree_intersection import __version__
from hashmap_tree_intersection.hashmap_tree_intersection import *
import pytest

#@pytest
def test_version():
    assert __version__ == '0.1.0'

#@pytest
def test_tree_intersection():
    tree1 = Counter("tree1")
    tree2 = Counter("tree2")
    array = []
    actual = tree1, tree2
    excepted = array 
    assert actual == excepted
