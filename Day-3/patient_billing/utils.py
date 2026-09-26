def format_currency(amount, currency="INR"):
    if currency.upper() == "INR":
        return f"₹{amount:,.2f}"

    return f"{currency} {amount:,.2f}"

def find_patient(patients, patient_id):
    for patient in patients:
        if patient.get("patient_id", "").upper() == patient_id:
            return patient
    return None

def find_bill(bills, patient_id):
    for bill in bills:
        if bill.get("patient_id", "").upper() == patient_id:
            return bill
    return None

def display_all_patients(patients):
    if not patients:
        print("\nNo patient records available.")
        return

    print("\n")
    print("ALL PATIENTS")

    print(
        f"{'ID':<8}"
        f"{'Name':<22}"
        f"{'Age':<6}"
        f"{'Gender':<10}"
        f"{'Blood':<8}"
        f"{'Doctor':<20}"
        f"{'Admission Date':<15}"
    )

    for patient in patients:
        print(
            f"{patient.get('patient_id', '-'):<8}"
            f"{patient.get('name', '-'):<22}"
            f"{patient.get('age', '-'):<6}"
            f"{patient.get('gender', '-'):<10}"
            f"{patient.get('blood_group', '-'):<8}"
            f"{patient.get('doctor', '-'):<20}"
            f"{patient.get('admission_date', '-'):<15}"
        )

def search_patient(patients):
    if not patients:
        print("\nNo patient records available.")
        return

    search_text = input("\nEnter patient ID or name to search: ").strip().lower()

    if not search_text:
        print("Search value cannot be empty.")
        return

    found = []
    for patient in patients:
        patient_id = str(patient.get("patient_id", "")).lower()
        name = str(patient.get("name", "")).lower()

        if search_text in patient_id or search_text in name:
            found.append(patient)

    if not found:
        print("\nNo matching patient found.")
        return

    print("\nMatching Patients")

    for patient in found:
        print(f"Patient ID : {patient.get('patient_id', '-')}")
        print(f"Name: {patient.get('name', '-')}")
        print(f"Age: {patient.get('age', '-')}")
        print(f"Gender: {patient.get('gender', '-')}")
        print(f"Blood Group: {patient.get('blood_group', '-')}")
        print(f"Doctor: {patient.get('doctor', '-')}")

def view_patient_bill(patients,bills,patient_id,currency="INR"):
    patient = find_patient(patients, patient_id)
    if patient is None:
        print(f"\nNo patient found with ID {patient_id}.")
        return

    bill = find_bill(bills, patient_id)

    if bill is None:
        print(f"\nNo bill found for patient {patient_id}.")
        return

    print("\n")
    print("PATIENT BILL")
    print(f"Patient ID : {patient.get('patient_id', '-')}")
    print(f"Name: {patient.get('name', '-')}")
    print(f"Doctor: {patient.get('doctor', '-')}")

    print(f"Bill ID: "
        f"{bill.get('bill_id', '-')}")

    print(f"Room Charges : "
        f"{format_currency(bill.get('room_charges', 0), currency)}")

    print(f"Doctor Charges : "
        f"{format_currency(bill.get('doctor_charges', 0), currency)}")

    print(f"Medicine Charges : "
        f"{format_currency(bill.get('medicine_charges', 0), currency)}")

    print(f"Lab Charges : "
        f"{format_currency(bill.get('lab_charges', 0), currency)}")

    print(f"Other Charges: "
        f"{format_currency(bill.get('other_charges', 0), currency)}")

    print(f"Total Bill : "
        f"{format_currency(bill.get('total_bill', 0), currency)}")

    print(f"Payment Status : "
        f"{bill.get('payment_status', '-')}")

