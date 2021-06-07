def isprime(a):
    for b in range(2,(a//2)+1):
        if a%b==0: return False
    return True



import sys
ar=sys.argv
if len(ar)!=3:
    print("Enter 2 arguments ony")
else:
    ar=ar[1:]
    ar[0]=int(ar[0])
    ar[1]=int(ar[1])
    for a in range(ar[0],ar[1]+1):
        if (isprime(a)): print(a)
