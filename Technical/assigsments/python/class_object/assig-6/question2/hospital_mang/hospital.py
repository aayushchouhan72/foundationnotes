from abc import ABC, abstractmethod


class Patient(ABC):

    def __init__(self, patient_id, patient_name, patient_age,
                 days, medicine_charge):

        self.patient_id = patient_id
        self.patient_name = patient_name
        self.patient_age = patient_age
        self.days = days
        self.medicine_charge = medicine_charge

        self.consultation_fee = 0
        self.room_charges = 0
        self.total_bill = 0
        self.discount = 0
        self.final_amount = 0
        self.bill_status = "NOT GENERATED"

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def calculate_discount(self):
        pass

    @abstractmethod
    def calculate_final_amount(self):
        pass

    @abstractmethod
    def generate_bill(self):
        pass


class GeneralPatient(Patient):

    def __init__(self, patient_id, patient_name, patient_age,
                 days, medicine_charge):

        super().__init__(
            patient_id,
            patient_name,
            patient_age,
            days,
            medicine_charge
        )

        self.patient_type = "General"

    def calculate_bill(self):

        self.consultation_fee = 500
        self.room_charges = self.days * 1000

        self.total_bill = (
            self.consultation_fee +
            self.room_charges +
            self.medicine_charge
        )

    def calculate_discount(self):

        self.discount = 0

    def calculate_final_amount(self):

        self.final_amount = self.total_bill - self.discount

    def generate_bill(self):

        self.calculate_bill()
        self.calculate_discount()
        self.calculate_final_amount()

        self.bill_status = "GENERATED"


class EmergencyPatient(Patient):

    def __init__(self, patient_id, patient_name, patient_age,
                 days, medicine_charge):

        super().__init__(
            patient_id,
            patient_name,
            patient_age,
            days,
            medicine_charge
        )

        self.patient_type = "Emergency"
        self.emergency_charge = 500

    def calculate_bill(self):

        self.consultation_fee = 1000
        self.room_charges = self.days * 2000

        self.total_bill = (
            self.consultation_fee +
            self.emergency_charge +
            self.room_charges +
            self.medicine_charge
        )

    def calculate_discount(self):

        self.discount = 0

    def calculate_final_amount(self):

        self.final_amount = self.total_bill - self.discount

    def generate_bill(self):

        self.calculate_bill()
        self.calculate_discount()
        self.calculate_final_amount()

        self.bill_status = "GENERATED"


class InsurancePatient(Patient):

    def __init__(self, patient_id, patient_name, patient_age,
                 days, medicine_charge):

        super().__init__(
            patient_id,
            patient_name,
            patient_age,
            days,
            medicine_charge
        )

        self.patient_type = "Insurance"
        self.insurance_amount = 0

    def calculate_bill(self):

        self.consultation_fee = 800
        self.room_charges = self.days * 1500

        self.total_bill = (
            self.consultation_fee +
            self.room_charges +
            self.medicine_charge
        )

    def calculate_discount(self):

        self.insurance_amount = self.total_bill * 0.70

    def calculate_final_amount(self):

        self.final_amount = self.total_bill - self.insurance_amount

    def generate_bill(self):

        self.calculate_bill()
        self.calculate_discount()
        self.calculate_final_amount()

        self.bill_status = "GENERATED"


class CorporatePatient(Patient):

    def __init__(self, patient_id, patient_name, patient_age,
                 days, medicine_charge):

        super().__init__(
            patient_id,
            patient_name,
            patient_age,
            days,
            medicine_charge
        )

        self.patient_type = "Corporate"
        self.discount_amount = 0

    def calculate_bill(self):

        self.consultation_fee = 700
        self.room_charges = self.days * 1200

        self.total_bill = (
            self.consultation_fee +
            self.room_charges +
            self.medicine_charge
        )

    def calculate_discount(self):

        self.discount_amount = self.total_bill * 0.20

    def calculate_final_amount(self):

        self.final_amount = self.total_bill - self.discount_amount

    def generate_bill(self):

        self.calculate_bill()
        self.calculate_discount()
        self.calculate_final_amount()

        self.bill_status = "GENERATED"