class Geometry:
    def area(self, a=None, b=None, c=None):
        #3 values: should work like volume of cuboid
        if a!=None and b!=None and c!=None:
            return a*b*c



#2 values: should work like area of Rectangle
        elif a!=None and b!=None and c==None:
            return a * b



#1 value: should work like area of circle
        elif a!=None and b==None and c==None:
            import math
            return math.pi * a * a



if __name__=="__main__":
    g1 = Geometry()
    result = g1.area(5)
    print("Area of Circle: ", result)



    result = g1.area(12, 9)
    print("Area of Rectangle: ", result)



    result = g1.area(12, 9, 5)
    print("Volume of Cuboid: ", result)
