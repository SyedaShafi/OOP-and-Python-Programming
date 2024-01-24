class Student:
    def __init__(self, n, r):
        self.name = n
        self.roll = r
    
    def disp(self):
        print("Student name", self.name)
        print("Student roll", self.roll)


class User:
    @staticmethod
    def show(s):
        print("User Name: ", s.name)
        print("USer roll: ", s.roll)
        s.disp()

stu = Student('Rahul', 101)
User.show(stu)
        