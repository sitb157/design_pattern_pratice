class Animal:
    def speak(self):
        None

class Dog(Animal):
    def speak(self):
        print("bark")

class Cat(Animal):
    def speak(self):
        print("meow")

### Add Animals with using open closed pattern 

class Cow(Animal):
    def speak(self):
        print("moo")

class Duck(Animal):
    def speak(self):
        print("quak")

if __name__ == '__main__':
    animals = []
    animals.append(Dog())
    animals.append(Cat())
    animals.append(Cow())
    animals.append(Duck())
    for a in animals:
        a.speak()
