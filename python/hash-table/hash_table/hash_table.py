class HashTable :
  def __init__(self, size = 1024):
    self.size = size
    self._buckets = [None] *self.size

  def add(self,key,value):
    """
    Add a value to our array by its key 

    parameters:
         key, value
    """
    index = self.hash(key)

    if not self._buckets[index]:
      self._buckets[index]=[[key,value]]
    else:
      self._buckets[index].append([key,value])

  def get(self,key):
    """
    Get value by key 

    parameters:
        key

    return: 
       the value 
      """
    index = self.hash[key]
    return index
    
  def contains(self,key):
    """
    Check if the value in key exist

    parameters:
        key

    return: 
        a boolean
    """
    index = self.hash(key)

    if self._buckets[index]:
      return self._buckets[index].includes(key)
    else:
      return False

  def hash(self,key:str)->int:
    """
    Get the indix of our array for a specific string key  

    parameters:
        key: a string
    """
    value=0

    for x in key:
      value += ord(x)
    index = (value * 7) % self.size   
    return index