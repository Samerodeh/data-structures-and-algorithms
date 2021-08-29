class Node:
  def __init__(self):
    self = self

input = 100
List = []

class fizzBuzzTree:
  def fizz_buzz_tree(self, k_ary_tree : 'int') -> 'List[str]':
        result = []
        if not k_ary_tree :
            return []
        for i in range(1, k_ary_tree + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

if __name__ == '__main__':
  print(f"\n{fizzBuzzTree().fizz_buzz_tree(input)}\n")
