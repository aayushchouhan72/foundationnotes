# =====================================================================
# QUESTION 3: HOSPITAL PATIENT TRACKER
# ====================================

# A hospital stores patient records for daily monitoring.

# Fields:
# patient_id, patient_name, age, disease

# Requirements:

# 1. Read N patient records from the user and store them in a list of NamedTuples.

# ---

# 2. Display all patient details.

# ---

# 3. Display patients whose age is above 60 years.

# ---

# 4. Search for a patient using Patient ID.

# ---

# 5. Count the number of patients suffering from a particular disease.

# ---

# Test Case:

# Input:
# Enter number of patients: 4

# P101 Rajesh 65 Diabetes
# P102 Suman 45 Fever
# P103 Mohan 70 Diabetes
# P104 Rita 35 Cold

# Enter Patient ID: P103
# Enter Disease: Diabetes

# Expected Output:
# Patient Found:
# P103 Mohan 70 Diabetes

# Patients Above 60:
# P101 Rajesh 65 Diabetes
# P103 Mohan 70 Diabetes

# Patients with Diabetes:
# 2



from collections import namedtuple 

student =  namedtuple("Student",["patient_id", "patient_name", "age", "disease"])

lis=[]

number =  int(input("Enter the number of patient "))

print()
for i in range(number):
    print()
    patient_id = int(input("Enter patient id ...."))
    patient_name =  input("Enter Patient Name ....")
    age = int(input("Enter the patient age ...."))
    disease = input("Enter disease name ....")
    lis.append(student(patient_id,patient_name,age,disease))
    print()
patentabove60=[]

print(".................. Enter data to find patient .............")
patentid= int(input("Enter patient id ...."))
disea= input("Enter the disease ....")
diseacount=0
foundpatient=None
for i  in lis:
     print(i.patient_id,i.patient_name,i.age,i.disease)
     if i.age>60:
          patentabove60.append(i)
     if disease == disea:
          diseacount+=1
     if patentid == i.patient_id and disease == disea:
          foundpatient=i
     print()

print(f"patient suffred by diseas is {diseacount} and found patent is {foundpatient}")
