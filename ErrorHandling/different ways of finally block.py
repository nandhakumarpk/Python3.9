#case2: there is an exception and that is handeled
try:
    print("try-block")
    print(10/0)
except ZeroDivisionError as msg:
    print("message: ", msg)
finally:
    print("This is finally-block")

#case3: there is an exception and that is not handeled
try:
    print("try-block")
    print(10/0)
except NameError:
    print("except-block")
finally:
    print("This is finally block when exception is not handled")



#Pre-defined Exceptoions vs User-defined Exceptions
