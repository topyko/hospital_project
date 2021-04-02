from emergency.person import Person

class Patient(Person):
    def __init__(self, first_name, last_name, presonal_id, age, body_temperature, symptoms):
        # super(Patient, self).__init__(first_name, last_name, presonal_id, age)
        self.body_temperature, self.symptoms = body_temperature, symptoms
        self.diag = None
        self.requires_isolation = False

    # # @personal_data.setter
    # def personal_data(self, val):
    #     pass