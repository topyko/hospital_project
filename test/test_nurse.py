from emergency.nurse import Nurse
from emergency.adult import Adult
from emergency.child import Child


def test_isolate():
    patient1 = Adult(first_name="Ahmad", last_name="mahmood", presonal_id=123, age=34, body_temperature=36,
                       symptoms="None")
    patient2 = Child(first_name="Shira", last_name="Alboher", presonal_id=124, age=13, body_temperature=40,
                       symptoms="cough")

    patients = [patient1, patient2]

    Nurse.isolate(patients)

    assert patient1.requires_isolation == False
    assert patient2.requires_isolation == True

def test_generate_report():
    patient1 = Adult(first_name="Ahmad", last_name="mahmood", presonal_id=111, age=34, body_temperature=36,
                       symptoms="None")
    patient2 = Child(first_name="Shira", last_name="Alboher", presonal_id=222, age=13, body_temperature=40,
                       symptoms="cough")
    patient2.diag = "Positive"
    patient3 = Child(first_name="Shira", last_name="Alboher", presonal_id=333, age=13, body_temperature=40,
                     symptoms="cough")
    patient4 = Child(first_name="Shira", last_name="Alboher", presonal_id=444, age=13, body_temperature=40,
                     symptoms="cough")
    patient5 = Adult(first_name="Shira", last_name="Alboher", presonal_id=555, age=30, body_temperature=40,
                     symptoms="cough")
    patient6 = Adult(first_name="Shira", last_name="Alboher", presonal_id=666, age=68, body_temperature=40,
                     symptoms="cough")
    patient7 = Adult(first_name="Shira", last_name="Alboher", presonal_id=777, age=70, body_temperature=40,
                     symptoms="cough")
    patient8 = Adult(first_name="Shira", last_name="Alboher", presonal_id=888, age=80, body_temperature=40,
                     symptoms="cough")
    patients = [patient1, patient2,patient3, patient4,patient5, patient6,patient7, patient8]
    Nurse.isolate(patients)
    report=Nurse.generate_report(patients)
    assert report["Ratio of COVID children from total children patients"] == 1/3
    assert report['Ratio of COVID patients from total patients'] == 1/8


def test_test_covid():
    isolated_patients = [
        Adult(first_name="Ahmad", last_name="mahmood", presonal_id=123, age=100, body_temperature=40,
                       symptoms=None),
        Adult(first_name="Blabla", last_name="Blablabla", presonal_id=456, age=100, body_temperature=36.6,
              symptoms="cough"),
        Child(first_name="Tim", last_name="Tararam", presonal_id=789, age=10, body_temperature=36.6,
              symptoms="cough")
    ]
    Nurse.test_covid(isolated_patients)
    for i, p in enumerate(isolated_patients):
        if i == 0:
            assert p.diag == "Positive"
        else:
            p.diag == "Negative"


def test_personal_data():
    n = Nurse("Joanne", "Dark", 123456, 25, "N22222")
    print(n.personal_data)
    assert n.personal_data == {'first_name': 'Joanne', 'last_name': 'Dark', 'presonal_id': 123456, 'age': 25, 'licence_number': 'N22222'}
    assert 'licence_number' in list(n.personal_data.keys())
