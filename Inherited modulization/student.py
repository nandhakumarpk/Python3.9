from base import Person
class Student(Person):
    def __init__(self):
        super().__init__()
        dob=' '
        cgpa=0.0

    def displayStudent(self):
        print('Name:',self.name)
        print("ID:",self.id)
        print('DOB:',self.dob)
        print("CGPA:",self.cgpa)
