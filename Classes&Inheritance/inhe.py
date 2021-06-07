class A:
    def __init__(self):
        self.A=0
class B:
    def __init__(self):
        self.B=1

class C(A,B):
    def __init__(self):
        super().__init__()
        B.__init__(self)

c=C()
print(c.A)
print(c.B)
print(c)
