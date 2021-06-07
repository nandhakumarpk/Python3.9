#Note: When a class is derived from ABC and having an abstractmethod,
#its object can't be created.



#the abstractmethod definition of an Abstract class
#should be defined in it child class



from abc import *
class Student(ABC):
    @abstractmethod
    def method1(self):
        pass



#if the class class is not given abstract
#method definition then the child class is also an abstract class.
#meaning even for child class object can not be created.
class StudentDerived(Student):
    pass



if __name__=="__main__":
    s = StudentDerived()



#TypeError: Can't instantiate abstract class StudentDerived with
#abstract methods method1
