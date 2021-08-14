from stack_queue_animal_shelter import __version__
from stack_queue_animal_shelter import * 

def test_version():
    assert __version__ == '0.1.0'

def test_enqueue():
    actual = ('poppy', 'dog')
    excepted = ('dog')
    actual = ('jojo', 'cat')
    excepted = ('cat')
    actual = ('goldenfish', 'fish')
    excepted = 'Not Cat or Dog'
    assert actual == excepted

def test_dequeue():
    actual = ('maxi', 'dog')
    excepted = ('dog')
    actual = ('sela', 'cat')
    excepted = ('cat')
    actual = ('popo', 'parrot ')
    excepted = 'Not Cat or Dog'
    assert actual == excepted
