#meaning of abstract class
#a class is an abstract class if it has at least on abstractmethod
from abc import abstractmethod
class A:
    @abstractmethod
    def method1(self):
        pass



objA = A() #Allowed to create object
