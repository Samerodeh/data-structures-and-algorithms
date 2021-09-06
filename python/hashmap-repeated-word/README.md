# Challenge Summary

### Feature Tasks

* Write a function called repeated word that finds the first word to occur more than once in a string
* Arguments: string
* Return: string


## Whiteboard Process

![Whiteboard Process](asset/hashmap-repeated-word.png)

## Approach & Efficiency

### What approach did you take? 

*Algorithm.*

### Why? 

*Because it is Hashmap.*

### What is the Big O space/time for this approach?

*Time : O(n) : Because : Instead of counting a number of occurrences of each word which will have O(N) time and space complexity, where N is number of words, we can stop when the count of any word becomes 2. That is no need to iterate through all the words in string.*

*Space : O(n) : Because : Instead of counting a number of occurrences of each word which will have O(N) time and space complexity, where N is number of words, we can stop when the count of any word becomes 2. That is no need to iterate through all the words in string.*

## Solution

    from collections import Counter

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

    def repeated_word(string):
        lis = list(string.split(" "))
        word = Counter(lis)
        for i in lis:
            if(word[i] > 1):
                return i
            else:
            if(word[i] < 1):
            return None
    
    if __name__ == '__main__':

    sentence = "Once upon a time, there was a brave princess who..."
    print(repeated_word(sentence))

    sentence = "it was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    print(repeated_word(sentence))

    sentence = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..." 
    print(repeated_word(sentence))

| Subject     | links |
| ----------- | ----------- |
| hashmap_repeated_word | [hashmap_repeated_word/hashmap_repeated_word.py](hashmap_repeated_word/hashmap_repeated_word.py) |
| test_hashmap_repeated_word | [tests/test_hashmap_repeated_word.py](tests/test_hashmap_repeated_word.py) |