import re

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

def repeated_word(sentence = None):
    if sentence == None :
        return 'the sentence is empty'

    hash_table = Hashtable(1024)
    sentence = re.sub('\W+', ' ', sentence).lower().split()

    for word in sentence:
        if hash_table.contains(word):
            return word
        else:
            hash_table.add(word, True)

if __name__ == "__main__":

  sentence = "Once upon a time, there was a brave princess who..."
  print(repeated_word(sentence))

  sentence = "it was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
  print(repeated_word(sentence))

  sentence = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..." 
  print(repeated_word(sentence))    