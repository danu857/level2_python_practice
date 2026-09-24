def create_account(accounts: dict[str, dict]) -> None:

    print("\n CREATE ACCOUNT")

    account_number = input("Enter account number: ").strip()

    if account_number in accounts:
        print("Account already exists.")
        return

    name = input("Enter account holder name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    password = input("Create password(Password must contain at least 6 characters, "
            "one uppercase letter, one lowercase letter and one number.):")

    password_conditions = [
        len(password) >= 6,
        any(char.isupper() for char in password),
        any(char.islower() for char in password),
        any(char.isdigit() for char in password)
    ]

    if not all(password_conditions):
        print(
            "Password must contain at least 6 characters, "
            "one uppercase letter, one lowercase letter and one number."
        )
        return

    accounts[account_number] = {
        "name": name,
        "password": password,
        "balance": 0.0,
        "transactions": []
    }

    print("Account created successfully!")


def login(accounts: dict[str, dict]) -> str | None:
    print("\n===== LOGIN =====")

    account_number = input("Enter account number: ").strip()
    password = input("Enter password: ")

    if account_number not in accounts:
        print("Account not found.")
        return None

    if accounts[account_number]["password"] != password:
        print("Incorrect password.")
        return None

    print(f"Welcome, {accounts[account_number]['name']}!")
    return account_number


def deposit(accounts: dict[str, dict], account_number: str) -> None:
    print("\n DEPOSIT")

    amount = float(input("Enter deposit amount: "))

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    accounts[account_number]["balance"] += amount

    accounts[account_number]["transactions"].append(f"Deposited ₹{amount:.2f}")

    print(f"₹{amount:.2f} deposited successfully.")


def withdraw(accounts: dict[str, dict], account_number: str) -> None:
    print("\n WITHDRAW ")

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    balance = accounts[account_number]["balance"]

    if amount > balance:
        print("Insufficient balance.")
        return

    accounts[account_number]["balance"] -= amount

    accounts[account_number]["transactions"].append(
        f"Withdrawn ₹{amount:.2f}"
    )

    print(f"₹{amount:.2f} withdrawn successfully.")


def check_balance(accounts: dict[str, dict], account_number: str) -> None:
    balance = accounts[account_number]["balance"]

    print("\n BALANCE")
    print(f"Account Holder : {accounts[account_number]['name']}")
    print(f"Balance        : ₹{balance:.2f}")


def transaction_history(
    accounts: dict[str, dict],
    account_number: str) -> None:

    print("\n TRANSACTION HISTORY")

    transactions = accounts[account_number]["transactions"]

    if not transactions:
        print("No transactions found.")
        return

    for number, transaction in enumerate(transactions, start=1):
        print(f"{number}. {transaction}")


def display_accounts(accounts: dict[str, dict]) -> None:
    print("\n ALL ACCOUNTS")

    if not accounts:
        print("No accounts available.")
        return

    sorted_accounts = sorted(accounts)

    for account_number in sorted_accounts:
        account = accounts[account_number]

        print(
            f"Account: {account_number} | "
            f"Name: {account['name']} | "
            f"Balance: ₹{account['balance']:.2f}"
        )


def account_summary(
    accounts: dict[str, dict],
    account_number: str) -> None:

    account = accounts[account_number]

    print("\n ACCOUNT SUMMARY")
    print(f"Account Number : {account_number}")
    print(f"Name           : {account['name']}")
    print(f"Balance        : ₹{account['balance']:.2f}")
    print(f"Transactions   : {len(account['transactions'])}")


def main() -> None:
    accounts: dict[str, dict] = {}

    while True:
        print("       BANKING APPLICATION")
        print("1. Create Account")
        print("2. Login")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check Balance")
        print("6. Transaction History")
        print("7. Account Summary")
        print("8. Display All Accounts")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()

        match choice:
            case "1":
                create_account(accounts)

            case "2":
                logged_account = login(accounts)
                if logged_account:
                    print("Login successful.")

            case "3":
                account_number = input("Enter account number: ").strip()
                if account_number in accounts:
                    deposit(accounts, account_number)
                else:
                    print("Account not found.")

            case "4":
                account_number = input("Enter account number: ").strip()
                if account_number in accounts:
                    withdraw(accounts, account_number)
                else:
                    print("Account not found.")

            case "5":
                account_number = input("Enter account number: ").strip()
                if account_number in accounts:
                    check_balance(accounts, account_number)
                else:
                    print("Account not found.")

            case "6":
                account_number = input("Enter account number: ").strip()
                if account_number in accounts:
                    transaction_history(accounts, account_number)
                else:
                    print("Account not found.")

            case "7":
                account_number = input("Enter account number: ").strip()
                if account_number in accounts:
                    account_summary(accounts, account_number)
                else:
                    print("Account not found.")

            case "8":
                display_accounts(accounts)

            case "9":
                print("Thank you for using the Banking Application.")
                break

            case _:
                print("Invalid choice. Please try again.")
main()