open_list = ["[","{","("]
close_list = ["]","}",")"]

def validate_brackets(string):
    stack = []
    for i in string:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

if __name__ == '__main__':

 string = "{[]{()}}"
 print(string,"-", validate_brackets(string))
  
 string = "[{}{})(]"
 print(string,"-", validate_brackets(string))
  
 string = "((()"
 print(string,"-",validate_brackets(string))