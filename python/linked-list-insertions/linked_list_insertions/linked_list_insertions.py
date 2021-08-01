class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, newElement):
    newNode = Node(newElement)
    if(self.head == None):
      self.head = newNode
      newNode.next = self.head
      return
    else:
      temp = self.head
      while(temp.next != self.head):
        temp = temp.next
      temp.next = newNode
      newNode.next = self.head

  def insert(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (True):
        print(temp.data, end=" ")
        temp = temp.next
        if(temp == self.head):
          break
      print()
    else:
      print("The list is empty.")

if __name__=="__main__":
    
 MyList = LinkedList()

 MyList.append(5)
 MyList.insert()