class cuboid:
    def __init__(self):
        self.a=float(input())
        self.b=float(input())
        self.c=float(input())

    def volume(self):
        print(self.a*self.b*self.c)

    def sur(self):
        sum=2*((self.a*self.b)+(self.b*self.b)+(self.c*self.a))
        print(sum)

cube=cuboid()
cube.volume()
cube.sur()
