# Day 51: Practice Project (Employee Management System)

'''
Project Structure
We’ll keep it CLI-based (Command Line Interface) for simplicity.

Features:
Add Employee

View All Employees

Search Employee by ID

Update Employee Information

Delete Employee

Exit
'''

import json
import os

EMPLOYEE_FILE = "employees.json"

# Load employee data
def load_employees():
    if not os.path.exists(EMPLOYEE_FILE):
        return {}
    with open(EMPLOYEE_FILE, "r") as file:
        return json.load(file)

# Save employee data
def save_employees(data):
    with open(EMPLOYEE_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add employee
def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")

    employees = load_employees()
    if emp_id in employees:
        print("Employee ID already exists!")
        return

    employees[emp_id] = {
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    }

    save_employees(employees)
    print("✅ Employee added successfully!")

# View all employees
def view_employees():
    employees = load_employees()
    if not employees:
        print("No employees found.")
        return
    for emp_id, info in employees.items():
        print(f"\nID: {emp_id}")
        for key, value in info.items():
            print(f"{key.title()}: {value}")

# Search employee
def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    employees = load_employees()
    emp = employees.get(emp_id)
    if emp:
        print(f"\nEmployee Found - ID: {emp_id}")
        for key, value in emp.items():
            print(f"{key.title()}: {value}")
    else:
        print("❌ Employee not found.")

# Update employee
def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    employees = load_employees()
    if emp_id not in employees:
        print("❌ Employee not found.")
        return

    print("Leave field blank to keep existing data.")
    name = input(f"Enter new name ({employees[emp_id]['name']}): ") or employees[emp_id]['name']
    age = input(f"Enter new age ({employees[emp_id]['age']}): ") or employees[emp_id]['age']
    department = input(f"Enter new department ({employees[emp_id]['department']}): ") or employees[emp_id]['department']
    salary = input(f"Enter new salary ({employees[emp_id]['salary']}): ") or employees[emp_id]['salary']

    employees[emp_id] = {
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    }
    save_employees(employees)
    print("✅ Employee updated successfully!")

# Delete employee
def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    employees = load_employees()
    if emp_id in employees:
        del employees[emp_id]
        save_employees(employees)
        print("✅ Employee deleted successfully!")
    else:
        print("❌ Employee not found.")

# Menu
def menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice = input("Choose an option: ")

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
            print("👋 Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
