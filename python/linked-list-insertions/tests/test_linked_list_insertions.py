from linked_list_insertions import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_sum(a,b):
  """ sum two numeric arguments """
  
  if isinstance(a, (int, float)) and isinstance(b, (int, float)):
    return a + b

  raise TypeError('argument must be int or float')

def test_should_sum_two_integers():
    expected = 3
    actual = sum(1,2)
    assert expected is actual, "sum of 1 and 2 should be 3"

def test_should_sum_two_larger_integers():
    expected = 1333332
    actual = sum(1234567,98765)
    assert expected is actual, "sum of 1234567 and 98765 should be 1333332" 

def test_should_sum_negative_numbers():
    expected = 3
    actual = sum(5,-2)
    assert expected is actual, "sum of 5 and -2 should be 3"

def test_should_handle_single_argument():
    expected = 2
    actual = sum(2)
    assert expected is actual, "sum of 2 and nothing should be 2 because 2nd argument defaults to 0"