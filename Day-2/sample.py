accounts: dict[str, dict] = {
        "1001": {
            "name": "Danusree",
            "password": "Danu123",
            "balance": 15000.0,
            "transactions": [
                "Deposited ₹15000.00"
            ]
        },
        "1002": {
            "name": "Priya",
            "password": "Priya123",
            "balance": 25000.0,
            "transactions": [
                "Deposited ₹25000.00"
            ]
        },
        "1003": {
            "name": "Karthik",
            "password": "Karthik123",
            "balance": 18000.0,
            "transactions": [
                "Deposited ₹18000.00"
            ]
        },
        "1004": {
            "name": "Arun",
            "password": "Arun123",
            "balance": 30000.0,
            "transactions": [
                "Deposited ₹30000.00"
            ]
        },
        "1005": {
            "name": "Meena",
            "password": "Meena123",
            "balance": 12000.0,
            "transactions": [
                "Deposited ₹12000.00"
            ]
        }
    }

def login(accounts: dict[str, dict]) -> str | None:
    print("\nLOGIN")

    account_number = input("Enter account number: ").strip()
    password = input("Enter password: ").strip()

    if account_number not in accounts:
        print("Account not found.")
        return None

    if accounts[account_number]["password"] != password:
        print("Invalid password.")
        return None

    print(f"Welcome {accounts[account_number]['name']}!")
    return account_number


def deposit(accounts: dict[str, dict], account_number: str) -> None:

    amount = float(input("Enter amount to deposit: "))

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    accounts[account_number]["balance"] += amount

    accounts[account_number]["transactions"].append(
        f"Deposited ₹{amount:.2f}"
    )

    print("Amount deposited successfully.")


def withdraw(accounts: dict[str, dict], account_number: str) -> None:

    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    if amount > accounts[account_number]["balance"]:
        print("Insufficient balance.")
        return

    accounts[account_number]["balance"] -= amount

    accounts[account_number]["transactions"].append(
        f"Withdrawn ₹{amount:.2f}"
    )

    print("Amount withdrawn successfully.")


def check_balance(accounts: dict[str, dict], account_number: str) -> None:

    print("\nACCOUNT BALANCE")
    print(f"Name    : {accounts[account_number]['name']}")
    print(f"Balance : ₹{accounts[account_number]['balance']:.2f}")


def transaction_history(
    accounts: dict[str, dict],
    account_number: str
) -> None:

    print("\nTRANSACTION HISTORY")

    transactions = accounts[account_number]["transactions"]

    if not transactions:
        print("No transactions available.")
        return

    for number, transaction in enumerate(transactions, start=1):
        print(f"{number}. {transaction}")


def account_summary(
    accounts: dict[str, dict],
    account_number: str
) -> None:

    print("\n ACCOUNT SUMMARY ")

    account = accounts[account_number]

    print(f"Account Number : {account_number}")
    print(f"Name           : {account['name']}")
    print(f"Balance        : ₹{account['balance']:.2f}")
    print(f"Transactions   : {len(account['transactions'])}")


def display_all_accounts(accounts: dict[str, dict]) -> None:

    print("\n ALL ACCOUNTS")

    for account_number in sorted(accounts):

        account = accounts[account_number]

        print(
            f"{account_number} | "
            f"{account['name']} | "
            f"₹{account['balance']:.2f}"
        )


def password_validator(password: str) -> bool:

    conditions = [
        len(password) >= 6,
        any(char.isupper() for char in password),
        any(char.islower() for char in password),
        any(char.isdigit() for char in password)
    ]

    return all(conditions)


def main() -> None:

    logged_in_account: str | None = None

    while True:

        print("      BANKING APPLICATION")
        print("1. Login")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Account Summary")
        print("7. Display All Accounts")
        print("8. Logout")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()

        match choice:

            case "1":
                logged_in_account = login(accounts)

            case "2":
                if logged_in_account:
                    deposit(accounts, logged_in_account)
                else:
                    print("Please login first.")

            case "3":
                if logged_in_account:
                    withdraw(accounts, logged_in_account)
                else:
                    print("Please login first.")

            case "4":
                if logged_in_account:
                    check_balance(accounts, logged_in_account)
                else:
                    print("Please login first.")

            case "5":
                if logged_in_account:
                    transaction_history(
                        accounts,
                        logged_in_account
                    )
                else:
                    print("Please login first.")

            case "6":
                if logged_in_account:
                    account_summary(
                        accounts,
                        logged_in_account
                    )
                else:
                    print("Please login first.")

            case "7":
                display_all_accounts(accounts)

            case "8":
                logged_in_account = None
                print("Logged out successfully.")

            case "9":
                print("Thank you for using the Banking Application.")
                break

            case _:
                print("Invalid choice.")
main()