from emergency.patient import Patient
class Adult(Patient):
    def __init__(self,  first_name, last_name, presonal_id, age, body_temperature, symptoms):
        super(Adult, self).__init__(first_name, last_name, presonal_id, age, body_temperature, symptoms) #this line was also fixed
        # self.body_temperature, self.symptoms = body_temperature, symptoms #this line was also fixed
        self.personal_data = (first_name, last_name, presonal_id, age)

    @Patient.personal_data.setter
    def personal_data(self, val):
        first_name, last_name, presonal_id, age = val
        self._personal_data = {"first_name": first_name, "last_name": last_name,
                               "presonal_id": presonal_id, "age": age}
