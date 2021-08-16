from tree_breadth_first import __version__
from tree_breadth_first.tree_breadth_first import *

def test_version():
    assert __version__ == '0.1.0'

def test_breadthFirst(tree):
    queue = []
    node = queue.pop(0)
    expected =  queue.append(tree)
    actual = (f"{queue.append(node.left), queue.append(node.right)}")
    assert actual == expected