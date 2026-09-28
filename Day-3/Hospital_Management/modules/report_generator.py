def generate_patient_report(
    patient: dict,
    bills: list
) -> None:

    patient_bills = [
        bill
        for bill in bills
        if bill["patient_id"] == patient["patient_id"]
    ]

    total_amount = sum(
        bill["total_bill"]
        for bill in patient_bills
    )

    print("\nPATIENT REPORT")
    print("=" * 40)

    print(f"Patient ID : {patient['patient_id']}")
    print(f"Name       : {patient['name']}")
    print(f"City       : {patient['city']}")
    print(f"Age        : {patient['age']}")

    print("\nBILL DETAILS")
    print("-" * 40)

    for bill in patient_bills:

        print(
            f"{bill['bill_id']} | "
            f"{bill['visit_date']} | "
            f"Rs.{bill['total_bill']}"
        )

    print("-" * 40)
    print(f"TOTAL BILL AMOUNT : Rs.{total_amount}")