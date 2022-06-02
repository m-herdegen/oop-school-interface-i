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

# from classes.school import School 

school = School('Ridgemont High') 
# print('\n*****STAFF*****')
# print(*school.staff, sep='\n') 
# print('\n\n*****STUDENTS*****')
# print(*school.students, sep = '\n')

options_arr = [1, 2, 3, 4, 5]
bool_var = True

while(bool_var):
    user_input = input("""
Ridgemont High Student Interface 
--------------------------------
Welcome, Richard. Your access level is Principal
    What would you like to do?
    Options:
    1 List All Students
    2 View Individual Student <student_id>
    3 Add a Student
    4 Remove a Student <student_id>
    5 Quit
\n\n>>""")
    if user_input == '1':
        print('\n\n*****STUDENTS*****')
        print(*school.students, sep = '\n') 
    elif user_input == '2':
        id = input('Enter a valid student ID:\n>>')
        check = next((item for item in school.students if item['school_id'] == id), 'there is no student with that id')
        print(check)

    elif user_input == '3':
        name = input('Please enter the student name: ')
        age = input('Please enter the student age: ')
        role = 'Student'
        school_id = input('Please enter the student ID: ')
        password = input('Please enter a temporary password: ')

        Student.add_student(name, age, role, school_id, password)
        print('Student added to the database.')

    elif user_input == '4':
        id = input('Enter a valid student ID:\n>>')
        next((Student.remove_student(id) for item in school.students if item['school_id'] == id), 'there is no student with that id')
        
    elif user_input == '5':
        bool_var = False

    else:
        user_input = input('Please read the directions. Hit enter to continue.')


