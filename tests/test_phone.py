import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def data_for_tests():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("NOKIA 3110", 20_000, 10, 1)
    return phone1, phone2


def test_str_repr_methods(data_for_tests):
    assert str(data_for_tests[0]) == 'iPhone 14'
    assert repr(data_for_tests[1]) == "Phone('NOKIA 3110', 20000, 10, 1)"


def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0


def test_sum_classes(data_for_tests):
    item = Item('Флэшка', 6, 20)
    assert data_for_tests[0] + data_for_tests[1] == 15
    assert item + data_for_tests[0] == 25
