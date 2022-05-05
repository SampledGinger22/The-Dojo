from random import random
from classes.ninja import Ninja
from classes.pirate import Pirate
from classes.dice import Dice

michelangelo = Ninja("Michelanglo")
jack_sparrow = Pirate("Jack Sparrow")
D20=Dice(20)
D6=Dice(6)


# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()


#######################################################



#######################################################

class Game:



    def __init__(self, ninjaplayer = michelangelo, pirateplayer = jack_sparrow):
        self.ninja_player = ninjaplayer
        self.pirate_player = pirateplayer
        self.dice20 = D20

    def startgame(self):
        if self.initiative_roll == "True" or "true":
            print("Rolling for who starts")
            return self.startingroll
        # else: 
        #     exit

    def startingroll(self):
        print(self.pirate_player, ":", self.D20_roll)
        print(self.ninja_player,":", self.D20_roll)

    def D20_roll(lowval,highval):
        roll = random(lowval, highval)
        print(roll)

    def D6_roll():
        roll = random(D6.lowcount, D6.highcount)
        print(roll)

    initiative_roll = input("Start Scenario? True or False: ")
    print("Start Game is: " + initiative_roll)
    if initiative_roll == "True" or "true":
        print("Rolling for who starts!! ") and D20_roll(1,20)
        


