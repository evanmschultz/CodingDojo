# Animal class
class Animal:
    def __init__(self, name, age, health=50, happiness=50):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        print(
            f'{self.__class__.__name__}: {self.name}, Age: {self.age}, Health: {self.health}, Happiness: {self.happiness}')
        return self

    def feed(self):
        self.health += 10
        self.happiness += 10
        return self


# Animal child classes
class Toucan(Animal):
    def __init__(self, name, age, health=70, happiness=60):
        super().__init__(name, age, health, happiness)

    def bray(self):
        print(f'{self.name} is braying. It sounds like a donkey!')
        return self


class Lion(Animal):
    def __init__(self, name, age, health=60, happiness=40):
        super().__init__(name, age, health, happiness)

    def roar(self):
        print(f'{self.name} is roaring... We get it, you\'re impressive!')
        return self

    def feed(self):
        self.health += 15
        self.happiness += 10
        return self


class Tiger(Animal):
    def __init__(self, name, age, health=70, happiness=30):
        super().__init__(name, age, health, happiness)

    def feed(self):
        self.health += 20
        self.happiness += 20

    def mark_territory(self):
        print(f'{self.name}, come one there are children here!')
        return self


class Bear(Animal):
    def __init__(self, name, age, health=80, happiness=20):
        super().__init__(name, age, health, happiness)

    def scratch_back(self):
        self.happiness += 2
        print(f'{self.name} is scratching its back... Hedonist!')
        return self

    def feed(self):
        self.health += 25
        self.health += 20
        return self


# Zoo class with name attribute and animals list attribute
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        return self

    def display_all_animals(self):
        for animal in self.animals:
            animal.display_info()
        return self

    def feed_animals(self):
        for animal in self.animals:
            animal.feed()
        return self


# run tests only if running this file directly, not if imported
if __name__ == '__main__':
    # instantiate a zoo instance
    zoo = Zoo('Animals in Captivity')
    # instantiate and add animals to zoo
    fred, george, stripe, yogurt = Toucan('Fred', 10), Lion(
        'George', 15), Tiger('Stripe', 7), Bear('Yogurt', 11)
    # add animals to the zoo by chaining methods
    zoo.add_animal(fred).add_animal(
        george).add_animal(stripe).add_animal(yogurt)
    # print animals, feed, display again
    zoo.display_all_animals().feed_animals().display_all_animals
    # have animals do their unique method
    fred.bray(), george.roar(), stripe.mark_territory(), yogurt.scratch_back()
