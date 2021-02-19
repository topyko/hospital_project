import numpy as np
from emergency.staff_member import StaffMember
from emergency.adult import Adult
from emergency.child import Child

class Nurse(StaffMember):
    def __init__(self,  first_name, last_name, presonal_id, age, licence_number):
        super(Nurse, self).__init__(first_name, last_name, presonal_id, age, licence_number)

    def generate_report(self):
        pass

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

    @staticmethod
    def isolate(patients):
        return list(filter(lambda x: x.body_temperature > 38.5 or x.symptoms == "cough", patients))
