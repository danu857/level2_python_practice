current_pin = input("Create pin : ")
Balance = int(input("Enter your balance : "))

for attempts in range(3):
    pin = int(input("Enter your pin:"))
    if pin == current_pin:
        print("PIN verified")
        break
    else:
        print("Invalid PIN!")

else:
    print("Maximum attempts exceeded.")
    exit()

while True:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change PIN")
    print("5. Exit")

    choice = int(input("Enter your choice : "))

    match choice:
        case 1:
            print("Current Balance : ",Balance)

        case 2:
            deposit_amount = int(input("Enter the amount you like to deposit : "))
            if deposit_amount > 0:
                Balance = Balance + deposit_amount
            print("Amount deposited successfully")

        case 3:
            withdraw_amount = int(input("Enter the amount you like to withdraw : "))
            if Balance > withdraw_amount:
                Balance = Balance - withdraw_amount
                print("Amount withdrawn successfully")
            else:
                print("Insufficient Balance")

        case 4:
            for attempts in range(3):
                old_pin = int(input("Enter your current pin:"))
                if old_pin == current_pin:
                    print("PIN verified")
                    new_pin = int(input("Enter new pin : "))
                    if current_pin != new_pin:
                        print("New pin should not be same as the old pin")
                    else:
                        current_pin = new_pin
                        break
                else:
                    print("Invalid PIN!")
            else:
                print("Maximum attempts exceeded.")
                exit()

        case 5:
            print("Thankyou for using the ATM!")
            break

        case _:
            print("Enter valid choice")