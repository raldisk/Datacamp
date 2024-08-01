# 1/3
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary


emp = Employee()
emp.set_name("Korel Rossi")
emp.set_salary(50000)

# Print the salary attribute of emp
print(emp.salary)

# Increase salary of emp by 1500
emp.salary = emp.salary + 1500

# Print the salary attribute of emp again
print(emp.salary)


# 2/3
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary

    # Add a give_raise() method with raise amount as a parameter
    def give_raise(self, amount):
        self.salary = self.salary + amount


emp = Employee()
emp.set_name("Korel Rossi")
emp.set_salary(50000)

print(emp.salary)
emp.give_raise(1500)
print(emp.salary)


# 3/3
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary

    def give_raise(self, amount):
        self.salary = self.salary + amount

    # Add monthly_salary method that returns 1/12th of salary attribute
    def monthly_salary(self):
        return self.salary / 12


emp = Employee()
emp.set_name("Korel Rossi")
emp.set_salary(50000)

# Get monthly salary of emp and assign to mon_sal
mon_sal = emp.monthly_salary()

# Print mon_sal
print(mon_sal)
