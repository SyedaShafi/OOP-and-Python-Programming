class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    def __add__(self, other):
        if isinstance(other, Cricketer):
            return self.age + other.age
        return NotImplemented

s = Cricketer('sakib', 40, 12, 16, 'BD')
c = Cricketer('Mushi', 34, 10, 14, 'BD')

# Chain addition for three objects
result = s + c
print(result)  # Output: 106
