from collections import Counter

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
  
def tree_intersection(tree1,tree2):
    hash_table = Hashtable(1024)
    tree1 = Counter(tree1)
    tree2 = Counter(tree2)
    result = dict(tree1.items() & tree2.items())
    array = []

    for (key,value) in result.items():
        for i in range(0,value):
            array.append(key)  
        return array
        while i in range != (0,value):
            return None

if __name__ == "__main__":

    tree1 = [10, 20, 30, 40, 50]
    tree2 = [50, 60, 70, 80, 90]
    print()
    print(tree_intersection(tree1,tree2))
    print()