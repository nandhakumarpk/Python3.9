class Duck:
    def talk(self):
        print("Quack..Quack...")



class Dog:
    def bark(self):
        print("Bhaow...Bhaow...")



class Cat:
    def talk(self):
        print("Meown...Meown...")



class Goat:
    def talk(self):
        print("Myaah...myaah...")



class Lion:
    def bark(self):
        print("Raor...Roar...")




def tellToSpeak(obj):
    if hasattr(obj, 'talk') == True:
        obj.talk()
    else:
        obj.bark()



#main module
if __name__ == "__main__":
    duck = Duck()
    dog = Dog()
    cat = Cat()
    goat = Goat()
    lion = Lion()



    list1 = [duck, dog, cat, goat, lion]
    for obj in list1:
        tellToSpeak(obj)
