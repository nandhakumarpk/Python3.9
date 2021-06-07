#A complete Example of an Interface in Python
from abc import *
#define interface Arithmetic
class Arithmetic(ABC):
    @abstractmethod
    def sum2Num(self, a, b):
        pass



    @abstractmethod
    def sum3Num(self, a, b, c):
        pass




#define class NumberArithmetic
class NumberArithmetic(Arithmetic):
    def sum2Num(self, a, b):
        return a + b



    def sum3Num(self, a, b, c):
        return a + b + c



#define class stringArithmetic
class StringArithmetic(Arithmetic):
    def sum2Num(self, a, b):
        return a + b



    def sum3Num(self, a, b, c):
        return a + b + c



#define class ComplexArithmetic
class ComplexArithemetic(Arithmetic):
    def sum2Num(self, a, b):
        real = a.real + b.real
        imag = a.imag + b.imag
        c = complex(real, imag)
        return c



    def sum3Num(self, a, b, c):
        real = a.real + b.real + c.real
        imag = a.imag + b.imag + c.imag
        c = complex(real, imag)
        return c



#main module
if __name__=="__main__":
    #create object of Arithmetic (Interface)
    #obj = Arithmetic()



    #create object of NumberArithmetic (derived class)
    obj = NumberArithmetic()
    print("obj.sum2Num(12, 15): ", obj.sum2Num(12, 15))
    print("obj.sum3Num(12, 15, 20): ", obj.sum3Num(12, 15, 20))



    #create object of StringArithmetic (derived class)
    obj = StringArithmetic()
    print("obj.sum2Num('Learning', 'Python'): ",
          obj.sum2Num('Learning', 'Python'))
    print("obj.sum3Num('Welcome', 'to', 'Python'): ",
          obj.sum3Num('Welcome', 'to', 'Python'))



    #create object of StringArithmetic (derived class)
    c1 = complex(4, 7)
    c2 = complex(12, 15)
    c3 = complex(100, 200)
    obj = StringArithmetic()
    print("obj.sum2Num(c1, c2): ", obj.sum2Num(c1, c2))
    print("obj.sum3Num(c1, c2, c3): ", obj.sum3Num(c1, c2, c3))
