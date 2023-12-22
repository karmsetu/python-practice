from typing import Self


class Animal:
    alive = True
    livingLoc = "land" # class variables
    def __init__(self, name, food):
        self.name = name # instance variable
        self.food = food # instance variable
    def intro(self):
        print("this animals name is", self.name)
    def eat(self):
        print(self.name,"eats",self.food)

class Amphibian(Animal):
    livingLoc = "water"
    def swim(self):
        print(self.name+" is swimming")
    pass

horse = Animal("Horse", "grass")
horse.intro()
horse.eat()

crocodile = Amphibian('crocodile',"meat")
# crocodile.livingLoc = "amphibian"
print(crocodile.livingLoc, horse.livingLoc)
crocodile.swim()