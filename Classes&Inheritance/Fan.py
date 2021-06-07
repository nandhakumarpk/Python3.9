class Fan:
    SLOW=1
    MEDIUM=2
    FAST=3
    def __init__(self):
        self.__speed=Fan.SLOW
        self.__on=False
        self.__radius=5.0
        self.__color='blue'


    def setSpeed(self,speed):
        self.__speed=speed

    def setOn(self,on):
        self.__on=on

    def setRadius(self,radius):
        self.__radius=radius

    def setColor(self,color):
        self.__color=color

    def getSpeed(self):
        return self.__speed

    def getOn(self):
        return self.__on

    def getRadius(self):
        return self.__radius

    def getColor(self):
        return self.__color

    def __str__(self):
        s='Speed:{}\nRadius:{}\nColor: {}\nOn: {}'.format(self.getSpeed(),self.getRadius(),self.getColor(),self.getOn())
        return s

def main():
    f1=Fan()
    f2=Fan()
    f1.setSpeed(Fan.FAST)
    f1.setRadius(10.0)
    f1.setColor('yellow')
    f1.setOn(True)
    f2.setSpeed(Fan.MEDIUM)
    f2.setRadius(5.0)
    f2.setColor('blue')
    f2.setOn(False)
    print(f1)
    print('\n')
    print(f2)

if __name__=='__main__':
    main()
