from emergency.staff_member import  StaffMember


class Doctor(StaffMember):
    def __init__(self,  first_name, last_name, presonal_id, age, licence_number):
        super(Doctor, self).__init__(first_name, last_name, presonal_id, age, licence_number)

    def generate_report(self):
        pass

    def generate_final_report(self):
        pass

    def give_treatment(self):
        pass
