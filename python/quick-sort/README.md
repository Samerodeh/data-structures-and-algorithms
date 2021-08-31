# Challenge Summary

**Given array have random input, then sorted it using Quick Sort.**

## Whiteboard Process

![Whiteboard Process](asset/quick_sort.png)

## Approach & Efficiency

> What approach did you take ? 

**Algorithm**

> Why ? 

**Because it is Quick Sort**

> What is the Big O space/time for this approach ?

**Time: O(n^2) : Because : The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times…concluding the algorithm to be n squared.**

**Space: O(1) : Because : No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).**

## Solution

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

| Subject     | links |
| ----------- | ----------- |
| quick_sort | [quick_sort/quick_sort.py](quick_sort/quick_sort.py) |
| test_quick_sort | [tests/test_quick_sort.py](tests/test_quick_sort.py) |
| BLOG | [BLOG.md](BLOG.md) |