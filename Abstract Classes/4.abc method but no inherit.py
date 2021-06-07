#Abstract class
#4. class not derived from ABC but having abstractmethod
from abc import *
class Student:
@abstractmethod
def method1(self):
pass



if __name__== "__main__":
s = Student()
print(s)
print(type(s))



#Note: here also we are able to create object because, class is not derived from ABC
