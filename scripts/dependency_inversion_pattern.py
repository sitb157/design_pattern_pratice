class Animal:
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print('meow')

class Dog(Animal):
    def speak(self):
        print('bark')

class Cow(Animal):
    def speak(self):
        print('moo')

class Zoo:
    def __init__(self): 
        self.animals = []

    def addAnimal(self, animal: Animal):
        self.animals.append(animal)

    def speaks(self):
        for animal in self.animals:
            animal.speak()

if __name__ == '__main__':
    zoo = Zoo()
    zoo.addAnimal(Cat())
    zoo.addAnimal(Dog())
    zoo.addAnimal(Cow())
    zoo.speaks()

