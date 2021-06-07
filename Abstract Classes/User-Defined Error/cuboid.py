class CuboidSizeError(Exception):
    pass

class Cuboid:
    def __init__(self):
        self.__x=0
        self.__y=0
        self.__z=0

    def setside1(self,x):
        if x<=0:
            raise CuboidSizeError("Invalid measurement")
        else:
            self.__x=x
    def setside2(self,y):
        if y<=0:
            raise CuboidSizeError("Invalid measurement")
        else:
            self.__y=y
    def setside3(self,z):
        if z<=0:
            raise CuboidSizeError("Invalid measurement")
        else:
            self.__z=z
    def getside1(self):
        return self.__x
    def getside2(self):
        return self.__y
    def getside3(self):
        return self.__z
    def volume(self):
        return ((self.getside1())*(self.getside2()*self.getside3()))

if __name__=='__main__':
    c=Cuboid()
    c.setside1(float(input("Enter the side1: ")))
    c.setside2(float(input("Enter the side2: ")))
    c.setside3(float(input("Enter the side3: ")))
    print("Volume of the cuboid is:",c.volume())
