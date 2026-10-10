# 3============================================================
# QUESTION 2: HOSPITAL PATIENT BILLING SYSTEM
# ============================================================

# Develop a MENU-DRIVEN Hospital Patient Billing System.

# The hospital treats different categories of patients:

# 1. General Patient
# 2. Emergency Patient
# 3. Insurance Patient
# 4. Corporate Patient

# Every patient must perform common operations such as:

# calculate_bill()
# calculate_discount()
# calculate_final_amount()
# generate_bill()

# However, the calculation rules are different for each type
# of patient.

# Therefore, use ABSTRACTION to design the system.

# ------------------------------------------------------------
# ABSTRACT CLASS:
# ------------------------------------------------------------

# Create an abstract class:

# Patient

# It should contain appropriate abstract methods required for
# billing.

# Create the following child classes:

# 1. GeneralPatient
# 2. EmergencyPatient
# 3. InsurancePatient
# 4. CorporatePatient

# ------------------------------------------------------------
# MAIN MENU:
# ------------------------------------------------------------

# ========================================
#        HOSPITAL MANAGEMENT SYSTEM
# ========================================

# 1. Register Patient
# 2. Generate Patient Bill
# 3. View Patient Bill
# 4. Exit

# Enter your choice:

# ------------------------------------------------------------
# OPTION 1: REGISTER PATIENT
# ------------------------------------------------------------

# Input:

# Patient ID
# Patient Name
# Patient Age

# Then display:

# 1. General Patient
# 2. Emergency Patient
# 3. Insurance Patient
# 4. Corporate Patient

# Enter patient type:

# ------------------------------------------------------------
# GENERAL PATIENT:
# ------------------------------------------------------------

# Consultation Fee : Rs.500
# Room Charge       : Rs.1000 per day
# Medicine Charge   : Actual amount
# Discount          : No discount

# Input:

# Number of Days
# Medicine Charge

# ------------------------------------------------------------
# EMERGENCY PATIENT:
# ------------------------------------------------------------

# Consultation Fee : Rs.1000
# Emergency Charge : Rs.500
# Room Charge       : Rs.2000 per day
# Medicine Charge   : Actual amount
# Discount          : No discount

# Input:

# Number of Days
# Medicine Charge

# ------------------------------------------------------------
# INSURANCE PATIENT:
# ------------------------------------------------------------

# Consultation Fee : Rs.800
# Room Charge       : Rs.1500 per day
# Medicine Charge   : Actual amount

# Insurance covers 70% of the total hospital bill.

# Patient pays remaining 30%.

# Input:

# Number of Days
# Medicine Charge

# ------------------------------------------------------------
# CORPORATE PATIENT:
# ------------------------------------------------------------

# Consultation Fee : Rs.700
# Room Charge       : Rs.1200 per day
# Medicine Charge   : Actual amount

# Corporate Discount = 20%

# Input:

# Number of Days
# Medicine Charge

# ------------------------------------------------------------
# SAMPLE INPUT:
# ------------------------------------------------------------

# Enter Patient ID: P1025
# Enter Patient Name: Rajesh
# Enter Patient Age: 42

# Select Patient Type:

# 1. General
# 2. Emergency
# 3. Insurance
# 4. Corporate

# Enter choice: 3

# Enter Number of Days: 4
# Enter Medicine Charge: 3500

# ------------------------------------------------------------
# EXPECTED OUTPUT:
# ------------------------------------------------------------

# ========================================
#             PATIENT BILL
# ========================================

# Patient ID       : P1025
# Patient Name     : Rajesh
# Patient Age      : 42
# Patient Type     : Insurance

# Consultation Fee : Rs.800.00
# Room Charges     : Rs.6000.00
# Medicine Charges : Rs.3500.00

# ----------------------------------------

# Total Hospital Bill : Rs.10300.00

# Insurance Coverage  : 70%
# Insurance Amount    : Rs.7210.00

# Patient Payable     : Rs.3090.00

# Bill Status         : GENERATED

# ========================================

# ------------------------------------------------------------
# OPTION 2: GENERATE PATIENT BILL
# ------------------------------------------------------------

# Ask:

# Enter Patient ID:

# If patient exists, generate and display the bill according
# to the patient's type.

# The calculation must be performed by the appropriate child
# class.

# ------------------------------------------------------------
# OPTION 3: VIEW PATIENT BILL
# ------------------------------------------------------------

