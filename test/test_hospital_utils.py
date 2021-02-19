import mock
from utils.hospital_utils import HospitalUtils
from emergency.doctor import Doctor
from emergency.nurse import Nurse
from emergency.adult import Adult
from emergency.child import Child

mock_lines = [
    "0|Carol|Allen|31|82-2000962|N30503082381762|36.6|",
    "1|Tim|Peterson|29|60-3674816|D566375589322|36.6|",
    "2|Valerie|Wojner|20|26-4993385||38.3|cough",
    "3|Benjamin|Pratt|10|13-1150795||40.0|nausea"
]

@mock.patch("utils.hospital_utils.HospitalUtils.readFile", return_value = mock_lines)
def test_populate(val):
    lines = HospitalUtils.readFile(None)
    data = HospitalUtils.populate(lines)
    assert isinstance(data['stuff']['doctor'], Doctor)
    doctor = data['stuff']['doctor']

    assert isinstance(data['stuff']['nurse'], Nurse)

