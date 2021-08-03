# Challenge Summary

### Feature Tasks

1. Write a function called zip lists
2. Arguments: 2 linked lists
3. Return: Linked List, zipped as noted below
4. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.
5. Try and keep additional space down to O(1)
6. You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.


## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency

* What approach did you take ? 

> Algorithm 

* Why ? 

> Because it is zip Linked List

* What is the Big O space/time for this approach ?

1. time : O(1), Because :  it just allocates a special iterable (called the zip object).
2. space : O(1), Because : Knoing the extra space is needed.

## Solution

        
    class Node:
     def __init__(self, data):
        self.data = data
        self.next = None
 
 

    class LinkedList:
     def __init__(self):
        self.head = None
 
    
    def append(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
 
    def addToList(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
 
        last = self.head
        while last.next:
            last = last.next
 
        last.next = newNode
 
     def zip_lists(headA, headB):
 
    storeNode = Node(0)
 
    last = storeNode
    while True:
 
        if headA is None:
            last.next = headB
            break
        if headB is None:
            last.next = headA
            break
 
        if headA.data <= headB.data:
            last.next = headA
            headA = headA.next
        else:
            last.next = headB
            headB = headB.next
        
        last = last.next
 
    return storeNode.next
 
    listA = LinkedList()
    listB = LinkedList()
 
    listA.addToList(4)
    listA.addToList(5)
    listA.addToList(6)
 
    listB.addToList(1)
    listB.addToList(2)
    listB.addToList(3)
 
    listA.head = zip_lists(listA.head, listB.head)

    print("zip_lists is:")
    listA.append()
 
| Subject     | links |
| ----------- | ----------- |
| Linked List zip | [linked_list_zip/linked_list_zip.py](linked_list_zip/linked_list_zip.py) |
| Test Linked List zip | [tests/test_linked_list_zip.py](tests/test_linked_list_zip.py) |