class Cat(object):
    def __new__(cls, *args, **kwargs): 
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        pass

if __name__ == '__main__':
    cat1 = Cat()
    cat2 = Cat()
    print(cat1 is cat2)
