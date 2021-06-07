#constructor Overloading
class Geometry:
    def __init__(self, length=None, breadth=None, height=None):
        self.length = length
        self.breadth = breadth
        self.height = height



    def area(self):
        #3 values: should work like volume of cuboid
        if self.length!=None and self.breadth!=None and self.height!=None:
            s = "Volume of Cuboid: {}".format(self.length * self.breadth * self.height)



        #2 values: should work like area of Rectangle
        elif self.length!=None and self.breadth!=None and self.height==None:
            s = "Area of Rectangle: {}".format(self.length * self.breadth)



        #1 value: should work like area of circle
        elif self.length!=None and self.breadth==None and self.height==None:
            import math
            s = "Area of Circle: {}".format(math.pi * self.length * self.length)
        return s

if __name__=="__main__":
    g1 = Geometry(5)
    result = g1.area()
    print(result)



    g2 = Geometry(12, 9)
    result = g2.area()
    print(result)



g3 = Geometry(12, 9, 5)
result = g3.area()
print(result)
