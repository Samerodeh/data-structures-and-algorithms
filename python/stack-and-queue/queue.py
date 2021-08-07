class Node:
   def __init__(self, value):
      self.value = value
      self.next = None

class Queue(object):
    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, value):
        '''This function adds an value to the rear end of the queue '''
        if(self.isFull() != True):
            self.queue.insert(0, value)
        else:
            print('Queue is Full!')

    def dequeue(none):
        ''' This function removes an item from the front end of the queue '''
        if(none.isEmpty() != True):
            return none.queue.pop()
        else:
            print('Queue is Empty!')

    def peek(none):
        ''' This function helps to see the first element at the fron end of the queue '''
        if(none.isEmpty() != True):
            return none.queue[-1]
        else:
            print('Queue is Empty!')

    def isEmpty(none):
        ''' This function checks if the queue is empty '''
        return none.queue == []

    def isFull(self):
        ''' This function checks if the queue is full '''
        return len(self.queue) == self.size

    def __str__(self):
        myString = ' '.join(str(i) for i in self.queue)
        return myString    

if __name__ == '__main__':
    myQueue = Queue(10)
    myQueue.enqueue(4)
    myQueue.enqueue(5)
    myQueue.enqueue(6)
    
    print(myQueue)
    
    myQueue.enqueue(1)
    myQueue.enqueue(2)
    myQueue.enqueue(3)
    
    print(myQueue)
    
    myQueue.dequeue()
    
    print(myQueue)