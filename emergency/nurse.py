import numpy as np
from emergency.staff_member import StaffMember
from emergency.adult import Adult
from emergency.child import Child
from emergency.patient import Patient

class Nurse(StaffMember):
    def __init__(self,  first_name, last_name, presonal_id, age, licence_number):
        super(Nurse, self).__init__(first_name, last_name, presonal_id, age, licence_number)


    # @staticmethod
    # def generate_report(patients:list):
    #     children = filter(lambda x: x.personal_data["age"] <=16, patients)
    #     sick_children = filter(lambda x: x.personal_data["age"] <=16, positive)
    #     sick_senior = filter(lambda x: x.personal_data["age"] > 65, positive)
    #
    #     report = {"Ratio of COVID patients from total patients": len(positive) / len(patients),
    #               "Ratio of COVID patients from patients with symptoms": len(positive) / len(isolated),
    #               "Ratio of COVID children from total children patients": len(sick_children) / len(children),
    #               "Ratio of COVID senior citizens (above 65) from total patients": len(sick_senior) / len(patients)}
    #
    #     return report

    @staticmethod
    def test_covid(isolated_patients):
        np.random.seed(seed=42)
        for patient in isolated_patients:
            if isinstance(patient, Child):
                diag = np.random.choice(["Positive", "Negative"], p=(0.2, 0.8))
            else:
                positive_outcome_prob = min(0.8, max(0.25, patient.personal_data['age']/100))
                diag = np.random.choice(["Positive", "Negative"], p=(positive_outcome_prob, 1 - positive_outcome_prob))
            patient.diag = diag

    # @staticmethod
    # def isolate(patients: list[Patient]):
    #     [setattr(p, 'requires_isolation', True) for p in patients if (p.body_temperature > 38.5 or p.symptoms == "cough")]
    #     # return list(filter(lambda x: x.body_temperature > 38.5 or x.symptoms == "cough", patients))
