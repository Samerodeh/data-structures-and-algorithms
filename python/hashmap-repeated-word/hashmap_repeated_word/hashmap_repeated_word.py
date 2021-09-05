from collections import Counter

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