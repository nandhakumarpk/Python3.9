#meaning of abstract class
#a class is an abstract class if it has at least on abstractmethod
#An abstract class can have abstractmethod as well as concrete method
#An abstract class can not be instantiated when created by inheriting ABC
#An abstract class must implement all its abstract method in its subclass
from abc import ABC, abstractmethod
class A(ABC):
    def __init__(self):
        self.a=10
    @abstractmethod
    def method1(self):
        self.a=20
        print("This is an abstract method")

    def method2(self):
        print("This is a concrete method")
        self.method1()
        print(self.a)



#Inherit in class B
#must implement all abstract method in subclass



class B(A):
    def method1(self):
        print("This is overridden in B")

#main module
if __name__ == "__main__":
#create object of A
#objA = A() #Error



#create object of B
    objB = B()
    #objB.method1()
    objB.method2()
