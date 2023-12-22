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

# multilevel inheritence:= when child class inherits from parent
class Organism:
    alive =True

class Cell(Organism):
    def eat(self):
        print("cell is eating")
        return self

class SingleCell(Cell):
    def __init__(self, type):
        self.type = type
    def move(self):
        print("cell is moving")
        return self

class MultipleCell(SingleCell):
    def __init__(self, noCell, type):
        self.noCell = noCell
        super().__init__(type)
    def sibling(self):
        print("it has certain no. og siblings")
        return self
    def cellStrucInfo(self):
        print("the cell structure has {} of {} cells".format(self.noCell, self.type))


human = MultipleCell("a lot", "prokaryotic")
human.eat().sibling().cellStrucInfo()

# Super function: return temp object

#abstract class: prevent a user from creating an object of that class
