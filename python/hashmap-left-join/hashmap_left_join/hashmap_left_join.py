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

def left_join(hash_map1,hash_map2):
    result=[]

    if hash_map1.map == hash_map1.size*[None] or hash_map2.map == hash_map2.size*[None] :
        return 'hash map is empty'

    for item in hash_map1.map:
        if item:
            arr=[]
            arr.append(item.head.data[0])
            arr.append(hash_map1.get(item.head.data[0]))
            arr.append(hash_map2.get(item.head.data[0]))
            result.append(arr) 
    return result


if __name__ == "__main__":

    hash_map1 = Hashtable(1024)
    hash_map1.add('Samer', 'Odeh')

    hash_map2 = Hashtable(1024)
    hash_map2.add('Odeh', 'Samer')

    print(left_join(hash_map1,hash_map2))