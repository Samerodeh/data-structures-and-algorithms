class Hashtable:
    def __init__(self, size):
        self.size = size
        self.map = [None]*size 
    
    def hash(self, key):
        index = 0
        for i in key:
            idx = ord(i)
            index += idx
        temp = index * 7
        hash = temp % self.size
        return hash
    
    def add(self, key, value):
        hash = self.hash(key)
        if not self.map[hash]:
            self.map[hash] = [key, value]
        self.map[hash].add((key,value))

    def contains(self,key):
        hash = self.hash(key)
        if self.map[hash]:
            self.map[hash].head.data[0]
            current=self.map[hash].head
            while current:
                if current.data[0]==key:
                    return True
                else:
                    current=current.next
        return False

    def get(self,key):
        hash = self.hash(key)
        if self.map[hash]:
            self.map[hash].head.data[0]
            current=self.map[hash].head
            while current:
                if current.data[0]==key:
                    return current.data[1]
                else:
                    current=current.next
        return None
  
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)
  
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTrees:
    def __init__(self):
        self.root = None

def tree_intersection(tree1,tree2):
    result = []
    hash_table = Hashtable(1024)

    if tree1.root == None or tree2.root == None:
        return 'tree is empty'

    def tree_travers(node):
        if hash_table.contains(str(node.value)):
            nonlocal result
            result += [node.value]
        else:
            hash_table.add(str(node.value),True)

        if node.left:
            tree_travers(node.left)
        if node.right:
            tree_travers(node.right)

    tree_travers(tree1.root)
    tree_travers(tree2.root)
    return result

if __name__ == "__main__":

    tree1 = BinaryTrees()
    tree1.root = Node(20)
    tree1.root.left = Node(10)
    tree1.root.right = Node(50)
    tree1.root.left.left = Node(30)
    tree1.root.left.right = Node(40)

    tree2 = BinaryTrees()
    tree2.root = Node(60)
    tree2.root.left = Node(50)
    tree2.root.right = Node(90)
    tree2.root.left.left = Node(70)
    tree2.root.left.right = Node(80)

    print(tree_intersection(tree1,tree2))