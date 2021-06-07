'''
Important point the note
2. We should keep try-block as small as possible
3. Exception may occur in except-block or finally-block.
In this situation there is not way to handle exception and
program terminates abnormally.
'''

#How to print message from excetion object
try:
    print(10/0)
except ZeroDivisionError as msg:
    print("Exception raised and its description is: ", msg)
finally:
    print('Over')

