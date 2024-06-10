# Employee Management System (EMS)

# Initialize an empty dictionary to store employee data
employees = {}

# Function to add an employee
def add_employee():
    employee_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    email = input("Enter employee email: ")
    department = input("Enter employee department: ")
    job_title = input("Enter employee job title: ")
    
    # Store employee data in the dictionary
    employees[employee_id] = {
        "name": name,
        "email": email,
        "department": department,
        "job_title": job_title
    }
    
    print("Employee added successfully!")

# Function to display all employees
def view_employees():
    if not employees:
        print("No employees found!")
    else:
        for employee_id, employee in employees.items():
            print(f"Employee ID: {employee_id}")
            print(f"Name: {employee['name']}")
            print(f"Email: {employee['email']}")
            print(f"Department: {employee['department']}")
            print(f"Job Title: {employee['job_title']}")
            print(f"name, email, department, job_tittle")

# Function to search for an employee
def search_employee():
    employee_id = input("Enter employee ID to search: ")
    if employee_id in employees:
        print("Employee found!")
        print(f"Name: {employees[employee_id]['name']}")
        print(f"Email: {employees[employee_id]['email']}")
        print(f"Department: {employees[employee_id]['department']}")
        print(f"Job Title: {employees[employee_id]['job_title']}")
    else:
        print("Employee not found!")

# Function to update an employee
def update_employee():
    employee_id = input("Enter employee ID to update: ")
    if employee_id in employees:
        name = input("Enter new name: ")
        email = input("Enter new email: ")
        department = input("Enter new department: ")
        job_title = input("Enter new job title: ")
        
        # Update employee data in the dictionary
        employees[employee_id] = {
            "name": name,
            "email": email,
            "department": department,
            "job_title": job_title
        }
        
        print("Employee updated successfully!")
    else:
        print("Employee not found!")

# Function to delete an employee
def delete_employee():
    employee_id = input("Enter employee ID to delete: ")
    if employee_id in employees:
        del employees[employee_id]
        print("Employee deleted successfully!")
    else:
        print("Employee not found!")

# Main program
while True:
    print("Employee Management System (EMS)")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")

print("Goodbye!")

