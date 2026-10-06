from flask import Flask, render_template, request, redirect

from database import (
    create_table,
    insert_employee,
    fetch_all_employees,
    find_employee,
    update_employee,
    delete_employee
)


app = Flask(__name__)

create_table()


# Home Page
@app.route("/")
def home():

    employees = fetch_all_employees()

    return render_template(
        "index.html",
        employees=employees
    )


# Add Employee
@app.route("/add", methods=["POST"])
def add_employee():

    employee_id = request.form["employee_id"].strip()
    name = request.form["name"].strip()
    department = request.form["department"].strip()

    if employee_id == "":
        return "Employee ID cannot be empty!"

    if name == "":
        return "Name cannot be empty!"

    if department == "":
        return "Department cannot be empty!"

    try:
        age = int(request.form["age"])
    except ValueError:
        return "Please enter a valid age!"

    if age <= 0:
        return "Age must be greater than 0!"

    try:
        salary = float(request.form["salary"])
    except ValueError:
        return "Please enter a valid salary!"

    if salary < 0:
        return "Salary cannot be negative!"

    result = insert_employee(
        employee_id,
        name,
        age,
        department,
        salary
    )

    if result == False:
        return "Employee ID already exists!"

    return redirect("/")


# Search Employee
@app.route("/search")
def search_employee():

    employee_id = request.args.get("employee_id")

    employee = find_employee(employee_id)

    if employee:
        employees = [employee]
    else:
        employees = []

    return render_template(
        "index.html",
        employees=employees
    )


# Delete Employee
@app.route("/delete/<employee_id>")
def delete_employee_route(employee_id):

    delete_employee(employee_id)

    return redirect("/")


# Edit Employee
@app.route("/edit/<employee_id>")
def edit_employee(employee_id):

    employee = find_employee(employee_id)

    return render_template(
        "edit.html",
        employee=employee
    )


# Update Employee
@app.route("/update/<employee_id>", methods=["POST"])
def update_employee_route(employee_id):

    name = request.form["name"]
    age = int(request.form["age"])
    department = request.form["department"]
    salary = float(request.form["salary"])

    update_employee(
        employee_id,
        name,
        age,
        department,
        salary
    )

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)