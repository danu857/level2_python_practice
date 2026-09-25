employee_name = input("Enter the employee name : ")
basic_pay = int(input("Enter the employee Salary:"))
experience = int(input("Enter the employee experience:"))

if basic_pay > 20000:
    DA = basic_pay * 0.585
    HRA = basic_pay * 0.15

elif basic_pay > 15000:
    DA = basic_pay * 0.46
    HRA = basic_pay * 0.12

else:
    DA = basic_pay * 0.425
    HRA = 1500

gross_pay = basic_pay + DA + HRA

if experience < 1:
    bonus_percentage = 5

elif experience <= 3:
    bonus_percentage = 10

elif experience <= 6:
    bonus_percentage = 15

else:
    bonus_percentage = 20

bonus = basic_pay * bonus_percentage / 100
salary = gross_pay + bonus

if salary > 100000:
    category = "High Salary"

elif salary >= 50000:
    category =  "Medium Salary"

else:
    category = "Low Salary"

print("\nEmployee Name : ",employee_name)
print("Basic Pay : ",basic_pay)
print("House Rent Allowance : ",HRA)
print("Dearness Allowance : ",DA)
print("Gross Pay : ",gross_pay)
print("Bonus : ",bonus)
print("Salary : ",salary)
print("Category : ",category)

