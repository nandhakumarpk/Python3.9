class Geometry:
     
    def triangle(self):
        t=Geometry().Triangle()
        s1=float(input('Enter the side 1 of the triangle\n'))
        s2=float(input('Enter the side 2 of the triangle\n'))
        s3=float(input('Enter the side 3 of the triangle\n'))
        t.setSide1(s1)
        t.setSide2(s2)
        t.setSide3(s3)
        colour=input('Enter colour\n')
        fill=int(input("Enter 0 for empty and 1 for fill\n"))
        print(t)
        print('Area=',t.getArea())
        print('Perimeter=',t.getPerimeter())
        print('Colour is',colour)
        print("Fill: True") if fill==1 else print("False")
    

    class Triangle:
        def __init__(self):
            self.__side1=1.0
            self.__side2=1.0
            self.__side3=1.0
        
        def setSide1(self,s):
            self.__side1=s

        def setSide2(self,s):
            self.__side2=s

        def setSide3(self,s):
            self.__side3=s

        def getSide1(self):
            return self.__side1

        def getSide2(self):
            return self.__side2

        def getSide3(self):
            return self.__side3

        def getArea(self):
            import math
            S=(self.getSide1()+self.getSide2()+self.getSide3())/2
            a=S*((S-self.getSide1())*(S-self.getSide2())*(S-self.getSide3()))
            if a==0:
                return 'Invalid traingle measurement' 
            else:
                return math.sqrt(a)
        def getPerimeter(self):
            peri=self.getSide1()+self.getSide2()+self.getSide3()
            return peri

        def __str__(self):
            s='Triangle:\nside1={}\nside2={}\nside3={}'.format(self.getSide1(),self.getSide2(),self.getSide3())
            return s

def main():
    g=Geometry()
    g.triangle()

if __name__=='__main__':
    main()
