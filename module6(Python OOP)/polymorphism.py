class Animal:
    def __init__(self, name) -> None:
        self.name = name
    def make_sound(self):
        print('animal makes sound')


class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('meow meow')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('bark bark')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    # def make_sound(self):
    #     pass

don = Cat('Real Don')
don.make_sound()

shapherd = Dog('local sh')
shapherd.make_sound()


mess = Goat('LM')
mess.make_sound()



