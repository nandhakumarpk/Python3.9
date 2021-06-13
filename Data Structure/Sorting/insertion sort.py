def insertion_sort(arr,length):
    i=j=k=0
    for i in range(1,length):
        j=i
        while (j>0 and arr[j-1]>arr[j]):
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1

    for a in arr:
        print(a)

if __name__=='__main__':
    arr=[int(a) for a in input().split()]
    insertion_sort(arr,len(arr))
