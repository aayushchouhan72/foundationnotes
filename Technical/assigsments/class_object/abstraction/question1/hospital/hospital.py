
from abc import ABC,abstractmethod
class Patient():
    def __init__(self,Patient_ID,Patient_Name,Patient_Age):
        self.Patient_ID=Patient_ID
        self.Patient_Name=Patient_Name
        self.Patient_Age=Patient_Age
       
    @abstractmethod
    def calculate_bill():
        pass 
    @abstractmethod
    def calculate_discount():
        pass 
    @abstractmethod
    def calculate_final_amount():
        pass 
    @abstractmethod
    def generate_bill():
        pass 

class GeneralPatient(Patient):

    def calculate_bill():
        pass 

    def calculate_discount():
        pass 

    def calculate_final_amount():
        pass 

    def generate_bill():
        print("""========================================
                                PATIENT BILL
                ========================================""")
        print("Patient ID       : ")
        print("Patient Name     :")
        print("Patient Age      : ")


class EmergencyPatient(Patient):
    def calculate_bill():
        pass 

    def calculate_discount():
        pass 

    def calculate_final_amount():
        pass 

    def generate_bill():
        pass 

class InsurancePatient(Patient):
    def calculate_bill():
        pass 

    def calculate_discount():
        pass 

    def calculate_final_amount():
        pass 

    def generate_bill():
        pass 

class CorporatePatient(Patient):
    def calculate_bill():
        pass 

    def calculate_discount():
        pass 

    def calculate_final_amount():
        pass 

    def generate_bill():
        pass 

