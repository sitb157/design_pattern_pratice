class Command:
    def execute(self):
        pass

class Animal:
    def sit(self):
        pass
    def stand(self):
        pass
    def speak(sefl):
        pass

class Dog(Animal):
    def __init__(self, name: str):
        self.name = name 
    def sit(self):
        print(f"{self.name} sits")

    def stand(self):
        print(f"{self.name} stands")

    def speak(self):
        print(f"{self.name} bark")

class Cat(Animal):
    def __init__(self, name: str):
        self.name = name 
    def sit(self):
        print(f"{self.name} sits")

    def stand(self):
        print(f"{self.name} stands")

    def speak(self):
        print(f"{self.name} meow")

class AnimalCommand(Command):
    def __init__(self, animal: Animal, commands_list: list):
        self.commands_list = commands_list
        self.animal = animal

    def execute(self):
        for command in self.commands_list:
            if command == 'sit':
                self.animal.sit()
            elif command == 'stand':
                self.animal.stand()
            elif command == 'speak':
                self.animal.speak()

class Invoker(object):
    def __init__(self):
        self.commands = []

    def addCommand(self, _command: Command):
        self.commands.append(_command)

    def executeCommand(self):
        for command in self.commands:
            command.execute()

if __name__ == '__main__':
    dog = Dog("dog")
    cat = Cat("cat")
    dogCommand = AnimalCommand(dog, ['sit', 'stand', 'speak']) 
    catCommand = AnimalCommand(cat, ['sit', 'stand', 'speak']) 
    invoker = Invoker()
    invoker.addCommand(dogCommand)
    invoker.addCommand(catCommand)
    invoker.executeCommand()
