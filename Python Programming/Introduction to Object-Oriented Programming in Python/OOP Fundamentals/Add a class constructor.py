# 1/2
class Employee:
    # Create __init__() method
    def __init__(self, name, salary=0):
        # Create the name and salary attributes
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

    def monthly_salary(self):
        return self.salary / 12


emp = Employee("Korel Rossi")
print(emp.name)
print(emp.salary)


# 2/2
class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        # Check if salary is positive
        if salary >= 0:
            self.salary = salary
        else:
            self.salary = 0
            print("Invalid salary!")

    def give_raise(self, amount):
        self.salary += amount

    def monthly_salary(self):
        return self.salary / 12


emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)
