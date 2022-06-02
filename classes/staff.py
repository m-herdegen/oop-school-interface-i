from classes.person import Person
import csv 

class Staff(Person):
    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id

    @classmethod
    def all_staff(cls):
        file_name = './data/staff.csv'
        staff_list = []

        with open(file_name, newline='') as staff_file:
            reader = csv.DictReader(staff_file)

            for row in reader:
                staff_list.append(row)

        return staff_list