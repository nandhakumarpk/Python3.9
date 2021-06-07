#if abstract class having only abstractmethods without its body definition the
#this type of abstract class is called Interface in python.
#Example of Interface
from abc import *
class Student(ABC):
    @abstractmethod
    def method1(self):
        pass



    @abstractmethod
    def method2(self):
        pass
