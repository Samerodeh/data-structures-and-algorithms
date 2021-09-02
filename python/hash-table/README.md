# Hashtables

> What is a Hashtable? (Links to an external site.)

* Hash :

**A hash is the result of some algorithm taking an incoming string and converting it into a value that could be used for either security or some other purpose. In the case of a hashtable, it is used to determine the index of the array.**

* Buckets :

**A bucket is what is contained in each index of the array of the hashtable. Each index is a bucket. An index could potentially contain multiple key/value pairs if a collision occurs.**

* Collisions :

**A collision is what happens when more than one key gets hashed to the same location of the hashtable.**

## Challenge

### Features

> Implement a Hashtable Class with the following methods:

* add

1. Arguments: key, value
2. Returns: nothing
3. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

* get

1. Arguments: key
2. Returns: Value associated with that key in the table

* contains

1. Arguments: key
2. Returns: Boolean, indicating if the key exists in the table already.

* hash

1. Arguments: key
2. Returns: Index in the collection for that key

## Approach & Efficiency

### What approach did you take? 

**Algorithm**

### Why? 

**Because : Its a Hash Table**

### What is the Big O space/time for this approach?

**Time : O(1) : Because : searching for the element takes the same amount of time as searching for the first element of an array**

**Space : O(n) : Because : Number of spaces unknown**

| Subject     | links |
| ----------- | ----------- |
| hash_table| [hash_table/hash_table.py](hash_table/hash_table.py) |
| test_hash_table | [tests/test_hash_table.py](tests/test_hash_table.py) |