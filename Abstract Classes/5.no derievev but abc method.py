#5. class not derived from ABC but having abstractmethod with its body statements
from abc import *
class Student:
    @abstractmethod
    def method1(self):
        print("abstract method with its body statement")



if __name__=="__main__":
    s = Student()
    print(s)
    print(type(s))
