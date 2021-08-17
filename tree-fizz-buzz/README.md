# Challenge Summary

* Write a function called fizz buzz tree
* Arguments: k-ary tree
* Return: new k-ary tree

**Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:**

* If the value is divisible by 3, replace the value with “Fizz”
* If the value is divisible by 5, replace the value with “Buzz”
* If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
* If the value is not divisible by 3 or 5, simply turn the number into a String.

## Whiteboard Process

![Whiteboard Process](asset/tree-fizz-buzz.png)

## Approach & Efficiency

> What approach did you take ?

**Algorithm**

> Why ? 

**Because it is fizz buzz tree** 

> What is the Big O space/time for this approach ?

**Time : O(n) Because : n is the number of nodes in the tree**

**Space : O(n) Because : spaces number unknown**

## Solution

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

| Subject     | links |
| ----------- | ----------- |
| tree_fizz_buzz | [tree_fizz_buzz/tree_fizz_buzz.py](tree_fizz_buzz/tree_fizz_buzz.py) |
| test_tree_fizz_buzz | [tests/test_tree_fizz_buzz.py](tests/test_tree_fizz_buzz.py) |
