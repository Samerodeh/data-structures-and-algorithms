# Stacks and Queues

* Node

*Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.*

* Stack

*Create a Stack class that has a top property. It creates an empty Stack when instantiated.* 

* Queue

*Create a Queue class that has a front property. It creates an empty Queue when instantiated.* 

* Testing 

1. Can successfully push onto a stack
2. Can successfully push multiple values onto a stack
3. Can successfully pop off the stack
4. Can successfully empty a stack after multiple pops
5. Can successfully peek the next item on the stack
6. Can successfully instantiate an empty stack
7. Calling pop or peek on empty stack raises exception
8. Can successfully enqueue into a queue
9. Can successfully enqueue multiple values into a queue
10. Can successfully dequeue out of a queue the expected value
11. Can successfully peek into a queue, seeing the expected value
12. Can successfully empty a queue after multiple dequeues
13. Can successfully instantiate an empty queue
14. Calling dequeue or peek on empty queue raises exception


## Challenge


### Features

> Node

* Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

> Stack

* Create a Stack class that has a top property. It creates an empty Stack when instantiated.
* The class should contain the following methods:

* push
1. Arguments: value
2. adds a new node with that value to the top of the stack with an O(1) Time performance.
        
* pop

1. Arguments: none
2. Returns: the value from node from the top of the stack
3. Removes the node from the top of the stack
4. Should raise exception when called on empty stack

* peek
1. Arguments: none
2. Returns: Value of the node located at the top of the stack
3. Should raise exception when called on empty stack

* is empty

1. Arguments: none
2. Returns: Boolean indicating whether or not the stack is empty.

> Queue

* Create a Queue class that has a front property. It creates an empty Queue when instantiated.
* The class should contain the following methods:
        
* enqueue

1. Arguments: value
2. adds a new node with that value to the back of the queue with an O(1) Time performance.
        
* dequeue

1. Arguments: none
2. Returns: the value from node from the front of the queue
3. Removes the node from the front of the queue
4. Should raise exception when called on empty queue
        
* peek
            
1. Arguments: none
2. Returns: Value of the node located at the front of the queue
3. Should raise exception when called on empty stack
        
* is empty
            
1. Arguments: none
2. Returns: Boolean indicating whether or not the queue is empty


## Approach & Efficiency

> What approach did you take ? 

* Algorithm 

> Why ?  

* Because it is stack-and-queue

> What is the Big O space/time for this approach ? 

* Stack : 

**Time : O(1)**

**Space : O(n)**

* Queue : 

**Time : O(1)**

**Space : O(n)**


| Subject     | links |
| ----------- | ----------- |
| Stack | [stack.py](stack.py) |
| Queue | [queue.py](queue.py) |