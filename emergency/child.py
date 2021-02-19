from emergency.patient import Patient
class Child(Patient):
    def __init__(self,  first_name, last_name, presonal_id, age, body_temperature, symptoms):
        super(Child, self).__init__(first_name, last_name, presonal_id, age, body_temperature, symptoms)
        # self.body_temperature, self.symptoms = body_temperature, symptoms
        self.personal_data = (first_name, last_name, presonal_id, age)

    @Patient.personal_data.setter
    def personal_data(self, val):
        first_name, last_name, presonal_id, age = val
        self._personal_data = {"first_name": first_name, "last_name": last_name,
                                "age": age}
