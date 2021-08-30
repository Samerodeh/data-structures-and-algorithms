def mergeSort(arr):
    if len(arr) > 1:

        mid = len(arr)//2

        left = arr[:mid]

        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)
        Merge(left, right, arr)

def Merge(left, right, arr):

        i = 0
        j = 0 
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

if __name__ == '__main__':
    arr = [8,4,23,42,16,15]
    print("Given array is :")
    print(arr)
    mergeSort(arr)
    print("Sorted array is :")
    print(arr)