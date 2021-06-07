#We can have multiple exceptions raised
#each exceptions should be in seperate except-blocks
'''
try:
state1
state2
state3
except Exception1:
alternate state
except Exception2:
alternate state
state4



'''
try:

    x = int(input("Enter number: "))
    y = int(input("Enter number: "))
    print(x/y)
except ZeroDivisionError:
    print("Can not divide by zero")
    print(10/2)
except ValueError:
    print("Enter valid inputs")
    x = 10


finally:
    print("x value: ", x)




#Note: if multiple except blocks are available then
#based on raised exception the corresponding block will be executed.
