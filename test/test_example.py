import pytest


def test_equal_or_not_equal():
    assert 3 == 3
    assert 3 != 1


def  test_is_instance():
    assert isinstance('this is a string', str)
    assert not isinstance ('10', int)

def test_boolean():
    validate = True
    assert validate is True
    assert ('hello' == 'world') is False

def test_type():
    assert type('Hello' is str)
    assert type('World' is not int)

def test_greater_and_less_than():
    assert 7 > 3
    assert 4 < 10

def test_list():
    num_list = [1,2,3,4,5]
    any_list = [False, False]
    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list)
    assert not any(any_list)



# fixtures

class Student:
    def __init__(self, first_name: str, last_name: str, years: int):
        self.first_name = first_name
        self.last_name = last_name
        self.years = years

@pytest.fixture
def default_employe():
    return Student('Géza','Nagy', 30)

# def test_person_initialization():
#     p = Student('Géza','Nagy', 30)
#     assert p.first_name == 'Géza', 'First name should be Géza'
#     assert p.last_name == 'Nagy', 'Last name should be Nagy'
#     assert p.years == 30

def test_person_initialization(default_employe):
    assert default_employe.first_name == 'Géza', 'First name should be Géza'
    assert default_employe.last_name == 'Nagy', 'Last name should be Nagy'
    assert default_employe.years == 30