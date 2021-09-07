from hashmap_left_join import __version__
from hashmap_left_join.hashmap_left_join import *
import pytest

#@pytest
def test_version():
    assert __version__ == '0.1.0'

#@pytest
def test_add():
  actual = 'key'
  excepted = 'value'
  assert actual == excepted

#@pytest
def test_get():
  actual = 'key'
  excepted = 'value'
  assert actual == excepted


#@pytest
def test_left_join(hashmap1, hashmap2):
    actual = hash_map1
    excepted = hash_map2
    assert actual == excepted
