class Shape:
    def __init__(self):
        self.colour=None
        self.fill=False
        print("000")

    def setColour(self,colour):
        self.colour=colour

    def setFilled(self,fill):
        self.filled=fill

    def getColour(self):
        return self.colour
    
    def getFill(self):
        return self.fill
    
class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.radius=0.0

    def addRadius(self):
        self.radius=10.0
    
    def setRadius(self,r=10.0):#mutators
        self.radius=r
    def getRadius(self):#accessors
        return self.radius
    

    def area(self):
        import math
        return math.pi*(self.radius**2)
    def perimeter(self):
        import math
        return 2*math.pi*self.radius
def main():
    c1=Circle()
    print("Radoius:",c1.radius)
    print('Colour:',c1.colour)
    '''c1.addRadius()
    print('Area:{}'.format(c1.area()))
    c1.setRadius(10.0)
    print('Perimeter:',c1.perimeter())
    c1.setColour("Blue")
    c1.fill=True
    print('Colour:',c1.getColour())
    print('Fill:',c1.getFill())
    c=Circle()
    c.setRadius(25)
    print("Area",c.area())
    print("Perimeter",c.perimeter())'''

if __name__=='__main__':
    main()
