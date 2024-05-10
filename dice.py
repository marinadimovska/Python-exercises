import random

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second #python prints tuple

dice = Dice() #object
print(dice.roll())
