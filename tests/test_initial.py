from collections import namedtuple

Car = namedtuple("Car", ["name", "owner", "year", "price"])
Car.__new__.__defaults__ = (None, None, None, None)


def test_defaults():
    c1 = Car()
    c2 = Car(None, None, None, None)
    assert c1 == c2


def test_owner():
    c = Car(owner="Asadbek")
    assert "Asadbek" == c.owner


def test_project():
    assert 1 == 1
