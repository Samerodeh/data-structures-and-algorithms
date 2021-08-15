class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item

class BinaryTree:
    def __init__(self):
        pass

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) + " -> ", end = '')
        inorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + " -> ", end = '')


def preorder(root):
    if root:
        print(str(root.val) + " -> ", end = '')
        preorder(root.left)
        preorder(root.right)

class BinarySearchTree:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild=None
     
def add(root,value):
    if root is None:
        root=BinarySearchTree(value)
        return root

    if value<root.data:
        root.leftChild=add(root.leftChild,value)
    else:
        root.rightChild=add(root.rightChild,value)
    return root

def Contains(root,value):
    if root==None:
        return False
    elif root.data==value:
        return True
    elif root.data <value:
        return Contains(root.rightChild,value)
    else:
        return Contains(root.leftChild,value)
  

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right = Node(6)

    print("Inorder traversal ")
    inorder(root)

    print("\nPreorder traversal ")
    preorder(root)

    print("\nPostorder traversal ")
    postorder(root)

    root= add(None, 15)
    add(root,1)
    add(root,5)
    add(root,15)
    add(root,7)
    add(root,9)
    print(Contains(root,5))
    print(Contains(root,10))
    print(Contains(root,13))
    print(Contains(root,9))