class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
       
class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if not self.isEmpty():
            self.head = self.head.next
            self.head.next = None
            return self.head.value
        else:
            return "is empty"

    def peek(self):
        try:
            return self.head.value
        except:
            return "is empty "

    def isEmpty(self):
        return None
         
class PseudoQueue:
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()
        self.Node = None
        self.head = None

    def enqueue(self, value):
        self.stack_1.push(value)
        self.Node = self.stack_1.head.value

    def dequeue(self):
        if self.stack_1.head:
            stack1 = self.stack_1
            while not stack1.isEmpty():
                self.stack_2.push(stack1.pop())

            poped = self.stack_2.pop()
            self.head = self.stack_2.head
            self.stack_1 = Stack()
            stack2 = self.stack_2
            while not stack2.isEmpty():
                self.stack_1.push(stack2.pop())
            return poped

    def __str__(self):
        String = ''
        current = self.stack_1.head
        while current:
            String += f"{{{str(current.value)}}} -> "
            current = current.next
        String += " Null"
        return String

if __name__ == '__main__':
  pass
