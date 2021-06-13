def shellsort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2

arr=[5,3,9,7,85,12,455,65]
print("Before sorting",arr)
shellsort(arr)
print(arr)
