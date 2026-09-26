import json
import os
from pathlib import Path
from dotenv import load_dotenv
from utils import *

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
PATIENTS_FILE = BASE_DIR / os.getenv("PATIENTS_FILE", "data/patients.json")
BILLS_FILE = BASE_DIR / os.getenv("BILLS_FILE", "data/total_bills.json")
HOSPITAL_NAME = os.getenv("HOSPITAL_NAME", "Hospital")
CURRENCY = os.getenv("CURRENCY", "INR")

def load_json_file(file_path):
    try:
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        if not file_path.is_file():
            raise OSError(f"Path is not a file: {file_path}")

        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError(f"Expected a JSON list in {file_path}")
        return data

    except FileNotFoundError as error:
        print(f"\nError: {error}")
        return []

    except json.JSONDecodeError as error:
        print(f"\nError: Invalid JSON in {file_path}")
        print(f"Details: {error}")
        return []

    except PermissionError:
        print(f"\nError: Permission denied while reading "
            f"{file_path}"
        )
        return []

    except OSError as error:
        print(f"\nFile error: {error}")
        return []

    except ValueError as error:
        print(f"\nData error: {error}")
        return []

def get_patient_id():
    patient_id = input("Enter patient ID (example: P001): ").strip().upper()

    if not patient_id:
        print("Patient ID cannot be empty.")
        return None
    return patient_id


def get_menu_choice():
    try:
        choice = int(input("\nEnter your choice: ").strip())
        return choice

    except ValueError:
        print("Please enter a valid number.")
        return None

def display_menu():
    print("\n")
    print("=" * 20)
    print(f"{HOSPITAL_NAME.upper()}")
    print("PATIENT BILLING SYSTEM")
    print("=" * 20)

    print("1. Display All Patients")
    print("2. Search Patient")
    print("3. View Patient Bill")
    print("4. Generate Patient Report")
    print("5. Display All Bills")
    print("6. Add New Bill")
    print("7. Display Hospital Summary")
    print("0. Exit")

    print("=" * 20)

def main():
    print("\nLoading hospital data...")
    # Load constant patient data.
    patients = load_json_file(PATIENTS_FILE)
    # Load billing data.
    bills = load_json_file(BILLS_FILE)

    if not patients:
        print("Warning: Patient data could not be loaded.")

    if not bills:
        print("Warning: Billing data could not be loaded.")

    while True:

        display_menu()
        choice = get_menu_choice()
        if choice is None:
            continue

        if choice == 1:
            display_all_patients(patients)

        elif choice == 2:
            search_patient(patients)

        elif choice == 3:
            patient_id = get_patient_id()

            if patient_id:
                view_patient_bill(
                    patients,
                    bills,
                    patient_id,
                    CURRENCY
                )

        elif choice == 4:
            patient_id = get_patient_id()

            if patient_id:
                generate_patient_report(
                    patients,
                    bills,
                    patient_id,
                    CURRENCY,
                    HOSPITAL_NAME
                )

        elif choice == 5:
            display_all_bills(bills,CURRENCY)

        elif choice == 6:
            display_bills_by_status(bills,"Paid",CURRENCY)

        elif choice == 7:
            display_bills_by_status(bills,"Pending",CURRENCY)

        elif choice == 8:
            calculate_total_revenue(bills,CURRENCY)

        elif choice == 9:
            hospital_summary(patients,bills,CURRENCY)

        elif choice == 0:
            print("\nThank you for using the system.")
            print("Program terminated.")
            break

        else:
            print(
                "\nInvalid choice. "
                "Please select a number from 0 to 9."
            )

if __name__ == "__main__":
    main()