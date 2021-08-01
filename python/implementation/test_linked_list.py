from __init__ import __version__
from implementation.linked_list import Linkedlist 

def test_version():
    assert __version__ == '0.1.0'

def test_instantiate():
    ListNode = Linkedlist()
    actual = ListNode.head
    expected = None
    assert actual == expected

def test_add():
    ListNode = Linkedlist()
    ListNode.add()
    actual=ListNode.head.data
    expected=()
    assert actual == expected

def test_head():
    ListNode = Linkedlist()
    ListNode.add()
    assert ListNode.head.data == ()

def test_data():
    ListNode = Linkedlist()
    ListNode.add()
    ListNode.insert() 
    assert ListNode.includes() == True

def test_data1():
    ListNode = Linkedlist()
    ListNode.add()
    ListNode.insert()
    assert ListNode.includes() == False

def test_str():
   ListNode = Linkedlist()
   ListNode.add()
   ListNode.insert()
   assert ListNode.__str__()=='{}---> {}---> {}---> NULL'
   
def List_Node():
        ListNode = Linkedlist()

        ListNode.add(5)
        ListNode.insert(11)
        ListNode.insert(23)
        ListNode.insert(47)
        ListNode.insert(94)

        return ListNode