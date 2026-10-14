# # Assignment: Hospital Management System Using Python Packages and Modules

# # Problem Statement:

# # Develop a menu-driven Hospital Management System application in Python.

# # The application should be developed using proper packages and modules.
# # Do not write the complete program in a single file. Divide the application
# # into different packages based on functionality.

# # Project Structure:

# # HospitalManagement/

# #     main.py

# #     patient/
# #         __init__.py
# #         patient_module.py

# #     doctor/
# #         __init__.py
# #         doctor_module.py

# #     appointment/
# #         __init__.py
# #         appointment_module.py

# #     billing/
# #         __init__.py
# #         billing_module.py


# # Requirements:

# # 1. Patient Management Package

# # Create a package named "patient".

# # Create module:
# # patient_module.py


# # Implement the following functions:

# # a) add_patient()

# # Take patient details from user:

# # - Patient ID
# # - Patient Name
# # - Age
# # - Gender
# # - Disease
# # - Mobile Number


# # Store patient information using list and dictionary.


# # b) display_patients()

# # Display all registered patients.


# # c) search_patient()

# # Search patient details using Patient ID.


# # --------------------------------------------------


# 2. Doctor Management Package

# Create a package named "doctor".

# Create module:
# doctor_module.py


# Implement the following functions:


# a) add_doctor()

# Take doctor details:

# - Doctor ID
# - Doctor Name
# - Specialization
# - Experience
# - Consultation Fees


# Store doctor information using list and dictionary.


# b) display_doctors()

# Display all doctor details.


# --------------------------------------------------


# 3. Appointment Management Package

# Create a package named "appointment".

# Create module:
# appointment_module.py


# Implement:


# a) book_appointment()

# Take appointment details:

# - Appointment ID
# - Patient ID
# - Doctor ID
# - Appointment Date
# - Appointment Time


# Store appointment information.


# b) show_appointments()

# Display all booked appointments.


# --------------------------------------------------


# 4. Billing Package

# Create a package named "billing".

# Create module:
# billing_module.py


# Implement:


# generate_bill()


# Take:

# - Patient ID
# - Consultation Charges
# - Medicine Cost
# - Test Charges


# Calculate total amount:

# Total Bill = Consultation Charges + Medicine Cost + Test Charges


# Display complete bill.


# --------------------------------------------------


# 5. Main Application

# Create main.py file.

# Create a menu-driven program.


# Menu:

# ========== Hospital Management System ==========

# 1. Add Patient

# 2. Display Patients

# 3. Search Patient

# 4. Add Doctor

# 5. Display Doctors

# 6. Book Appointment

# 7. Show Appointments

# 8. Generate Bill

# 9. Exit


# According to user choice call the required functions from packages.


# --------------------------------------------------


import patient as p
import billing as b
import doctor as d
import appointment as a


patient=[]
doctor=[]
bills=[]
appoinment=[]
while True:
     print("""
1. Add Patient
2. Display Patient
3. Search Patien
4. Add Docto
5. Display Doctor
6. Book Appointmen
7. Show Appointment
8. Generate Bil
9. Exit
""")
     choice = input("Enter the choice ...")
     match choice:
          case "1":
               patient.append(p.add_patient())
          case "2":
               p.display_patient(patient)
          case "3":
               find=int(input("Enter the patient id "))
               p.search_patient(patient,find)
          case "4":
               doctor.append(d.add_doctor())
          case "5":
               d.display_doctor(doctor)
          case "6":
               appoinment.append(a.book_appointment())
          case "7":
               a.show_appointments(appoinment)
          case "8":
               bills.append(b.generate_bill())
          case "9":
               print("Thankyou for using an application...")
               break

     
