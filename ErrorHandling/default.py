#default except-block: used to handle any type of exceptions
try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    print(x/y)

except ZeroDivisionError:
    print("can not divide by zero")

except:
    print("Defualt Exception Occurred")
    print("Welcome to Python")