def generate_patient_report(
    patients,
    bills,
    patient_id,
    currency="INR",
    hospital_name="Hospital"
):
    patient = find_patient(patients, patient_id)
    if patient is None:
        print(f"\nNo patient found with ID {patient_id}.")
        return

    bill = find_bill(bills, patient_id)

    print("\n")
    print(f"{hospital_name.upper()}")
    print(f"{'PATIENT REPORT'}")

    print("\nPATIENT DETAILS")

    print(f"Patient ID : "
        f"{patient.get('patient_id', '-')}")

    print(f"Name : "
        f"{patient.get('name', '-')}")

    print(f"Age : "
        f"{patient.get('age', '-')}")

    print(f"Gender : "
        f"{patient.get('gender', '-')}")

    print(f"Phone : "
        f"{patient.get('phone', '-')}")

    print(f"Address : "
        f"{patient.get('address', '-')}")

    print(f"Blood Group : "
        f"{patient.get('blood_group', '-')}")

    print(f"Admission Date : "
        f"{patient.get('admission_date', '-')}")

    print(f"Doctor           : "
        f"{patient.get('doctor', '-')}")

    print("\nBILL DETAILS")

    if bill is None:
        print("No billing information available.")

    else:
        print(f"Bill ID : "
            f"{bill.get('bill_id', '-')}")

        print(f"Room Charges : "
            f"{format_currency(bill.get('room_charges', 0), currency)}")

        print(f"Doctor Charges : "
            f"{format_currency(bill.get('doctor_charges', 0), currency)}")

        print(f"Medicine Charges : "
            f"{format_currency(bill.get('medicine_charges', 0), currency)}")

        print(f"Lab Charges : "
            f"{format_currency(bill.get('lab_charges', 0), currency)}")

        print(f"Other Charges : "
            f"{format_currency(bill.get('other_charges', 0), currency)}")

        print(f"Total Bill       : "
            f"{format_currency(bill.get('total_bill', 0), currency)}")

        print(f"Payment Status   : "
            f"{bill.get('payment_status', '-')}")

def display_all_bills(bills, currency="INR"):
    if not bills:
        print("\nNo billing records available.")
        return

    print("\n")
    print("ALL BILLS")

    print(
        f"{'Bill ID':<10}"
        f"{'Patient ID':<12}"
        f"{'Total Bill':<18}"
        f"{'Status':<15}"
    )

    for bill in bills:
        total = bill.get("total_bill", 0)

        print(
            f"{bill.get('bill_id', '-'):<10}"
            f"{bill.get('patient_id', '-'):<12}"
            f"{format_currency(total, currency):<18}"
            f"{bill.get('payment_status', '-'):<15}"
        )

def display_bills_by_status(
    bills,
    status,
    currency="INR"
):

    matching_bills = []
    for bill in bills:
        if bill.get("payment_status", "").lower() == status.lower():
            matching_bills.append(bill)

    if not matching_bills:
        print(f"\nNo {status.lower()} bills found.")
        return

    print("\n")
    print(f"{status.upper()} BILLS")

    total = 0
    for bill in matching_bills:
        amount = bill.get("total_bill", 0)
        total += amount
        print(f"Bill ID : {bill.get('bill_id', '-')}")

        print(f"Patient ID : {bill.get('patient_id', '-')}")

        print(f"Amount     : "
            f"{format_currency(amount, currency)}")
        
    print(f"Number of Bills : {len(matching_bills)}")

    print(f"Total Amount    : "
        f"{format_currency(total, currency)}")


def calculate_total_revenue(
    bills,
    currency="INR"
):

    paid_total = 0
    pending_total = 0
    overall_total = 0

    for bill in bills:
        amount = bill.get("total_bill", 0)
        overall_total += amount

        if bill.get("payment_status", "").lower() == "paid":
            paid_total += amount

        elif bill.get("payment_status", "").lower() == "pending":
            pending_total += amount

    print("\n")
    print("BILL SUMMARY")

    print(f"Paid Amount    : "
        f"{format_currency(paid_total, currency)}")

    print(f"Pending Amount : "
        f"{format_currency(pending_total, currency)}")

    print(f"Total Billing  : "
        f"{format_currency(overall_total, currency)}")

def hospital_summary(
    patients,
    bills,
    currency="INR"
):

    total_patients = len(patients)
    total_bills = len(bills)

    paid_bills = 0
    pending_bills = 0

    paid_amount = 0
    pending_amount = 0

    for bill in bills:
        amount = bill.get("total_bill", 0)

        if bill.get("payment_status", "").lower() == "paid":
            paid_bills += 1
            paid_amount += amount

        elif bill.get("payment_status", "").lower() == "pending":
            pending_bills += 1
            pending_amount += amount

    print("\n")
    print("HOSPITAL SUMMARY")
    print(f"Total Patients : {total_patients}")
    print(f"Total Bills : {total_bills}")
    print(f"Paid Bills : {paid_bills}")
    print(f"Pending Bills : {pending_bills}")

    print(f"Paid Amount: "
        f"{format_currency(paid_amount, currency)}")

    print(f"Pending Amount: "
        f"{format_currency(pending_amount, currency)}")

    print(f"Total Billing: "
        f"{format_currency(paid_amount + pending_amount, currency)}")