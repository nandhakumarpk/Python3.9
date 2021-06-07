#1. Enhance the discussed problem with neccessary Mutators and Accessors
#and also with str method
#2. Enhance the GeometricShape class design to as Square sub-class, with neccessary improved attributes.
#3. Enhance the discussed desgin with equals() method is each class
#This is Parent class
class GeometricShape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
        print("GeometricShape Construcgtor")



    def area(self):
        return 0.0



    def perimeter(self):
        return 0.0



#This is child class fo GeometricShape
class Circle(GeometricShape):



#Circle constructor extended definition
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        #self.color = color
        #self.filled = filled
        self.radius = radius
        print("Circle Constructor")

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



class Rectangle(GeometricShape):
    #overriding constructor
    def __init__(self, color, filled, length, breadth):
        super().__init__(color, filled)
        self.length = length
        self.breadth = breadth
        print("Rectangle Constructor")



#overriding methods
    def area(self):
        return self.length * self.breadth



    def perimeter(self):
        return 2 * (self.length + self.breadth)



    def __str__(self):
        s = "Color: {}, Filled: {}, Length: {}, Breadth: {}, Area: {}, Perimeter: {}".format(self.color, self.filled, self.length, self.breadth, self.area(), self.perimeter())
        return s

#main module
if __name__=="__main__":
    g1 = GeometricShape("White", True)
    #use hasattr(className/obj, attributeName)
    print("g1 has color: ", hasattr(g1, 'color'))
    print("g1 has filled: ", hasattr(g1, "filled"))
    print("g1 has area(): ", hasattr(g1, "area"))
    print("g1 has perimeter(): ", hasattr(g1, "perimeter"))



    c1 = Circle("Red", True, 12.5)
    #c1.setRadius(12.5)
    print("c1 has color: ", hasattr(c1, 'color'))
    print("c1 has filled: ", hasattr(c1, "filled"))
    print("c1 has area(): ", hasattr(c1, "area"))
    print("c1 has perimeter(): ", hasattr(c1, "perimeter"))
    print("c1 has radius: ", hasattr(c1, 'radius'))

    print("g1.area(): ", g1.area())
    print("g1.perimeter(): ", g1.perimeter())



    print("c1.area(): ", c1.area())
    print("c1.perimeter(): ", c1.perimeter())



    r1 = Rectangle("Yellow", True, 12.5, 4.5)
    print(r1)
