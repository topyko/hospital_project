from emergency.staff_member import StaffMember
from emergency.adult import Adult
from emergency.child import Child
import numpy as np


class Doctor(StaffMember):
    def __init__(self,  first_name, last_name, presonal_id, age, licence_number):
        super(Doctor, self).__init__(first_name, last_name, presonal_id, age, licence_number)

    @staticmethod
    def generate_report():
        report = {
                "Total ratio of recovered COVID patients": None,
                "Ratio of COVID recovered children": None,
                "Ratio of COVID recovered senior citizens (above 65)": None
                  }
        return report

    @staticmethod
    def generate_final_report():
        return {}

    @staticmethod
    def give_treatment(patients):
        outcome = [0, 1]
        for patient in patients:
            if isinstance(patient, Adult):
                weights = [0.7, 0.3]
            elif isinstance(patient, Child):
                weights = [0.6, 0.4]
            success = np.choices(outcome, weights)
            if success == 1:
                patient.diag = None
