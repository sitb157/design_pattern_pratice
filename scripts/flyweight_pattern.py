class AnimalDNA:
    def __init__(self, name, DNA):
        self.name = name
        self.DNA = DNA

class Animal:
    DNA_table = dict() 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        if not self.name in Animal.DNA_table:
            print(f"No find {self.name} in DNA_table")

    def __repr__(self):
        _DNA = Animal.DNA_table[self.name]
        return f"{self.name}'s DNA is {_DNA}"

    @staticmethod
    def addDNA(DNA: AnimalDNA):
        Animal.DNA_table[DNA.name] = DNA.DNA

if __name__ == '__main__':
    dogDNA = AnimalDNA('dog', '1q84')
    catDNA = AnimalDNA('cat', '2q34')
    Animal.addDNA(dogDNA)
    Animal.addDNA(catDNA)
    dog = Animal('dog', 15)
    cat = Animal('cat', 12)
    print(dog)
    print(cat)
