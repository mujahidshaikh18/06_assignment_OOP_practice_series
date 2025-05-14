class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_employee_info(self):
        return f"Employee Name: {self.name}, Position is: {self.position}"
    
class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee

    def get_department_info(self):
        return f"Department: {self.department_name}, {self.employee.get_employee_info()}"
    
# Creating instances
employee1 = Employee("Moin Shaikh", "Software Engineer")
department1 = Department("IT", employee1)

# Displaying information
print(department1.get_department_info())
# Output Department: IT Department, Employee: Employee Name: Moin Shaikh, Position is: Software Engineer

