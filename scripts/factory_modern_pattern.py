class Animal():
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("bark")

class Cat(Animal):
    def speak(self):
        print("meow")

class AnimalFactory:
    def createAnimal(self):
        pass

class CatFactory(AnimalFactory):
    def __init__(self):
        self.cat_count = 0

    def createAnimal(self):
        self.cat_count += 1
        return Cat()
    
    def countAnimal(self):
        return self.cat_count

class DogFactory(AnimalFactory):
    def createAnimal(self):
        return Dog()

    def addWing(self, dog: Dog):
        print("dog wing added")
        return dog

if __name__ == '__main__':
    cat_factory = CatFactory()
    dog_factory = DogFactory()
    cat_1 = cat_factory.createAnimal()
    cat_2 = cat_factory.createAnimal()
    dog = dog_factory.createAnimal()
    print(f"cat's num is {cat_factory.countAnimal()}")
    dog_factory.addWing(dog)
