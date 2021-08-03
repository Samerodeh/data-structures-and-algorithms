# Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
# Create LinkedList
class LinkedList:
    def __init__(self):
        self.head = None
 
    # Method to display the list
    def append(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
 
    # Method to add element to list
    def addToList(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
 
        last = self.head
        while last.next:
            last = last.next
 
        last.next = newNode
 
 
# Function to zip the lists
# Takes two lists which are sorted
# joins them to get a single sorted list
def zip_lists(headA, headB):
 
    # A store node to store the result
    storeNode = Node(0)
 
    # Last stores the last node
    last = storeNode
    while True:
 
        # If any of the list gets completely empty
        # directly join all the elements of the other list
        if headA is None:
            last.next = headB
            break
        if headB is None:
            last.next = headA
            break
 
        # Compare the data of the lists and whichever is smaller is
        # appended to the last of the merged list and the head is changed
        if headA.data <= headB.data:
            last.next = headA
            headA = headA.next
        else:
            last.next = headB
            headB = headB.next
 
        # Advance the last
        last = last.next
 
    # Returns the head of the merged list
    return storeNode.next
 
 
# Create 2 lists
listA = LinkedList()
listB = LinkedList()
 
# Add elements to the list in sorted order
listA.addToList(4)
listA.addToList(5)
listA.addToList(6)
 
listB.addToList(1)
listB.addToList(2)
listB.addToList(3)
 
# Call the zip_lists function
listA.head = zip_lists(listA.head, listB.head)
 
# Display zip_lists list
print("zip_lists is:")
listA.append()
 