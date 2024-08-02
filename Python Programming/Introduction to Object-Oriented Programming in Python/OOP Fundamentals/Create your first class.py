# 1/2
# Create an empty class Employee
class Employee:
    pass


# Create an object emp of class Employee
emp = Employee()


# 2/2
class Employee:
    def set_name(self, new_name):
        self.name = new_name


emp = Employee()

# Use set_name() on emp to set the name of emp to 'Korel Rossi'
emp.set_name("Korel Rossi")
print(emp.name)
