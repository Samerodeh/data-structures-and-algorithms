class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
def treeMax(root):
    if (root == None):
        return float('-inf')
    currnet = root.data
    leftCurrent = treeMax(root.left)
    rightCurrnet = treeMax(root.right)
    if (leftCurrent > currnet):
        currnet = leftCurrent
    if (rightCurrnet > currnet):
        currnet = rightCurrnet
    return currnet
 
if __name__ == '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.left = Node(2)
    root.left.right = Node(6)
    root.left.right.left = Node(5)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)
    
    print("The maximum value is",treeMax(root))