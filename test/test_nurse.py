from emergency.nurse import Nurse
from emergency.adult import Adult
from emergency.child import Child


def test_isolate():
    patient1 = Adult(first_name="Ahmad", last_name="mahmood", presonal_id=123, age=34, body_temperature=36,
                       symptoms="None")
    patient2 = Child(first_name="Shira", last_name="Alboher", presonal_id=124, age=13, body_temperature=40,
                       symptoms="cough")

    patients = [patient1, patient2]

    isolated_kids = Nurse.isolate(patients)

    assert len(isolated_kids) == 1
    assert isolated_kids[0].personal_data['first_name'] == 'Shira'

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
