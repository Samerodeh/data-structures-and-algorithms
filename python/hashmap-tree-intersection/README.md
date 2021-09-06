# Challenge Summary

### Feature Tasks

***Find all values found to be in 2 binary trees***

* Write a function called tree intersection
* Arguments: two binary trees
* Return: array


## Whiteboard Process

![Whiteboard Process](asset/hashmap-tree-intersection.png)

## Approach & Efficiency

### What approach did you take? 

*Algorithm.*

### Why? 

*Because it is Hash Map.*

### What is the Big O space/time for this approach?

*Time : O(1) : Because : It is constant time not dependent on the input data (n).* 

*Space : O(n) : Because : unknown number of spaces.*

## Solution

    from collections import Counter

    class Node:
        def __init__(self, value):
            self.value = value

    class HashTable:
        def __init__(self, size):
            self.size = size
            self.hash_table = self.create_buckets()
    
        def create_buckets(self):
            return [[] for _ in range(self.size)]
    
        def add(self, key, value):
            """
            # add value into hash map
            # Get the index from the key
            # using hash function
            # Get the bucket corresponding to index
            # check if the bucket has same key as
            # the key to be inserted
            # If the bucket has same key as the key to be inserted,
            # Update the key value
            # Otherwise append the new key-value pair to the bucket
            # parameters: key, value
            """ 

            hashed_key = hash(key) % self.size
            bucket = self.hash_table[hashed_key]
            found_key = False
            for index, record in enumerate(bucket):
                record_key, record_value = record
                if record_key == key:
                    found_key = True
                    break
            if found_key:
                bucket[index] = (key, value)
            else:
                bucket.append((key, value))
    
        
        def get(self, key):
            """
            # Return searched value with specific key
            # Get the index from the key using
            # hash function
            # Get the bucket corresponding to index
            # check if the bucket has same key as 
            # the key being searched
            # If the bucket has same key as the key being searched,
            # Return the value found
            # Otherwise indicate there was no record found
            # parameters: key
            """ 

            hashed_key = hash(key) % self.size
            bucket = self.hash_table[hashed_key]
            found_key = False
            for index, record in enumerate(bucket):
                record_key, record_value = record
                if record_key == key:
                    found_key = True
                    break
            if found_key:
                return record_value
            else:
                return "No record found"
    
        def __str__(self):
            return "".join(str(item) for item in self.hash_table)
    
        def tree_intersection(tree1,tree2):

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
            print(tree_intersection(tree1,tree2))

| Subject     | links |
| ----------- | ----------- |
| hashmap_tree_intersection | [hashmap_tree_intersection/hashmap_tree_intersection.py](hashmap_tree_intersection/hashmap_tree_intersection.py) |
| test_hashmap_tree_intersection | [tests/test_hashmap_tree_intersection.py](tests/test_hashmap_tree_intersection.py) |