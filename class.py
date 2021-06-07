class cal:
    def __init__(self,x,y):
        self.a=x
        self.b=y

    def add(self):
        print(self.a+self.b)

    def sub(self):
        print(self.a-self.b)

a=int(input())
b=int(input())
c1=cal(x,y)
c1.add()
c1.sub()
