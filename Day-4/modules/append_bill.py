from dataclasses import dataclass,asdict,field
from modules.config import FileHandler

@dataclass
class Bill:
    bill_id: str
    patient_id: str
    visit_date: str
    doctor_fee: float
    lab_fee: float
    medicine_fee: float
    room_charge: float
    total_bill: float = field(init=False)

    def __post_init__(self):
        self.total_bill = (
            self.doctor_fee
            + self.lab_fee
            + self.medicine_fee
            + self.room_charge)

class BillManager:
    def __init__(self,bills: list,bill_file: str):
        self.bills = bills
        self.bill_file = bill_file

    def add_bill(self) -> None:
        patient_id = input("Enter Patient ID : ").upper()
        doctor_fee = float(input("Doctor Fee : "))
        lab_fee = float(input("Lab Fee : "))
        medicine_fee = float(input("Medicine Fee : "))
        room_charge = float(input("Room Charge : "))
        bill_id = f"B{len(self.bills) + 1:03}"
        new_bill = Bill(
            bill_id=bill_id,
            patient_id=patient_id,
            visit_date=input("Visit Date (YYYY-MM-DD): "),
            doctor_fee=doctor_fee,
            lab_fee=lab_fee,
            medicine_fee=medicine_fee,
            room_charge=room_charge)
        self.bills.append(asdict(new_bill))

        FileHandler.save_json(self.bill_file,self.bills)
        print("Bill added successfully.")

def add_bill(bills: list,bill_file: str) -> None:
    bill_manager = BillManager(bills,bill_file)
    bill_manager.add_bill()