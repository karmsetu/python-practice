from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go():
        print("go")

class Car(Vehicle):
    pass

# Objects as arguments

class MotorCycle:
    color = None

def change_color(car, color):
    car.color = color

car1 = MotorCycle()

change_color(car1, "blue")

print(car1.color)

# Duck typing: class is less imp than its method
# to be or not to be !boi

