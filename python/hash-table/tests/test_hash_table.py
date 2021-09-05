from hash_table import __version__
from hash_table.hash_table import *
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

