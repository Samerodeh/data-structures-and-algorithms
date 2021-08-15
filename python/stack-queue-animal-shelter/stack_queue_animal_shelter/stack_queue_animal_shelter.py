class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Queue():
    def __init__(self):
        self.head = None
        self.Node = None

    def enqueue(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.Node = node
            return self.Node.value
        else:
            self.Node.next = node
            self.Node = node
            return self.Node.value

    def dequeue(self):
            if self.head == None:
              self.head = self.head.next
              return self.head.value
            else:
              return None

    def peek(self):
            if self.head == None:
              return self.head.value
            else:
              return None

    def isEmpty(self):
        return self.head == None

class AnimalShelter:
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()
        
    def enqueue(self, animal, kind):
        if kind == 'cat':
            return self.cat.enqueue(animal)
        elif kind == 'dog':
            return self.dog.enqueue(animal)
        else:
            return 'Not Cat or Dog'

    def dequeue(self, pref):
        if pref == 'dog':
            return self.dog.dequeue()
        if pref == 'cat':
            return self.cat.dequeue()
        else:
            return 'Not Cat or Dog'

    def is_empty(self):
        return None

if __name__ == '__main__':
  pass
