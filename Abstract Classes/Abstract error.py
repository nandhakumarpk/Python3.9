#meaning of abstract class
#a class is an abstract class if it has at least on abstractmethod
from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass



objA = A()
#TypeError: Can't instantiate abstract class A with abstract methods method1
