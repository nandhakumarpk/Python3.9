#General Risky statement is kept withing outer try-block, specific or too much Risky statement should be ketp in inner try-block.
#General Risky statement: So abvious statement
#too much risky: which is very specific as per the exception poit of view



#the Exception raised in inner try-block should be handeled by inner except-block



#if not handeled by the inner except block then, will be handeled by outer-except-block



try:
    print("Outer try block")
    try:
        print("Inner try block")
        print(10/0)
    except ZeroDivisionError:
        print("Can not divide by zero")
        print(10/2)
    finally:
        print("Inner Finally block")
except:
    print("Outer except block")
finally:
    print("Outer finally block")
