from emergency.adult import Adult

def test_personal_data():
    patient = Adult("John", "Smith", 123456, 20, 36.6, None)
    assert patient.personal_data == {'first_name': 'John', 'last_name': 'Smith', 'presonal_id': 123456, 'age': 20}
