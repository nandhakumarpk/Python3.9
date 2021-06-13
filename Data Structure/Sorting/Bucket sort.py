# Python3 program to sort an array
# using bucket sort
def insertionSort(b):
    for i in range(1, len(b)):
        j=i
        while (j>0 and b[j-1]>b[j]):
            b[j-1],b[j]=b[j],b[j-1]
            j-=1
            
    return b    
             
def bucketSort(x):
    arr = []
    slot_num = 10 # 10 means 10 slots, each
                  # slot's size is 0.1
    for i in range(slot_num):
        arr.append([])
         
    # Put array elements in different buckets
    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)
     
    # Sort individual buckets
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])
         
    # concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x
 
# Driver Code
x = []
[x.append(float(a) for a in input().split()]
print("Sorted Array is")
print(bucketSort(x))
