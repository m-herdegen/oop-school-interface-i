from classes.person import Person 
from classes.school import School 
from classes.staff import Staff 
from classes.student import Student
# from pprint import pprint

# school = School('Ridgemont High') 

# print(school.name)

# student_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
# student1 = Student(**student_info)
# print(student1.name)

# print(*Student.all_students(), sep='\n')

from classes.school import School 

school = School('Ridgemont High') 
print('\n*****STAFF*****')
print(*school.staff, sep='\n') 
print('\n\n*****STUDENTS*****')
print(*school.students, sep = '\n')