#meaning of abstract class
#a class is an abstract class if it has at least on abstractmethod
from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print("This is a abstract method")
    #concrete method
    def method2(self):
        print("This is a concrete method")
    #TypeError: Can't instantiate abstract class A with abstract methods method1
class B(A):
    def m1(self):
        pass
objA = B()
objA.method1()
objA.method2()

