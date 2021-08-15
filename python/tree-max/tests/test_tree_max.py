from tree_max import __version__
from tree_max.tree_max import *


def test_version():
    assert __version__ == '0.1.0' 

def test_treeMax(root):
    currnet = root.data
    leftCurrent = treeMax(root.left)
    rightCurrnet = treeMax(root.right)
    expected = int 
    actual = (f"{leftCurrent, rightCurrnet}") 
    assert actual == expected

        