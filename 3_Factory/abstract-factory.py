from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print("This tea is nice but I'd prefer it with milk")


class Coffee(HotDrink):
    def consume(self):
        print("This coffee is delicious")


# First way with abstract class
# ---------------------------------------------------------------------
# Abstract class to factory HotDrinks.
class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Put in tea bag, boil water, pour {amount}ml, enjoy!")
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Grind some beans, boil water, pour {amount}ml, enjoy!")
        return Coffee()


def make_drink(type):
    if type == "tea":
        return TeaFactory().prepare(200)
    elif type == "coffee":
        return CoffeeFactory().prepare(50)
    else:
        return None


# ---------------------------------------------------------------------


# Second way
# ---------------------------------------------------------------------

"""Specifying abstract classes is a good idea because we explicitly specify which API we want to implement.
Also in other strongly typed languages an abstract class is needed for a factory there"""


# class TeaFactory:
#     def prepare(self, amount):
#         print(f"Put in tea bag, boil water, pour {amount}ml, enjoy!")
#         return Tea()


# class CoffeeFactory:
#     def prepare(self, amount):
#         print(f"Grind some beans, boil water, pour {amount}ml, enjoy!")
#         return Coffee()


class HotDrinkMachine:
    class AvailableDrink(Enum):  # violates OCP
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + "Factory"
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print("Available drinks:")
        for f in self.factories:
            print(f[0])

        s = input(f"Please pick drink (0-{len(self.factories)-1}): ")
        idx = int(s)
        s = input("Specify amount: ")
        amount = int(s)
        return self.factories[idx][1].prepare(amount)


# ---------------------------------------------------------------------


if __name__ == "__main__":
    # entry = input("What kind of drink would you like? Tea or coffee? ")
    # drink = make_drink(entry)
    # drink.consume()

    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()
