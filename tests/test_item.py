"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def data_for_tests():
    return [
        {'name': 'Кабель', 'price': 10, 'quantity': 5},
        {'name': 'Мышка', 'price': 50, 'quantity': 5},
        {'name': 'Клавиатура', 'price': 75, 'quantity': 5}
    ]


def test_correct_data(data_for_tests):
    [Item(**item) for item in data_for_tests]
    assert isinstance(data_for_tests, list)
    assert isinstance(data_for_tests[0], dict)
    assert len(data_for_tests) == 3
    assert isinstance(Item.all, list)
    assert isinstance(Item.all[0], Item)
    assert len(Item.all) == 3
    assert Item.all[0].name == 'Кабель'
    assert Item.all[1].price == 50
    assert Item.all[2].quantity == 5


def test_calculate_total_price(data_for_tests):
    [Item(**item) for item in data_for_tests]
    item1 = Item('Монитор', 100, 5)
    assert Item.all[1].calculate_total_price() == 250
    assert item1.calculate_total_price() == 500


def test_apply_discount(data_for_tests):
    [Item(**item) for item in data_for_tests]
    item1 = Item('Флэшка', 6, 20)
    Item.pay_rate = 0.5
    Item.all[0].apply_discount()
    item1.apply_discount()
    assert item1.price == 3
    assert Item.all[0].price == 5
