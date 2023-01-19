class Mytriangle:
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

    def isValid(self):
        a=[]
        #a+b>c
        #a+b-c>0
        #a+b(+c-c)-c>0
        a.append(self.getSide1())
        a.append(self.getSide2())
        a.append(self.getSide3())
        mx=max(a)
        res=a[0]+a[1]+a[2]-mx-mx
        if res>0:
            return True 
        else:
            return False
    
    def area(self):
        import math
        if self.isValid():
            S=(self.getSide1()+self.getSide2()+self.getSide3())/2
            a=S*((S-self.getSide1())*(S-self.getSide2())*(S-self.getSide3()))
            return math.sqrt(a)
        else:
            return("Invalid measurement")

def main():
    tri=Mytriangle()
    s1=float(input("Enter side 1\n"))
    s2=float(input("Enter side 2\n"))
    s3=float(input("Enter side 3\n"))
    tri.setSide1(s1)
    tri.setSide2(s2)
    tri.setSide3(s3)
    if tri.isValid():
        print('Area of the triangle:',tri.area())
    else:
        print("Invalid measurement")

if __name__=='__main__':
    main()
