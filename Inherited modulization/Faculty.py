import base
class Faculty(base.Person):
    def __init__(self):
        super().__init__()
        salary=0
        experience=0
        dpt=None
        
    def displayFaculty(self):
        print('Name:',self.name)
        print("ID:",self.id)
        print('Salary:',self.salary)
        print("Experience:",self.experience)
        print("Department:",self.dpt)
