student_name = input("Enter student's name:")
tamil_mark = int(input("Enter tamil mark:"))
english_mark = int(input("Enter english mark:"))
maths_mark = int(input("Enter maths mark:"))
science_mark = int(input("Enter science mark:"))
computer_mark = int(input("Enter computer mark:"))
print("\n")

total_marks = (tamil_mark + english_mark + maths_mark + science_mark + computer_mark)
average= total_marks/5

if tamil_mark < 40 or english_mark < 40 or maths_mark < 40 or science_mark < 40 or computer_mark < 40:
    result = "FAIL"
    grade = "F"
    
else:
    if average >= 50:
        result = "PASS"

        if average >= 90:
            grade="O"
        elif average >= 80:
            grade="A"
        elif average >= 60:
            grade="B"
        elif average >= 50:
            grade="C"
    else:
        grade = "F"

print("Student name : ",student_name)
print("\n")
print("Tamil : ",tamil_mark)
print("English : ",english_mark)
print("Maths : ",maths_mark)
print("Science : ",science_mark)
print("Computer : ",computer_mark)
print("\n")

print("Total : ",total_marks)
print("Average : ",average)
print("Grade : ",grade)
print("Results : ",result)
