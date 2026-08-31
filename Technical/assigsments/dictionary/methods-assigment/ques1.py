# 1.ASSIGNMENT: HOSPITAL PATIENT RECORD MANAGEMENT SYSTEM:--

# A multi-specialty hospital is currently maintaining patient records manually in registers. As the number of patients is increasing, it has become difficult to search, update, and manage records efficiently.

# The hospital management has decided to develop a simple Patient Record Management System using Python. The system should store patient information in a nested dictionary where:

# Key → Patient ID
# Value → Dictionary containing patient details

# Each patient record should contain:

# Patient Name
# Age
# Gender
# Disease
# Doctor Name
# Sample Data Structure
# {
# 101:{
#     "name":"Ajay",
#     "age":35,
#     "gender":"Male",
#     "disease":"Fever",
#     "doctor":"Dr. Sharma"
# },
# 102:{
#     "name":"Ravi",
#     "age":42,
#     "gender":"Male",
#     "disease":"Diabetes",
#     "doctor":"Dr. Gupta"
# }
# }
# Menu Driven Program

# Display the following menu repeatedly until the user chooses Exit.

# =====================================
#  HOSPITAL PATIENT MANAGEMENT SYSTEM
# =====================================

# 1. Add New Patient
# 2. Search Patient
# 3. Update Patient Disease
# 4. Delete Patient Record
# 5. Display All Patients
# 6. Count Total Patients
# 7. Display Patients By Disease
# 8. Display Oldest Patient
# 9. Display Youngest Patient
# 10. Exit

# Functional Requirements
# 1. Add New Patient

# Accept the following information from the user:

# Patient ID
# Patient Name
# Age
# Gender
# Disease
# Doctor Name

# Store the record in the nested dictionary.

# Validation:
# If the Patient ID already exists, display:

# Patient ID already exists.

# 2. Search Patient

# Accept Patient ID from the user.

# If the patient exists, display complete information.

# Sample Output

# Patient ID : 101
# Name       : Ajay
# Age        : 35
# Gender     : Male
# Disease    : Fever
# Doctor     : Dr. Sharma

# If Patient ID is not found:

# Patient Record Not Found

# 3. Update Patient Disease

# Accept Patient ID.

# If found:

# Ask for new disease.
# Update the disease information.

# Sample Output

# Disease Updated Successfully
# 4. Delete Patient Record

# Accept Patient ID.

# If found:

# Remove the patient record.

# Sample Output

# Patient Record Deleted Successfully

# Otherwise:

# Patient Not Found
# 5. Display All Patients

# Display all patient records in a formatted manner.

# Sample Output

# --------------------------------
# Patient ID : 101
# Name       : Ajay
# Age        : 35
# Disease    : Fever
# Doctor     : Dr. Sharma
# --------------------------------

# Patient ID : 102
# Name       : Ravi
# Age        : 42
# Disease    : Diabetes
# Doctor     : Dr. Gupta
# 6. Count Total Patients

# Display the total number of patients currently stored.

# Sample Output

# Total Patients : 25
# 7. Display Patients By Disease

# Accept a disease name from the user.

# Display all patients suffering from that disease.

# Sample Output

# Enter Disease : Fever

# 101  Ajay
# 108  Aman
# 115  Neha

# If no patient is found:

# No Patient Found
# 8. Display Oldest Patient

# Find and display the patient having the highest age.

# Sample Output

# Oldest Patient Details

# Patient ID : 110
# Name       : Ravi
# Age        : 68
# Disease    : Diabetes
# Doctor     : Dr. Gupta
# 9. Display Youngest Patient

# Find and display the patient having the minimum age.

# Sample Output

# Youngest Patient Details

# Patient ID : 121
# Name       : Riya
# Age        : 4
# Disease    : Viral Fever
# Doctor     : Dr. Mehta
# 10. Exit

# Terminate the application.

# Sample Output

# Thank You For Using Hospital Patient Management System



