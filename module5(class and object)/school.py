class Student:
    def __init__(self, name, id, fee):
        self.name = name
        self.id = id
        self.fee = fee
    
    def __repr__(self) -> str:
        return f'Student name: {self.name} Id: {self.id}  Fee: {self.fee}'
    
class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher name: {self.name}, Subject: {self.subject}'

class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []
    def add_teacher(self, name, subject):
        id = len(self.teachers)+101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)
    def enroll(self, name, fee):
        if(fee < 6500):
            return 'invalid fee'
        else:
            id = len(self.students)+1
            std1 = Student(name, id, fee)
            self.students.append(std1)
    def __repr__(self) -> str:
        print(f'-------welcome to {self.name}----------')
        print("_________all teachers___________")
        for item in self.teachers:
            print(item)
        print('________all Students________')
        for item in self.students:
            print(item)
        return '------------------------'

phitron = School('Phitron')

phitron.add_teacher('t1', 'DS')
phitron.add_teacher('t2', 'algo')
phitron.add_teacher('t3', 'Python')

phitron.enroll('std1', 5000)
phitron.enroll('std2', 30000)


print(phitron)






