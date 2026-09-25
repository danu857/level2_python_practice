customer_name = input("Enter your name : ")
units=int(input("Enter unit reading: "))

if units < 0:
    print("Units consumed cannot be negative")
else:
    if units <= 100:
        amount = 0
    elif units <= 200:
        amount = (units - 100) * 2.25
    elif units <= 500:
        amount = (100 * 0) + (100 * 2.25) + (units - 200) * 4.5
    else:
        amount = (100 * 0) + (100 * 2.25) + (300 * 4.5) + (units - 500) * 6

    tax = amount * 0.05
    total_amount = amount + tax

    print("\nElectricity Bill : ")
    print("Customer Name : ",customer_name)
    print("Units Consumed : ",units)
    print("Energy Charge : ",amount)
    print("Tax : ",tax)
    print("\nTotal Bill : ",total_amount)
