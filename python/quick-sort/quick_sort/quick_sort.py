def SelectionSort(arr):
    elements = len(arr)
    if elements < 1:
        return arr
    
    curr = 0 

    for i in range(1, elements):
         if arr[i] <= arr[0]:
              curr += 1
              temp = arr[i]
              arr[i] = arr[curr]
              arr[curr] = temp

    temp = arr[0]
    arr[0] = arr[curr] 
    arr[curr] = temp 
    
    left = SelectionSort(arr[0:curr])  
    right = SelectionSort(arr[curr+1:elements]) 
    arr = left + [arr[curr]] + right 

    return arr

if __name__ == '__main__':

  array = [8,4,23,42,16,15]
  print("Original Array: ",array)
  print("Sorted Array: ",SelectionSort(array))