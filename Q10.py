# Student Management Console

students = []

while True:
    print("\n===== STUDENT MANAGEMENT CONSOLE =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Average")
    print("5. Find Topper")
    print("6. Display Passed Students")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            name = input("Enter Student Name: ")
            mark = int(input("Enter Student Mark: "))

            student = {
                "name": name,
                "mark": mark
            }

            students.append(student)
            print("Student added successfully!")

        case 2:
            if len(students) == 0:
                print("No students available.")
            else:
                print("\nStudent Details:")
                for student in students:
                    print(student)

        case 3:
            search_name = input("Enter Student Name to Search: ")

            found = False

            for student in students:
                if student["name"].lower() == search_name.lower():
                    print("\nStudent Found:")
                    print(student)
                    found = True
                    break

            if not found:
                print("Student not found.")

        case 4:
            if len(students) == 0:
                print("No students available.")
            else:
                total = sum([student["mark"] for student in students])
                average = total / len(students)

                print("Average Mark =", average)

        case 5:
            if len(students) == 0:
                print("No students available.")
            else:
                highest_mark = max(
                    [student["mark"] for student in students]
                )

                for student in students:
                    if student["mark"] == highest_mark:
                        print("\nTopper:")
                        print(student)

        case 6:
            passed_students = [
                student
                for student in students
                if student["mark"] >= 40
            ]

            if len(passed_students) == 0:
                print("No students passed.")
            else:
                print("\nPassed Students:")
                for student in passed_students:
                    print(student)

        case 7:
            print("Thank You!")
            break

        case _:
            print("Invalid Choice!")