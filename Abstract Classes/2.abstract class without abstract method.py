#Abstract class
#2. derived class of ABC (Abstract Base Class)
from abc import *
class Student(ABC):
    pass


s = Student()
print(s)
print(type(s))



#Note: Here also I am able to create an instance, because the class is
#derived from ABC but does not any abstractmethod.
