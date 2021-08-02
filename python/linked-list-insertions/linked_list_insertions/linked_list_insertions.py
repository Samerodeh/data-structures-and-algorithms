class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        current = self.head
        string = ""
        while current:
            string += str(current) + " -> "
            current = current.next
        string += "None"
        return string

    def append(self, value):
        node = Node(value)

        current = self.head
        if current:
            while current.next:   
                current = current.next
            current.next = node
        else:
            self.head = node

    def insertAfter(self, value, key):
        found = False

        node = Node(value)

        current = self.head
        
        while current:
            if current.data == key:
                node.next = current.next
                current.next = node
                found = True
                break
            current = current.next
        if not found:
            raise Exception("Not found")
    
    def insertBefore(self, value, key):
        found = False

        node = Node(value)
        prev = self.head
        current = self.head
        
        while current:
            if current.data == key:
                prev.next = node
                node.next = current
                found = True
                break
            prev = current
            current = current.next
        if not found:
            raise Exception("Not found")
    

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    My_List = LinkedList()
    My_List.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    My_List.append(11)
    My_List1 =  LinkedList()
    My_List1.append("A")
    My_List1.append("B")
    assert My_List1.head.data == "A"
    assert My_List1.head.next.data == "B"
    assert My_List1.head.next.next == None
    print(My_List1)
    print(My_List)

    My_List2 = LinkedList()
    try:
        My_List2.insertAfter(2,1)
    except Exception as e:
        print(e)
        assert str(e) == "Not found"
        print("Passed")
    
    My_List2.append(1)
    My_List2.append(3)
    My_List2.insertAfter(2,1)

    print(My_List2)
    assert My_List2.head.next.data == 2
    print("Inserted")

    try:
        My_List2.insertAfter(2,8)
    except Exception as e:
        print(e)
        assert str(e) == "Not found"
        print("Passed")


    My_List3 = LinkedList()
    try:
        My_List3.insertBefore(2,1)
    except Exception as e:
        print(e)
        assert str(e) == "Not found"
        print("Passed")
    
    My_List3.append(1)
    My_List3.append(3)
    My_List3.insertBefore(2,3)

    print(My_List3)
    assert My_List3.head.next.data == 2
    print("Inserted")

    try:
        My_List3.insertBefore(2,8)
    except Exception as e:
        print(e)
        assert str(e) == "Not found"
        print("Passed")