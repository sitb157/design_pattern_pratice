class Observer:
    def update(self):
        None

class Dog(Observer):
    def update(self):
        print("bark")

class Cat(Observer):
    def update(self):
        print("meow")

class Cow(Observer):
    def update(self):
        print("moo")
    
class Owner(Observer):
    def __init__(self):
        self.observers = []
    
    def addObserver(self, _observer:Observer):
        self.observers.append(_observer)

    def notify(self):
        for o in self.observers:
            o.update()

if __name__ == '__main__':
    owner = Owner()
    owner.addObserver(Dog())
    owner.addObserver(Cat())
    owner.addObserver(Cow())
    owner.notify()
