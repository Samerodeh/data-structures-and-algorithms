from hashmap_repeated_word import __version__
from hashmap_repeated_word.hashmap_repeated_word import *
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
def test_repeated_word():
    actual = 'string'
    excepted = 'string'
    assert actual == excepted
