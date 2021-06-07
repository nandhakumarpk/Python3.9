'''Important point the note
1. If exception occurs within try-block anywhere then the rest of the
statements will not execute. We should only keep
risky-statement inside try-block.
#this is wrong way'''
try:
    print("Hello")
    print(10/0)
    print("Welcome to python")
except ZeroDivisionError:
    print(10/2)



#Correct way
print("Hello")
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
print("Welcome to Python")
#Note: in case of multiple except blocks the
#order of these blocks must follow its heirarchy.
