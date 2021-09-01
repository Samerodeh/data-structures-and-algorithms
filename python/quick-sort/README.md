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

**Space: O(1) : Because : No need to additional space.**

## Solution

    def quick_sort(arr, left, right):
    if left < right:
        position = partition(arr, left, right)
        quick_sort(arr, left, position - 1)
        quick_sort(arr, position + 1, right)

    def partition(arr, left, right):
    pivot = arr[right]
    low = left - 1

    for i in range(left, right):
        if arr[i] <= pivot:
            low += 1
            swap(arr, i, low)

    swap(arr, right, low + 1)
    return low + 1

    def swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp

    if __name__ == '__main__':

    arr = [8,4,23,42,16,15]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)

| Subject     | links |
| ----------- | ----------- |
| quick_sort | [quick_sort/quick_sort.py](quick_sort/quick_sort.py) |
| test_quick_sort | [tests/test_quick_sort.py](tests/test_quick_sort.py) |
| BLOG | [BLOG.md](BLOG.md) |