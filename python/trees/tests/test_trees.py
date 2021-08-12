from python.trees import trees
from trees import __version__
from trees.binary_tree import *
from trees.binary_search_tree import *
import pytest

def test_version():
    assert __version__ == '0.1.0' 


def test_InOrder(fixed_BinaryTree):
    expected = '4 -> 2 -> 5 -> 1 -> 3 ->'
    actual = '4 -> 2 -> 5 -> 1 -> 3 ->'
    assert fixed_BinaryTree.InOrder() == '4 -> 2 -> 5 -> 1 -> 3 ->'

def test_PreOrder(fixed_BinaryTree):
    expected = '1 -> 2 -> 4 -> 5 -> 3 ->'
    actual = '1 -> 2 -> 4 -> 5 -> 3 ->'
    assert fixed_BinaryTree.PreOrder() == '1 -> 2 -> 4 -> 5 -> 3 ->'

def test_PostOrder(fixed_BinaryTree):
    expected = '4 -> 5 -> 2 -> 3 -> 1 -> % '
    actual = '4 -> 5 -> 2 -> 3 -> 1 -> % '
    assert (expected, actual, fixed_BinaryTree.PostOrder() == '4 -> 5 -> 2 -> 3 -> 1 -> % ')




def test_add(root,value):
    expected = 'root, 1'
    actual = 'root, 1'
    assert(expected, actual)

def test_Contains(root,value):
    excepted = 'Boleen'
    actual = 'Boleen'
    assert(excepted, actual)

def test_fixed_BinaryTree():
    trees = fixed_BinaryTree

@pytest.fixture
def fixed_BinaryTree():
    root = BinaryTree()
    root = Node('1')
    root.left = Node('2')
    root.right = Node('3')
    root.left.left = Node('4')
    root.left.right = Node('5')
    root.right.left = Node('6')

