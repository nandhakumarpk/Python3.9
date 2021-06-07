#We can have multiple Exceptions within single except-block
'''
Syntax:



except (Exception1, Exception2, Exception3,...)
or
except (Exception1, Exception2, Exception3,...) as msg
'''



try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    print(x/y)
except (ZeroDivisionError, ValueError) as msg:
    print("Exception Occurred, the description is: ", msg)
