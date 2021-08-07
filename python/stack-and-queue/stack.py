class Node:
   def __init__(self, value):
      self.value = value
      self.next = None

class Stack(object):
    def __init__(self, size):
        self.index = []
        self.size = size

    def push(self, value):
        ''' Pushes a element to top of the stack '''
        if(self.isFull() != True):
            self.index.append(value)
        else:
            print('Stack overflow')

    def pop(none):
        ''' Pops the top element '''
        if(none.isEmpty() != True):
            return none.index.pop()
        else:
            print('Stack is already empty!')

    def peek(none):
        ''' Returns the top element of the stack '''
        if(none.isEmpty() != True):
            return none.index[-1]
        else:
            print('Stack is already empty!')

    def isEmpty(none):
        ''' Checks whether the stack is empty '''
        return len(none.index) == []

    def isFull(self):
        ''' Checks whether the stack if full '''
        return len(self.index) == self.size

    def stackSize(self):
        ''' Returns the current stack size '''
        return len(self.index)
    
    def __str__(self):
        myString = ' '.join(str(i) for i in self.index)
        return myString

if __name__ == '__main__':
    myStack = Stack(10)
    for i in range(0, 10):
        myStack.push(i)
    print(myStack.isEmpty())        
    print(myStack.isFull())         
    print(myStack)                  
    print(myStack.stackSize())      
    print(myStack.pop())            
    print(myStack)                  
    print(myStack.peek())   