# Ask:

# Enter Patient ID:

# Display the complete patient bill.

# If patient does not exist:

# Patient record not found.

# ------------------------------------------------------------
# OPTION 4:
# ------------------------------------------------------------

# Display:

# Thank you for using Hospital Management System.


from hospital_mang.hospital import (
    GeneralPatient,
    EmergencyPatient,
    InsurancePatient,
    CorporatePatient
)


patients = {}


def register_patient():

    print("\n========================================")
    print("          REGISTER PATIENT")
    print("========================================")

    patient_id = input("Enter Patient ID: ")
    patient_name = input("Enter Patient Name: ")
    patient_age = int(input("Enter Patient Age: "))

    print("\nSelect Patient Type")

    print("1. General")
    print("2. Emergency")
    print("3. Insurance")
    print("4. Corporate")

    choice = input("Enter choice: ")

    days = int(input("Enter Number of Days: "))
    medicine_charge = float(input("Enter Medicine Charge: "))

    patient = None

    if choice == "1":

        patient = GeneralPatient(
            patient_id,
            patient_name,
            patient_age,
            days,
            medicine_charge
        )

    elif choice == "2":

        patient = EmergencyPatient(
            patient_id,
            patient_name,
            patient_age,
            days,
            medicine_charge
        )

    elif choice == "3":

        patient = InsurancePatient(
            patient_id,
            patient_name,
            patient_age,
            days,
            medicine_charge
        )

    elif choice == "4":

        patient = CorporatePatient(
            patient_id,
            patient_name,
            patient_age,
            days,
            medicine_charge
        )

    else:

        print("Invalid patient type.")
        return

    patients[patient_id] = patient

    print("\nPatient registered successfully.")


def display_bill(patient):

    print("\n========================================")
    print("            PATIENT BILL")
    print("========================================")

    print(f"Patient ID       : {patient.patient_id}")
    print(f"Patient Name     : {patient.patient_name}")
    print(f"Patient Age      : {patient.patient_age}")
    print(f"Patient Type     : {patient.patient_type}")

    print(f"\nConsultation Fee : Rs.{patient.consultation_fee:.2f}")
    print(f"Room Charges     : Rs.{patient.room_charges:.2f}")
    print(f"Medicine Charges : Rs.{patient.medicine_charge:.2f}")

    if isinstance(patient, EmergencyPatient):

        print(f"Emergency Charge : Rs.{patient.emergency_charge:.2f}")

    print("\n----------------------------------------")

    print(f"Total Hospital Bill : Rs.{patient.total_bill:.2f}")

    if isinstance(patient, InsurancePatient):

        print("\nInsurance Coverage  : 70%")
        print(f"Insurance Amount    : Rs.{patient.insurance_amount:.2f}")
        print(f"\nPatient Payable     : Rs.{patient.final_amount:.2f}")

    elif isinstance(patient, CorporatePatient):

        print("\nCorporate Discount   : 20%")
        print(f"Discount Amount      : Rs.{patient.discount_amount:.2f}")
        print(f"\nPatient Payable     : Rs.{patient.final_amount:.2f}")

    else:

        print(f"\nDiscount            : Rs.{patient.discount:.2f}")
        print(f"Patient Payable     : Rs.{patient.final_amount:.2f}")

    print(f"\nBill Status         : {patient.bill_status}")

    print("========================================")


def generate_patient_bill():

    patient_id = input("\nEnter Patient ID: ")

    if patient_id not in patients:

        print("Patient record not found.")
        return

    patient = patients[patient_id]

    # Polymorphism
    patient.generate_bill()

    display_bill(patient)


def view_patient_bill():

    patient_id = input("\nEnter Patient ID: ")

    if patient_id not in patients:

        print("Patient record not found.")
        return

    patient = patients[patient_id]

    if patient.bill_status != "GENERATED":

        print("Bill has not been generated yet.")
        return

    display_bill(patient)


def main():

    while True:

        print("\n========================================")
        print("       HOSPITAL MANAGEMENT SYSTEM")
        print("========================================")

        print("1. Register Patient")
        print("2. Generate Patient Bill")
        print("3. View Patient Bill")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            register_patient()

        elif choice == "2":

            generate_patient_bill()

        elif choice == "3":

            view_patient_bill()

        elif choice == "4":

            print("\nThank you for using Hospital Management System.")
            break

        else:

            print("Invalid choice.")


main()