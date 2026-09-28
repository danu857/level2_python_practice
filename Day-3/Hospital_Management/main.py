from dotenv import load_dotenv
from pathlib import Path
import os

from modules.config import load_json
from modules.report_generator import generate_patient_report
from modules.append_bill import add_bill


load_dotenv()

PATIENTS_FILE = os.getenv("PATIENTS_FILE")
BILLS_FILE = os.getenv("BILLS_FILE")

def view_patients(patients: list) -> None:
    print("\nPATIENT LIST")

    for patient in patients:
        print(
            patient["patient_id"],
            patient["name"],
            patient["city"]
        )


def view_bills(bills: list) -> None:
    print("\nBILL LIST")

    for bill in bills:
        print(
            bill["bill_id"],
            bill["patient_id"],
            bill["total_bill"]
        )


def search_patient(
    patients: list,
    patient_id: str
) -> dict | None:

    for patient in patients:
        if patient["patient_id"] == patient_id:
            return patient
    return None


def highest_bill_report(
    patients: list,
    bills: list
) -> None:

    highest_bill = max(
        bills,
        key=lambda bill: bill["total_bill"])

    patient = search_patient(
        patients,
        highest_bill["patient_id"])

    print("\nHIGHEST BILL REPORT")
    print("Bill ID :", highest_bill["bill_id"])
    print("Patient :", patient["name"])
    print("Amount  :", highest_bill["total_bill"])


def revenue_report(bills: list) -> None:
    total_revenue = sum(bill["total_bill"]for bill in bills)
    print("\nTOTAL REVENUE")
    print(f"Rs.{total_revenue}")


def main():
    patients = load_json(PATIENTS_FILE)
    bills = load_json(BILLS_FILE)

    while True:
        print("\nHOSPITAL MANAGEMENT")
        print("1. View All Patients")
        print("2. View All Bills")
        print("3. Search Patient")
        print("4. Generate Patient Report")
        print("5. Highest Bill Report")
        print("6. Revenue Report")
        print("7. Add Bill")
        print("8. Exit")

        try:
            choice = int(input("\nEnter choice : "))

            match choice:
                case 1:
                    view_patients(patients)

                case 2:
                    view_bills(bills)

                case 3:
                    patient_id = input("Enter Patient ID : ").upper()
                    patient = search_patient(patients,patient_id)

                    if patient:
                        print(patient)
                    else:
                        print("Patient not found")

                case 4:
                    patient_id = input("Enter Patient ID : ").upper()
                    patient = search_patient(patients,patient_id)
                    if patient:
                        generate_patient_report(patient,bills)

                    else:
                        print("Patient not found")

                case 5:
                    highest_bill_report(patients,bills)

                case 6:
                    revenue_report(bills)

                case 7:
                    add_bill(bills,BILLS_FILE)

                case 8:
                    print("Thank You")
                    break

                case _:
                    print("Invalid choice")

        except ValueError:
            print("Enter numbers only")

        except Exception as error:
            print(error)

if __name__ == "__main__":
    main()