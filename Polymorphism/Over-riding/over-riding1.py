#This is Parent class
class GeometricShape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled



    def area(self):
        return 0.0



    def perimeter(self):
        return 0.0



#This is child class fo GeometricShape
class Circle(GeometricShape):
    #method overriding of area
    def area(self):
        import math
        a = math.pi * self.radius * self.radius
        return a



    def perimeter(self):
        import math
        p = 2 * math.pi * self.radius
        return p



    def setRadius(self, radius):
        self.radius = radius



#main module
if __name__=="__main__":
    g1 = GeometricShape("White", True)
    #use hasattr(className/obj, attributeName)
    print("g1 has color: ", hasattr(g1, 'color'))
    print("g1 has filled: ", hasattr(g1, "filled"))
    print("g1 has area(): ", hasattr(g1, "area"))
    print("g1 has perimeter(): ", hasattr(g1, "perimeter"))



    c1 = Circle("Red", True)
    c1.setRadius(12.5)
    print("c1 has color: ", hasattr(c1, 'color'))
    print("c1 has filled: ", hasattr(c1, "filled"))
    print("c1 has area(): ", hasattr(c1, "area"))
    print("c1 has perimeter(): ", hasattr(c1, "perimeter"))
    print("c1 has radius: ", hasattr(c1, 'radius'))

    print("g1.area(): ", g1.area())
    print("g1.perimeter(): ", g1.perimeter())



    print("c1.area(): ", c1.area())
    print("c1.perimeter(): ", c1.perimeter())




    #overriding is also called dynamic binding of dynamic polymorphism
    g1.area()
    c1.area()



    g1.perimeter()
    c1.perimeter()




    '''#overloading is also called static binding or static polymorphism
    area(12.5) #area of circle
    area(12.5, 4.5) #area of Rectangle
    area(12.5, 4.5, 8.0) #area of Cuboid'''