patients={
    101: {
        "name": "Ajay",
        "age": 35,
        "gender": "Male",
        "disease": "Fever",
        "doctor": "Dr. Sharma"
    },
    102: {
        "name": "Ravi",
        "age": 42,
        "gender": "Male",
        "disease": "Diabetes",
        "doctor": "Dr. Gupta"
    },
    103: {
        "name": "Priya",
        "age": 28,
        "gender": "Female",
        "disease": "Migraine",
        "doctor": "Dr. Mehta"
    },
    104: {
        "name": "Vikram",
        "age": 51,
        "gender": "Male",
        "disease": "Blood Pressure",
        "doctor": "Dr. Verma"
    },
    105: {
        "name": "Neha",
        "age": 31,
        "gender": "Female",
        "disease": "Asthma",
        "doctor": "Dr. Singh"
    },
    106: {
        "name": "Rohit",
        "age": 45,
        "gender": "Male",
        "disease": "Heart Disease",
        "doctor": "Dr. Kapoor"
    },
    107: {
        "name": "Anjali",
        "age": 24,
        "gender": "Female",
        "disease": "Fever",
        "doctor": "Dr. Sharma"
    },
    108: {
        "name": "Karan",
        "age": 38,
        "gender": "Male",
        "disease": "Diabetes",
        "doctor": "Dr. Gupta"
    },
    109: {
        "name": "Sneha",
        "age": 29,
        "gender": "Female",
        "disease": "Thyroid",
        "doctor": "Dr. Mehta"
    },
    110: {
        "name": "Manish",
        "age": 56,
        "gender": "Male",
        "disease": "Blood Pressure",
        "doctor": "Dr. Verma"
    }
}
while True:
    print( "=====================================")
    print("HOSPITAL PATIENT MANAGEMENT SYSTEM")
    print( "=====================================")
    print('''
     1. Add New Patient \n
     2. Search Patient  \n
     3. Update Patient Disease  \n
     4. Delete Patient Record  \n
     5. Display All Patients  \n
     6. Count Total Patients  \n
     7. Display Patients By Disease  \n
     8. Display Oldest Patient  \n
     9. Display Youngest Patient  \n
     10. Exit''')
    choice  = input("Enter the your choice")
    match choice:
         case "1":
             print("Entering the new patient ....")
             pid =int(input("Enter the patient id ..."))
             pname= input("Enter the patient name ...")
             page = int(input("Enter the patient age ..."))
             pgender = input("Enter the patient gender ...")
             pdisease=input("ENter the disease ....")
             pdoctname = input("Enter the doctor name ...")

             if pid not in patients:
                  patients.update({pid :{
                        "name":pname,
                        "age":page,
                        "gender":pgender,
                        "disease":pdisease,
                        "doctor":pdisease
                       }})
             else:
                  print("Patient is already exists")
         case "2":
             print("Wellcome to search patient section .....")
             pid =  int(input("Enter the patient id ..."))
             if  pid in patients:
                    patient =  patients[pid]
                    for k,v in patient.items():
                         print(f"{k} : {v}")
             else:
                  print("patient id not in record ...")
         case "3":
            print("Wellcome to update patient desies secction .....")
            pid =  int(input("Enter the patient id ..."))
            if  pid in patients:
                  newdise = input("Enter the desies of patient...")
                  patients[pid]["disease"] =  newdise
                  print("Disease updated successfully ...")
            else:
                 print("patient id not in record ...")
         case "4":
              pid =  int(input("Enter the patient id ..."))
              if  pid in patients:
                   del patients[pid]
                   print(patients)
              else:
                   print("patient id not in record ...")
              
         case "5":
              if not patients:
                    print("Dictionary is already Empty ...")
              else:
                    patients.clear()
         case "6":
             print("Total patient count ",len(patients))
         case "7":
            print("Wellcome to Display Patients By Disease ")
            pid =  int(input("Enter the patient id ...."))
            if pid in patients:
               des=input("Enter the disease .....")
               for k,v in patients.items():
                    if patients[k]["disease"] == des  and pid == k:
                         for i,j in patients[k].items():
                              print(f" {i} : {j} ")
            else:
                 print("Invalid user id ....")
         case "8":
              print("wellcome to seen first patient funtionlity ....")
              for i,j in patients.items():
                   for k,v in i.iteams():
                        print(f" {k} : {v} ")
                        print
                   break
         case "9":
               print("wellcome to display last inserted  patient funtionlity ....")
               key,valus = patients.popitem()
               for k,v in valus.items():
                     print(f" {k} : {v} ")
               patients[key]=valus
            
         case "10":
              print("Thank You For Using Hospital Patient Management System😎😎👍👍")
              break
         case __:
             print("Enter the Vaild Choice ")