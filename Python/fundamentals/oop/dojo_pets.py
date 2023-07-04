class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()

        return self

    def feed(self):
        self.pet.eat()

        return self

    def bathe(self):
        self.pet.noise()

        return self


class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        print('We won\'t sleep... We believe in nothing Lebowski!\n')
        self.energy += 25

        return self

    def eat(self):
        print('Scratching bath watery skin\n')
        self.energy += 5
        self.health += 10

        return self

    def play(self):
        print('Where\'s the money?\n')
        self.health += 5

    def noise(self):
        print('Where\'s the money Lebowski\n')

        return self


the_dude = Ninja('The', 'Dude', Pet('The German\'s Ferret', 'nice marmot', 'scratching skin', 10, 10),
                 'bath watered skin', 'The Dude\'s dignity and micturate on The Dude\'s rug that really ties the room together')

the_dude.walk().feed().bathe()

the_dude.pet.sleep()
