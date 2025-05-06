class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp = Employee("Shiza", 50000, "123-25-2222")

print("Name:", emp.name)
print("Salary:", emp._salary)

try:
    print("SSN:", emp.__ssn)
except AttributeError as e:
    print("Error accessing __ssn:", e)

print("SSN (via name mangling):", emp._Employee__ssn)
