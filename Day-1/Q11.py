account = None

while True:

    print("\n BANKING APPLICATION")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:

            if account is not None:
                print("Account already exists.")

            else:
                name = input("Enter account holder name: ")
                initial_balance = float(
                    input("Enter initial deposit: ")
                )

                if initial_balance < 0:
                    print("Initial deposit cannot be negative.")

                else:
                    account = {
                        "name": name,
                        "balance": initial_balance,
                        "history": []
                    }

                    account["history"].append(
                        f"Account created with balance {initial_balance}"
                    )

                    print("Account created successfully.")

        case 2:

            if account is None:
                print("Please create an account first.")

            else:
                deposit_amount = float(
                    input("Enter deposit amount: ")
                )

                if deposit_amount <= 0:
                    print("Deposit must be positive.")

                else:
                    account["balance"] += deposit_amount

                    account["history"].append(
                        f"Deposited: {deposit_amount}"
                    )

                    print("Deposit successful.")
                    print(
                        "Current Balance:",
                        account["balance"]
                    )

        case 3:

            if account is None:
                print("Please create an account first.")

            else:
                withdraw_amount = float(
                    input("Enter withdrawal amount: ")
                )

                if withdraw_amount <= 0:
                    print("Withdrawal must be positive.")

                elif withdraw_amount > account["balance"]:
                    print("Insufficient balance.")

                else:
                    account["balance"] -= withdraw_amount

                    account["history"].append(
                        f"Withdrawn: {withdraw_amount}"
                    )

                    print("Withdrawal successful.")
                    print(
                        "Current Balance:",
                        account["balance"]
                    )

        case 4:

            if account is None:
                print("Please create an account first.")

            else:
                print("Account Holder :", account["name"])
                print("Balance        :", account["balance"])

        case 5:

            if account is None:
                print("Please create an account first.")

            elif len(account["history"]) == 0:
                print("No transactions available.")

            else:
                print("\n TRANSACTION HISTORY")

                for transaction in account["history"]:
                    print(transaction)

        case 6:
            print("Thank you for using the banking application.")
            break

        case _:
            print("Invalid choice.")