from __init__ import __version__
from linked_list import Linkedlist 

def test_version():
    assert __version__ == '0.1.0'

def test_instantiate():
    ListNode = Linkedlist()
    actual = ListNode.head
    expected = None
    assert actual == expected

def add():
    ListNode = Linkedlist()
    ListNode.add()
    actual=ListNode.head.data
    expected=()
    assert actual == expected

def head():
    ListNode = Linkedlist()
    ListNode.add()
    assert ListNode.head.data == ()

def data():
    ListNode = Linkedlist()
    ListNode.add()
    ListNode.append()
    assert ListNode.includes() == True

def data1():
    ListNode = Linkedlist()
    ListNode.add()
    ListNode.append()
    assert ListNode.includes() == False

def str():
   ListNode = Linkedlist()
   ListNode.add()
   ListNode.append()
   assert ListNode.__str__()=='{}---> {}---> {}---> NULL'
   
def List_Node():
        ListNode = Linkedlist()

        ListNode.add(5)
        ListNode.append(11)
        ListNode.append(23)
        ListNode.append(47)
        ListNode.append(94)

        return ListNode