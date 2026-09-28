from dataclasses import dataclass


@dataclass
class Patient:

    patient_id: str
    name: str
    age: int
    gender: str
    blood_group: str
    phone: str
    city: str


class ReportGenerator:

    @staticmethod
    def generate_patient_report(
        patient: dict,
        bills: list
    ) -> None:

        patient_object = Patient(
            patient_id=patient["patient_id"],
            name=patient["name"],
            age=patient["age"],
            gender=patient["gender"],
            blood_group=patient["blood_group"],
            phone=patient["phone"],
            city=patient["city"]
        )

        patient_bills = [
            bill
            for bill in bills
            if bill["patient_id"]
            == patient_object.patient_id
        ]

        total_amount = sum(
            bill["total_bill"]
            for bill in patient_bills
        )

        print("\nPATIENT REPORT")
        print("=" * 40)

        print(
            f"Patient ID : "
            f"{patient_object.patient_id}"
        )

        print(
            f"Name       : "
            f"{patient_object.name}"
        )

        print(
            f"City       : "
            f"{patient_object.city}"
        )

        print(
            f"Age        : "
            f"{patient_object.age}"
        )

        print("\nBILL DETAILS")
        print("-" * 40)

        for bill in patient_bills:

            print(
                f"{bill['bill_id']} | "
                f"{bill['visit_date']} | "
                f"Rs.{bill['total_bill']}"
            )

        print()

        print(
            f"TOTAL BILL AMOUNT : "
            f"Rs.{total_amount}"
        )


def generate_patient_report(
    patient: dict,
    bills: list
) -> None:

    ReportGenerator.generate_patient_report(
        patient,
        bills
    )