class Animal:
    def speak(self):
       None 

class Dog(Animal):
    def speak(self):
        print("bark!!")

class Cat(Animal):
    def speak(self):
        print("meow!!")
    
class Zoo(Animal):
    def __init__(self):
        self.animals = []

    def addAnimal(self, _animal: Animal): 
        self.animals.append(_animal)
    
    def speak(self):
        print("zoo!!")
        for a in self.animals:
            a.speak()
            
if __name__ == '__main__':
    zoo_1 = Zoo()
    zoo_1.addAnimal(Cat())
    zoo_1.addAnimal(Cat())

    zoo_2 = Zoo()
    zoo_2.addAnimal(Dog())
    zoo_2.addAnimal(Dog())

    zoo_3 = Zoo()
    zoo_3.addAnimal(zoo_1)
    zoo_3.addAnimal(zoo_2)

    zoo_3.speak()
