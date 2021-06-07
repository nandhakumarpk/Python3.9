import sys
arg= sys.argv
if len(arg)<2:
    print("Give a number along with the command line")
elif len(arg)>2:
    print("Give only one number")
else:
    arg=int(arg[1])
    sum=1
    for a in range(1,arg+1):
        sum*=a
    print(sum)
