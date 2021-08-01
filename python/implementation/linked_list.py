class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def add(self, data):
        node1 = Node(data)
        if not self.head:
            self.head=node1
        else:
             return ("---")

    def insert(self, data):
        node1 = Node(data)
        if self.head==None:
            self.head=node1
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=Node(data)

    def includes(self,data):
        if self.head:
            current=self.head
            while current:
                if current.data==data:
                    return True
                current=current.next
            return False
        else:
            return ("---")

    def __str__(self):
        if self.head:
            data_str=""
            current=self.head
            while current:
                data_str +='('+str(current.data)+')---> '
                current=current.next
            data_str +='NULL'
            return data_str
        else:
            return ("---")

if __name__ == "__main__":
        ListNode = Linkedlist()

        ListNode.add(5)
        ListNode.insert(11)
        ListNode.insert(23)
        ListNode.insert(47)
        ListNode.insert(94)

        print(ListNode)