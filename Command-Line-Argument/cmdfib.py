import sys
ar=sys.argv
if len(ar)!=2:
    print("Enter one argument only")
else:
    ar=int(ar[1])
    fib={}
    fib[0]=0
    fib[1]=1
    for i in range(2,ar):
        fib[i]=fib[i-2]+fib[i-1]
    print(fib[ar-1])

#printed fib[ar-1] since 1 element in fibnocci series is so if 10 is the output we need to calculate only upto fib[9] and then print fib[9]
