#1. Enhance the discussed problem with neccessary Mutators and Accessors
#and also with str method
#2. Enhance the GeometricShape class design to as Square sub-class, with neccessary improved attributes.
#3. Enhance the discussed desgin with equals() method is each class
#This is Parent class
class GeometricShape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
        #print("GeometricShape Constructor")
        
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
        #print("Circle Constructor")

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
        
    def getRadius(self):
        return self.radius
    
    def getColor(self):
        return self.color
    
    def getFilled(self):
        return self.filled
    
    def __eq__(self,other):
        if self.area==other.area:
            return True
        else:
            return False
    def __str__(self):
        s = "Circle attributes\nColor: {}\nFilled: {}\nRadius: {}\nArea: {}\nPerimeter: {}".format(self.getColor(), self.getFilled(), self.getRadius(), self.area(), self.perimeter())
        return s
    
class Rectangle(GeometricShape):
    #overriding constructor
    def __init__(self, color, filled, length, breadth):
        super().__init__(color, filled)
        self.length = length
        self.breadth = breadth
        #print("Rectangle Constructor")
        
    def setLength(self,l):
        self.length=l
        
    def setBreadth(self,b):
        self.breadth=b
        
    def getLength(self):
        return self.length
    
    def getRadius(self):
        return self.breadth
    
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
    def __eq__(self,other):
        if self.area==other.area:
            return True
        else:
            return False
    def __str__(self):
        s = "Rectangle attributes\nColor: {}\nFilled: {}\nLength: {}\nBreadth: {}\nArea: {}\nPerimeter: {}".format(self.color, self.filled, self.length, self.breadth, self.area(), self.perimeter())
        return s
class Square():
    def __init__(self,color,filled,side):
        GeometricShape.__init__(self,color,filled)
        self.side=side
        #print("Square constructor")
        
    def setSide(self):
        self.side=side
        
    def getSide(self):
        return self.side
    
    def area(self):
        return self.side**2

    def perimeter(self):
        return 4*self.side
    
    def __eq__(self,other):
        if self.area==other.area:
            return True
        else:
            return False
        
    def __str__(self):
        s = "Sqare attributes\nColor: {}\nFilled: {}\nSide: {}\nArea: {}\nPerimeter: {}".format(self.color, self.filled, self.side, self.area(), self.perimeter())
        return s
#main module
if __name__=="__main__":
    s1=Square('White',True,10)
    s2=Square('White',True,10)
    s1.area()
    s1.perimeter()
    s2.area()
    s2.perimeter()
    s3=Square('Blue',True,10)
    s3.area()
    s3.perimeter()
    print(s1)
    print('\n\n\n')
    print(s2)
    print('\n\n\n')
    print(s3)
    print('\n\n\n')
    print("s1==s2:",s1==s2)
    print("s2==s3:",s2==s3)
    print('\n\n\n')
    r1=Rectangle('RED',True,10,5)
    r1.area()
    r1.perimeter()
    r2=Rectangle("Red",True,10,5)
    r2.area()
    r2.perimeter()
    
    print(r1)
    print('\n\n\n')
    print(r2)
    print("r1==r2:",r1==r2)
    print('\n\n\n')
    c1=Circle("Yellove",False,12)
    c2=Circle("Yellove",False,12)
    c1.perimeter()
    c2.perimeter()
    c1.area()
    c2.area()
    print(c1)
    print('\n\n\n')
    print(c2)
    print('\n\n\n')
    print('c1==c2',c1==c2)
    
