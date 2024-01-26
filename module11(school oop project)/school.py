
class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.classrrooms = {}
    
    def add_classroom(self, classroom):
        self.classrrooms[classroom.name] = classroom
    
    def student_addmission(self, student, classroom_name):
        if classroom_name  in self.classrrooms:
            self.classrrooms[classroom_name].add_student(student)

        else:
            print(f'No classroom as named {classroom_name}')



class ClassRoom:
    def __init__(self, name) -> None:
        self.name = name
        self.students = []


    def add_student(self, student):
        serial_id = f'{self.name}-{len(self.students) + 1}'
        self.students.append(student)


    def __str__(self) -> str:
        return f'{self.name}-{len(self.students)}'




