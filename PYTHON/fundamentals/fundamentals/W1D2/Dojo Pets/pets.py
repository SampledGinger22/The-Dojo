class Pet:

    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    
    def sleep(self):
        self.energy =+ 25
        print("Puppers energy is now:",self.energy)

    def eat(self):
        self.energy += 5
        self.health += 10
        print("Puppers energy is now:", self.energy, "and Health is now:", self.health)

    def play(self):
        self.health += 5
        print("Puppers Health is now:", self.health)
        
    def noise(self):
        print("Howl! Snort! Grunt! Whine!")


class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet("Spot", "corgi", "sit", 100, 100)

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

Mason = Ninja("Mason", "Britsch", "Jerky", "Kibble")

Mason.feed().walk().bathe()