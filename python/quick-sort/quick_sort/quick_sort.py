def Partition(arr, left, right):
    i = (left-1)        
    pivot = arr[right]     
  
    for j in range(left, right):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[right] = arr[right], arr[i+1]
    return (i+1)
  
def QuickSort(arr, left, right):
    if len(arr) == 1:
        return arr

    if left < right:
        p = Partition(arr, left, right)

        QuickSort(arr, left, p-1)
        QuickSort(arr, p+1, right)

if __name__ == '__main__':

  arr = [8, 4, 23, 42, 16, 15]
  n = len(arr)
  QuickSort(arr, 0, n-1)
  print("Sorted array :")
  print(arr)