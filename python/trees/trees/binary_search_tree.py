class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild=None
     
def add(root,value):
    if root is None:
        root=BinaryTreeNode(value)
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