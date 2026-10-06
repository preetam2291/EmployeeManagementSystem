from database import (
    create_table,
    insert_employee,
    fetch_all_employees,
    find_employee,
    update_employee,
    delete_employee
)


def add_employee():
    print("\n--- Add Employee ---")

    employee_id = input("Enter employee ID: ").strip()

    if employee_id == "":
        print("Employee ID cannot be empty!")
        return

    name = input("Enter employee name: ").strip()

    if name == "":
        print("Name cannot be empty!")
        return

    try:
        age = int(input("Enter employee age: "))

        if age <= 0:
            print("Age must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid age.")
        return

    department = input("Enter department: ").strip()

    if department == "":
        print("Department cannot be empty!")
        return

    try:
        salary = float(input("Enter salary: "))

        if salary < 0:
            print("Salary cannot be negative.")
            return

    except ValueError:
        print("Please enter a valid salary.")
        return

    result = insert_employee(
        employee_id,
        name,
        age,
        department,
        salary
    )

    if result:
        print("\nEmployee added successfully!")
    else:
        print("Employee ID already exists!")


def display_employees():

    print("\n--- Employee List ---")

    employees = fetch_all_employees()

    if len(employees) == 0:
        print("No employees found.")
        return

    for employee in employees:

        print("\n-----------------------")
        print("ID         :", employee[0])
        print("Name       :", employee[1])
        print("Age        :", employee[2])
        print("Department :", employee[3])
        print("Salary     :", employee[4])


def search_employee():

    print("\n--- Search Employee ---")

    employee_id = input("Enter employee ID: ").strip()

    employee = find_employee(employee_id)

    if employee:

        print("\nEmployee Found!")
        print("-----------------------")
        print("ID         :", employee[0])
        print("Name       :", employee[1])
        print("Age        :", employee[2])
        print("Department :", employee[3])
        print("Salary     :", employee[4])

    else:
        print("Employee not found.")


def update_employee_details():

    print("\n--- Update Employee ---")

    employee_id = input("Enter employee ID: ").strip()

    employee = find_employee(employee_id)

    if employee is None:
        print("Employee not found!")
        return

    print("\nCurrent Employee Details:")
    print("Name       :", employee[1])
    print("Age        :", employee[2])
    print("Department :", employee[3])
    print("Salary     :", employee[4])

    print("\nEnter New Details")

    name = input("Enter new name: ").strip()

    if name == "":
        print("Name cannot be empty!")
        return

    try:
        age = int(input("Enter new age: "))

        if age <= 0:
            print("Age must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid age.")
        return

    department = input("Enter new department: ").strip()

    if department == "":
        print("Department cannot be empty!")
        return

    try:
        salary = float(input("Enter new salary: "))

        if salary < 0:
            print("Salary cannot be negative.")
            return

    except ValueError:
        print("Please enter a valid salary.")
        return

    update_employee(
        employee_id,
        name,
        age,
        department,
        salary
    )

    print("\nEmployee updated successfully!")


def delete_employee_details():

    print("\n--- Delete Employee ---")

    employee_id = input("Enter employee ID: ").strip()

    employee = find_employee(employee_id)

    if employee is None:
        print("Employee not found!")
        return

    print("\nEmployee Found!")
    print("Name       :", employee[1])
    print("Department :", employee[3])

    confirmation = input(
        "Are you sure you want to delete this employee? (yes/no): "
    )

    if confirmation.lower() == "yes":

        delete_employee(employee_id)

        print("Employee deleted successfully!")

    else:
        print("Delete cancelled.")


create_table()


while True:

    print("\n=================================")
    print("   EMPLOYEE MANAGEMENT SYSTEM")
    print("=================================")

    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        display_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_employee_details()

    elif choice == "5":
        delete_employee_details()

    elif choice == "6":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Please try again.")