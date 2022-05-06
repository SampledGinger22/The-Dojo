from random import randint
from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")
jack_sparrow = Pirate("Jack Sparrow")


# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()


#######################################################



#######################################################

class Game:

    def __init__(self, ninja, pirate):
        self.pirate = pirate
        self.ninja = ninja

    def startingroll(self, pirate_player, ninja_player):
        print(pirate_player, ":", self.D_roll(1,20))
        print(ninja_player,":", self.D_roll(1,20))

    def D_roll(lowval,highval):
        return(randint(lowval,highval))

initiative_roll = input("Start Scenario? True or False: ")
if initiative_roll == "True" or "true":
    print("Rolling for who starts!! ")
Game.startingroll(Game, michelangelo.name, jack_sparrow.name)
    


