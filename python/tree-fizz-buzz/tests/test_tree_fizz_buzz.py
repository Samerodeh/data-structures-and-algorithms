from tree_fizz_buzz import __version__
from tree_fizz_buzz.tree_fizz_buzz import *
import pytest


def test_version():
    assert __version__ == '0.1.0'

@pytest
def test_fizz_buzz_tree_1(self, k_ary_tree : 'int') -> 'List[str]':
    result = []
    expected = result.append("FizzBuzz")
    actual = (i % 3 == 0 and i % 5 == 0)
    assert actual == expected 

def test_fizz_buzz_tree_2():
    result = []
    expected = result.append("Fizz")
    actual = (i % 3 == 0)
    assert actual == expected 

def test_fizz_buzz_tree_3():
    result = []
    expected = result.append("Buzz")
    actual = (i % 5 == 0)
    assert actual == expected 

def test_fizz_buzz_tree_4():
    result = []
    expected = result.append(str(i))
    actual = (not i % 3 == 0 and not i % 5 == 0)
    assert actual == expected 

