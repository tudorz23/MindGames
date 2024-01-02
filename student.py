class Student:
    def __init__(self, name, surname, grade):
        self.name = name
        self.surname = surname
        self.grade = grade

    def print_student(self):
        print('Student {} {} has grade {}.'.format(self.name, self.surname, self.grade))
