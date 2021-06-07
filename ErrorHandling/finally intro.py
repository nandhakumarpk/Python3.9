'''
#finally Block
#1. it is prohibited to give any cleaning statement code in try-block or except-block
#Cleaning-statement code: the code for deallocating any memory, file etc.
#2. if these type of work is prohibited from try-block, except-block, then the left over block is finally-block.
#and here comes cencept of finally-block
#3. the cleaning-statement codes should be written within finally block.



#What is finally-block: it is part of exception handling which ensures to execute its block,
#irrespective of exception raised or not raised.



#finally block is not executed only in case of os._exit(0);

'''

try:
    risky code
except:
    alternate code
finally:
    cleaning statement code

