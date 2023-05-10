class Animal(object):
    def __init__(self):
        pass
    def speak(self):
        pass

class Cat(Animal):
    def __init__(self):
        pass
    def speak(self):
        print("meow~")

class Dog(Animal):
    def __init__(self):
        pass
    def speak(self):
        print("bark~")

def animal_speak(animal: Animal):
    animal.speak()

if __name__ == '__main__':
    zoo = []
    zoo.append(Cat())
    zoo.append(Dog())
    for animal in zoo:
        animal_speak(animal)
