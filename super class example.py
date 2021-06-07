class Parent:
    a=10
    def __init__(self):
        self.b=20
        print("Parent constructor")
    def m1(self):
        print("Instance Parent")
    @staticmethod
    def m2():
        print("Static Parent")
    @classmethod
    def m3(cls):
        print('Class method')

class Child(Parent):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
        print("\n\n\n")

    def method1(self):
        super().__init__()
        super().m1()
        super().m2()
        print("Instance member",self.b)
        print("Static method",super().a)
        super().m3()



if __name__=='__main__':
    c=Child()
    c.method1()
