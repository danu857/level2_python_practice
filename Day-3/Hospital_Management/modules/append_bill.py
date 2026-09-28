import json
from pathlib import Path

def add_bill(bills: list,bill_file: str) -> None:
    patient_id = input("Enter Patient ID : ").upper()
    doctor_fee = float(input("Doctor Fee : "))
    lab_fee = float(input("Lab Fee : "))
    medicine_fee = float(input("Medicine Fee : "))
    room_charge = float(input("Room Charge : "))
    total_bill = (doctor_fee+ lab_fee + medicine_fee + room_charge)
    bill_id = f"B{len(bills)+1:03}"

    new_bill = {
        "bill_id": bill_id,
        "patient_id": patient_id,
        "visit_date": input("Visit Date (YYYY-MM-DD): "),
        "doctor_fee": doctor_fee,
        "lab_fee": lab_fee,
        "medicine_fee": medicine_fee,
        "room_charge": room_charge,
        "total_bill": total_bill
    }

    bills.append(new_bill)

    path = Path(bill_file)

    with path.open("w",encoding="utf-8") as file:

        json.dump(bills,file,indent=4)

    print("Bill added successfully.")