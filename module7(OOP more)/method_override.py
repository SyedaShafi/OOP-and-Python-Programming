class Person:
    def __init__(self, age, name, height) -> None:
        self.name = name
        self.age = age
        self.height = height
    def exersize(self):
        raise NotImplemented

class Doctor(Person):
    def __init__(self, age, name, height, salary) -> None:
        self.salary = salary
        super().__init__(age, name, height)
    def exersize(self):
        print("They do exersize")

obj = Doctor(23, "XYS", 98, 300000)

obj.exersize()


