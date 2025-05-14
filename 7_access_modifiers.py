class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    def get_ssn(self):
        return self.__ssn
    
    def set_salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("salary must be positive in number")

    def display(self):
        print(f"Name: {self.name}") # public attribute
        print(f"Salary: {self._salary}") # protected attribute
        print(f"SSN: {self.__ssn()}") # private attribute


class Manager(Employee):
    def __init__(self, name, salary, ssn, department):
        # Call the constructor of the parent class
        super().__init__(name, salary, ssn)
        self.department = department

    def show_manager_info(self):
        print(f"Manager Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Protected Salary: {self._salary}") # protected attribute
        print(f"Accessing SSN via getter command: {self.get_ssn()}")

m= Manager("Ali", "80000", "123-45-2025", "HR")
m.show_manager_info()
m.set_salary(90000)
print(f"Updated Salary:", m._salary)

print("Private SSN via managed: " , m._Employee__ssn) # This will raise an AttributeError because __ssn is private