from emergency.staff_member import StaffMember
from emergency.adult import Adult
from emergency.child import Child
from emergency.patient import Patient
import numpy as np
from datetime import datetime


class Doctor(StaffMember):
    def __init__(self,  first_name, last_name, presonal_id, age, licence_number):
        super(Doctor, self).__init__(first_name, last_name, presonal_id, age, licence_number)

    @staticmethod
    def generate_report(patients:list[Patient]):
        positive = list(filter(lambda x: x.diag == 'Positive', patients))
        recovered = list(filter(lambda x: x.diag == 'Recovered', patients))
        positive_children = list(filter(lambda x: x.diag == 'Positive' and x.age <= 16, patients))
        recovered_children = list(filter(lambda x: x.diag == 'Recovered' and x.age <= 16, patients))
        positive_senior = list(filter(lambda x: x.diag == 'Positive' and x.age > 65, patients))
        recovered_senior = list(filter(lambda x: x.diag == 'Recovered' and x.age > 65, patients))
        report = {
                "Total ratio of recovered COVID patients": len(recovered)/(len(positive)+len(recovered)),
                "Ratio of COVID recovered children": len(recovered_children)/(len(positive_children)+len(recovered_children)),
                "Ratio of COVID recovered senior citizens (above 65)": len(recovered_senior)/(len(positive_senior)+len(recovered_senior))
                  }
        return report

    @staticmethod
    def generate_final_report(patients:list[Patient]):
        report = {}
        for p in patients:
            report[datetime.now()] = p.personal_data
        return report

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
                patient.diag = 'Recovered'
