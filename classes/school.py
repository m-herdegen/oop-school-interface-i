from classes.student import Student
from classes.staff import Staff

class School:
    def __init__(self, name):
        self.name = name   
        self.students = Student.all_students() 
        self.staff = Staff.all_staff()

