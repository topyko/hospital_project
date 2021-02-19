from emergency.doctor import Doctor
from emergency.nurse import Nurse
from emergency.child import Child
from emergency.adult import Adult

class HospitalUtils():

    @staticmethod
    def readFile(filepath):
        try:
            with open(filepath, 'rb') as fp:
                return fp.readlines()
        except Exception as exp:
            print("Caught an exception:", exp)
            return None


    @staticmethod
    def populate(lines):
        result = {"patients":{
            "adults": [],
            "children": []
        },
            "stuff": {
                "doctor": None,
                "nurse": None
            }
        }
        for i, line in enumerate(lines):
            values = line.split("|")
            first_name = values[1]
            last_name = values[2]
            age = int(values[3])
            personal_id = values[4]
            l_number = values[5]
            body_t = values[6]
            symptoms = values[7]
            if len(l_number) > 0:
                if l_number.startswith("D"):
                    doctor = Doctor(first_name, last_name, personal_id, age, l_number)
                    result['stuff']['doctor'] = doctor
                elif l_number.startswith("N"):
                    nurse = Nurse(first_name, last_name, personal_id, age, l_number)
                    result['stuff']['nurse'] = nurse
                else:
                    raise Exception("not suported")
            else:
                if age > 16:
                    adult = Adult(first_name, last_name, personal_id, age, body_t, symptoms)
                    result['patients']['adults'].append(adult)
                    # print(adult.personal_data)
                else:
                    child = Child(first_name, last_name, personal_id, age, body_t, symptoms)
                    result['patients']['children'].append(adult)

        return result

if __name__ == '__main__':
    lines = HospitalUtils.readFile("C:\\Users\\chigr\\Downloads\\hospital_data.csv")
    data = HospitalUtils.populate(lines)
