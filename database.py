import sqlite3


def connect_database():
    return sqlite3.connect("employee.db")


def create_table():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        department TEXT NOT NULL,
        salary REAL NOT NULL
    )
    """)

    connection.commit()
    connection.close()


def insert_employee(employee_id, name, age, department, salary):
    connection = connect_database()
    cursor = connection.cursor()

    try:
        cursor.execute("""
        INSERT INTO employees
        (id, name, age, department, salary)
        VALUES (?, ?, ?, ?, ?)
        """, (employee_id, name, age, department, salary))

        connection.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        connection.close()


def fetch_all_employees():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    connection.close()

    return employees


def find_employee(employee_id):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM employees WHERE id = ?",
        (employee_id,)
    )

    employee = cursor.fetchone()

    connection.close()

    return employee


def update_employee(employee_id, name, age, department, salary):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE employees
    SET name = ?, age = ?, department = ?, salary = ?
    WHERE id = ?
    """, (name, age, department, salary, employee_id))

    connection.commit()

    connection.close()


def delete_employee(employee_id):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE id = ?",
        (employee_id,)
    )

    connection.commit()
