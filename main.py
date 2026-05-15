import random


class Dice:
    def roll(self):
        selection = (random.randint(1,6), random.randint(1,6))
        return selection
    
    
dice1= Dice()
print(dice1.roll())