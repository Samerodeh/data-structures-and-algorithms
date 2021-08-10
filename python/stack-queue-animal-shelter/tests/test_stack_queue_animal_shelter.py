from stack_queue_animal_shelter import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_enqueue():
    expected = 'animal'
    actual = 'Cats, Dogs'
    assert expected is actual, "animal : Cats, Dogs"

def test_dequeue():
    expected = 'name'
    actual = 'pref'
    assert expected is actual, "name : pref"