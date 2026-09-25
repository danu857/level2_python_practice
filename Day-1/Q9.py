# Employee Management System

employees = []

while True:
    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Find Highest Salary")
    print("5. Display Employees by Department")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            employee_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            department = input("Enter Department: ")
            salary = float(input("Enter Salary: "))

            employee = {
                "id": employee_id,
                "name": name,
                "department": department,
                "salary": salary
            }

            employees.append(employee)
            print("Employee added successfully!")

        case 2:
            if len(employees) == 0:
                print("No employees found.")
            else:
                print("\nEmployee Details:")
                for employee in employees:
                    print(employee)

        case 3:
            search_id = input("Enter Employee ID to search: ")

            found = False

            for employee in employees:
                if employee["id"] == search_id:
                    print("\nEmployee Found:")
                    print(employee)
                    found = True
                    break

            if not found:
                print("Employee not found.")

        case 4:
            if len(employees) == 0:
                print("No employees available.")
            else:
                highest_salary = max(
                    [employee["salary"] for employee in employees]
                )

                for employee in employees:
                    if employee["salary"] == highest_salary:
                        print("\nEmployee with Highest Salary:")
                        print(employee)

        case 5:
            department_name = input("Enter Department Name: ")

            department_employees = [
                employee
                for employee in employees
                if employee["department"].lower() == department_name.lower()
            ]

            if len(department_employees) == 0:
                print("No employees found in this department.")
            else:
                print("\nEmployees in", department_name, "Department:")
                for employee in department_employees:
                    print(employee)

        case 6:
            print("Thank You!")
            break

        case _:
            print("Invalid Choice. Please try again.")