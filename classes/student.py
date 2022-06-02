from classes.person import Person
import csv

class Student(Person):

    student_list = []

    def __init__(self, name, age, role, school_id, password):
        super().__init__(name, age, role, password)
        self.school_id = school_id

    @classmethod
    def all_students(cls):
        file_name = './data/students.csv'
        

        with open(file_name, newline='') as student_file:
            reader = csv.DictReader(student_file)

            for row in reader:
                cls.student_list.append(row)

        return cls.student_list

    @classmethod
    def add_student(cls, name, age, role, school_id, password):
        cls.student_list.append({'name': name, 'age': age, 'role': role, 'school_id': school_id, 'password': password})

    @classmethod
    def remove_student(cls, school_id):
        for i,item in enumerate(Student.student_list):
            if school_id == item['school_id']:
                Student.student_list.pop(i)