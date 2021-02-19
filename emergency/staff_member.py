from emergency.person import Person
from abc import abstractmethod
class StaffMember(Person):
    def __init__(self,  first_name, last_name, presonal_id, age, licence_number):
        # super(StaffMember, self).__init__(first_name, last_name, presonal_id, age)
        # self.body_temperature, self.symptoms = body_temperature, symptoms
        self.personal_data = (first_name, last_name, presonal_id, age, licence_number)

    @Person.personal_data.setter
    def personal_data(self, val):
        first_name, last_name, presonal_id, age, licence_number = val
        self._personal_data = {"first_name": first_name, "last_name": last_name,
                               "presonal_id": presonal_id, "age": age, "licence_number": licence_number}
    @abstractmethod
    def generate_report(self):
        pass
