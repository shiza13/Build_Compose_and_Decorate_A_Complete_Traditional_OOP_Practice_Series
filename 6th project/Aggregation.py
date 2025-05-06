class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee

employee = Employee("John")
department = Department("HR", employee)

print(f"Department: {department.name}, Employee: {department.employee.name}")
