from emergency.child import Child

def test_personal_data():
    p = Child("Ann", "Frank", 123456, 10, 38.2, "cough")
    assert p.personal_data == {'first_name': 'Ann', 'last_name': 'Frank', 'age': 10}
    assert "personal_id" not in p.personal_data.keys()
    assert "first_name" in p.personal_data.keys()
