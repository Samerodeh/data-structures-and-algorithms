from collections import defaultdict

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
 
def left_join(hash_map1, index1, hash_map2, index2):
    hash_table = Hashtable(1024)
    hash = defaultdict(list)
    for i in hash_map1:
        hash[i[index1]].append(i)
    return [(i, r) for r in hash_map2 for i in hash[r[index2]]]

if __name__ == '__main__':

  hash_map1 = (23, "Samer"),
  hash_map2 = ("Samer", "Odeh"),
 
for row in left_join(hash_map1, 1, hash_map2, 0):
    print(row)
     
