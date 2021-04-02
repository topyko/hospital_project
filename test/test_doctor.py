from emergency.doctor import Doctor


def test_personal_data():
    d = Doctor("Bob", "Barley", 123456, 25, "D22222")
    print(d.personal_data)
    assert d.personal_data == {'first_name': 'Bob', 'last_name': 'Barley', 'presonal_id': 123456, 'age': 25, 'licence_number': 'D22222'}
    assert 'licence_number' in list(d.personal_data.keys())

