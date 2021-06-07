def printIt(size):
    print()
    for i in range(size//2,size+1,2):
        for j in range(1,size-i,2):
            print(end=" ")
        for j in range(1,i+1):
            print(end="*")
        for j in range(1,size-i+1):
            print(end=" ")
        for j in range(1,i+1):
            print(end="*")
        print()
    for i in range(size,0,-1):
        for j in range(i,size):
            print(end=" ")
        for j in range(1,(i*2)):
            print(end="*")
        print()
