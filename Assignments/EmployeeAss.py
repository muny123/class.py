  # create a class Employee
class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        
    # string method that returns employee information
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.salary}"
    
    #  update employee's position
    def update_position(self, new_position):
        self.position = new_position
     
     # update employee's salary
    def update_salary(self, new_salary):
        self.salary = new_salary
        
 # creating a new class Company
class Company:
    def __init__(self):
        self.employees = []
    
    #function to add an emlpyee
    def add_employee(self, employee):
        self.employees.append(employee)
        print("Employee added successfully")
        
    #function to remove an employee
    def remove_employee(self, name):
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                print("Employee has been removed!")
            
  
    # function to update an employee
    def update_employee(self, name, new_position, new_salary):
        for employee in self.employees:
            if employee.name == name:
                if new_position:
                    employee.update_position(new_position)
                if new_salary:
                    employee.update_salary(new_salary)
                
    
    #function to view all employees
    def view_all_employees(self):
        for employee in self.employees:
            print(employee)
      
      
    # function to find an employee  
    def find_employee(self, name):
        for employee in self.employees:
            if employee.name == name:
                return employee
            else:
                print(" Employee not found!")
        return " "


def main():
    company = Company()

    while True:
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Update Employee")
        print("4. View All Employees")
        print("5. Find Employee")
        print("6. Exit")

        choice = input("Choose an option: ")
        # choice to add an employee
        if choice == "1":
            name = str(input("Enter name: "))
            age = int(input("Enter age: "))
            position = str(input("Enter position: "))
            salary = float(input("Enter salary: "))
            employee = Employee(name, age, position, salary)
            company.add_employee(employee)
            
        # choice to remove an employee    
        elif choice == "2":
            name = input("Enter name: ")
            company.remove_employee(name)
        #choice to update an employee    
        elif choice == "3":
            name = input("Enter name: ")
            new_position = input("Enter new position (optional): ")
            new_salary = input("Enter new salary (optional): ")
            company.update_employee(name, new_position, new_salary)
        # choice to view all employees   
        elif choice == "4":
            company.view_all_employees()
        #choice to find an employee    
        elif choice == "5":
            name = input("Enter name: ")
            employee = company.find_employee(name)
            if employee:
                print(employee)
            else:
                print("Employee not found")
        elif choice == "6":
            break
        else:
            print("Invalid option, try again!!!")


if __name__ == "__main__":
    main()

 