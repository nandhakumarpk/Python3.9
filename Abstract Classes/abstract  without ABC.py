#meaning of abstract class
#a class is an abstract class if it has at least on abstractmethod
#An abstract class can have abstractmethod as well as concrete method
#An abstract class can not be instantiated when created by inheriting ABC
#An abstract class must implement all its abstract method in its subclass
from abc import ABC, abstractmethod
class A:
    @abstractmethod
    def method1(self):
        print("This is an abstract method")
#concrete method
    def method2(self):
        print("This is a concrete method")
        self.method1()



#inheriting Abstract class
#must implement abstractmethod in subclass
class B(A):
    def method1(self):
        print("This implemented in B")



objA = A()
#TypeError: Can't instantiate abstract class A with abstract methods method1
objA.method1()
objA.method2()



objB = B()
objB.method1()
objB.method2()
