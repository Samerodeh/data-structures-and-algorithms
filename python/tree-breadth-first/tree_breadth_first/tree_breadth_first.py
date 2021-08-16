class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def breadthFirst(tree):
    if tree is None:
      return 

    queue = []

    queue.append(tree)

    while(len(queue) > 0):
        print(queue[0].data)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)
 
if __name__ == '__main__':
  tree = Node(1)
  tree.left = Node(2)
  tree.right = Node(3)
  tree.left.left = Node(4)
  tree.left.right = Node(5)
  breadthFirst(tree) 