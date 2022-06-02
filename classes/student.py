from classes.person import Person
import csv

class Student(Person):


    def __init__(self, name, age, role, school_id, password):
        super().__init__(name, age, role, password)
        self.school_id = school_id

    @classmethod
    def all_students(cls):
        file_name = './data/students.csv'
        student_list = []

        with open(file_name, newline='') as student_file:
            reader = csv.DictReader(student_file)

            for row in reader:
                student_list.append(row)

        return student_list