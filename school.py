class Student:
    def __init__(self, name, curr_class) -> None:
        self.name = name
        self.Curr_class = curr_class
        self.id = None

    def __repr__(self) -> str:
        return f'Student with name: {self.name}, class: {self.Curr_class}, Id: {self.id}'


class Teacher:
    def __init__(self, name, subject) -> None:
        self.name = name
        self.subject = subject

    def __repr__(self) -> str:
        return f'Teacher with name: {self.name}, subject: {self.subject}'

class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        teacher = Teacher(name, subject)
        self.teachers.append(teacher)

    def enroll_student(self, name, curr_class):
        student = Student(name, curr_class)
        student.id = len(self.students) + 1
        self.students.append(student)

    def __repr__(self) -> str:
        result = f'Welcome to {self.name}\n------Our Teachers------\n'
        for teacher in self.teachers:
            result += str(teacher) + '\n'
        result += '------Our Students------\n'
        for student in self.students:
            result += str(student) + '\n'
        return result

phitron = School('Phitron')

phitron.enroll_student('Alia', 'A')
phitron.enroll_student('Rafiq', 'B')
phitron.enroll_student('Kabir', 'C')

phitron.add_teacher('Jobbar', 'DS')
phitron.add_teacher('Sofiq', 'Database')

print(phitron)
