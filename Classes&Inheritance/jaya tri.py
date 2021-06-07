class triangle:
    def __init__(self):
        self.side1=0
        self.side2=0
        self.side3=0
    def SetSide1(self,a):
        self.side1=a
    def SetSide2(self,b):
        self.side2=b
    def SetSide3(self,c):
        self.side3=c
    def getside1(self):
        return self.side1
    def getside2(self):
        return self.side2
    def getside3(self):
        return self.side3
    def Area(self):
        import math
        from math import sqrt
        s=(self.side1+self.side2+self.side3)/2
        return math.sqrt(s*(s-self.side1)*(s-self.side2)*(s-self.side3))
    def isValid(self):
        count=0
        if self.side1+self.side2>self.side3:
            count=count+1
        if self.side2+self.side3>self.side1:
            count=count+1
        if self.side1+self.side3>self.side2:
            count=count+1
        if count==3:
            print("valid")
   
obj=triangle()
obj.SetSide1(3)
obj.SetSide2(4)
obj.SetSide3(5)
print(obj.Area())
obj.isValid()
