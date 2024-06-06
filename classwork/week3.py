class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def change_salary(self, amount):
        self.salary += amount
        
# create employee instances
employees = [
    Employee("Alice", 50000),
    Employee("Bob", 60000),
    Employee("chalie", 70000),
    Employee("Avast", 2000)
]

# change the salries by 10k
for employee in employees:
    if employee.name != "Avast":
        employee.change_salary(10000)

for employee in employees:
    print(f"{employee.name}'s new salary : {employee.salary}")


    