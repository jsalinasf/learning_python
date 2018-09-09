# Exercise 9.14 - DICE

from random import randint

class Dice():
    """ An Attempt to define a Dice with any sides"""

    def __init__(self, number_sides=6):
        self.sides = number_sides

    def roll_dice(self):
        x = randint(1, self.sides)
        return x

sides = ""
sides = input("How many sides will your Dice have (leave blank for 6): ")
if len(sides) > 0:
    dice01 = Dice(int(sides))
else:
    dice01 = Dice()

for i in range(1, 10):
    print("Intento {}: {}".format(i, dice01.roll_dice()))
