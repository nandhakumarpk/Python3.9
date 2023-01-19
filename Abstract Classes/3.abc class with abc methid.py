#Abstract class
#3. class derived from ABC and having an abstractemthod
from abc import *
class Student(ABC):
  @abstractmethod
  def method1(self):
    pass



if __name__=="__main__":
  s = Student()



#TypeError: Can't instantiate abstract class Student
#with abstract methods method1
#Note: a class derived from ABC and having
#abstractmethod can not be instantiated directly
