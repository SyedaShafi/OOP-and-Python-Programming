# ----example 1---------


# class Person:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#     def Display(self):
#         print(self.name, self.id)


# class emp(Person):
#     def Print(self):
#         print('emp class called')

# emp1 = emp('shafi', 1009)
# emp1.Display()

# emp1.Print()



#______________ example 2____________

# parent class
class Person():
    def __init__(self, name, age):#rahul 23
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

# child class
class Student(Person):
    def __init__(self, name, age):# mayank 23
        self.sName = name
        self.sAge = age
        super().__init__("Rahul", age)

    def displayInfo(self):
        print(self.sName, self.sAge)



obj = Student("Mayank", 23)
obj.display()
obj.displayInfo()









