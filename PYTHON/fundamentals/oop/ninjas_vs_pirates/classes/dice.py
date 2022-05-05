from random import random


class Dice:

    def __init__(self, highcount, lowcount=1):
        self.highcount = highcount
        self.lowcount = lowcount

D20=Dice(20)
D6=Dice(6)

def D20_roll():
    roll = random(D20.lowcount, D20.highcount)
    print(roll)
    return roll

def D6_roll():
    roll = random(D6.lowcount, D6.highcount)
    print(roll)
    return roll