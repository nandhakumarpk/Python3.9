class student:
    def __init__(self):
        self.name=input("Name:\n")
        #self.id=int(input("ID:\n"))
        #self.phno=int(input("Phone number:\n"))
        #self.email=input("Email:\n")

    def display(self):
        print(self.name)
        #print(self.id)
        #print(self.phno)
        #print(self.email)

'''s1=student()
s2=student()
s3=student()
s4=student()
s5=student()


s1.display()
s2.display()
s3.display()
s4.display()
s5.display()'''
s=[]
s=[0 for a in range(5)]
for a in range(0,5):
    s[a]=student()

for a in range(5):
    s[a].display()
