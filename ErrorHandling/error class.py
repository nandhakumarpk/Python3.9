#Generally in programming language we get two types of problems
#1. Syntanx Error
#2. Run Time Error also calle Exception
#Example of Syntax Error
if 10 % 2 == 0
    print("Even")
else:
    print("Odd")



#Example of Run Time Error
print(10/0)
#ZeroDivisionError: division by zero



print(10/'two')
#TypeError: unsupported operand type(s) for /: 'int' and 'str'



x = int(input("Enter a Number: "))
#ValueError: invalid literal for int() with base 10: 'ten'
