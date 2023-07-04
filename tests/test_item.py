"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def data_for_tests():
    Item.all = []
    data = [
        {'name': 'Кабель', 'price': 10, 'quantity': 5},
        {'name': 'Мышка', 'price': 50, 'quantity': 5},
        {'name': 'Клавиатура', 'price': 75, 'quantity': 5}
    ]
    for row in data:
        Item(name=row['name'],
             price=Item.string_to_number(row['price']),
             quantity=Item.string_to_number(row['quantity']))


def test_correct_data(data_for_tests):
    assert isinstance(Item.all, list)
    assert isinstance(Item.all[0], Item)
    assert len(Item.all) == 3
    assert Item.all[0].name == 'Кабель'
    Item.all[0].name = 'Монитор'
    assert Item.all[0].name == 'Монитор'
    assert Item.all[1].price == 50
    assert Item.all[2].quantity == 5


def test_calculate_total_price(data_for_tests):
    item1 = Item('Монитор', 100, 5)
    assert Item.all[1].calculate_total_price() == 250
    assert item1.calculate_total_price() == 500


def test_apply_discount(data_for_tests):
    item1 = Item('Флэшка', 6, 20)
    Item.pay_rate = 0.5
    Item.all[0].apply_discount()
    item1.apply_discount()
    assert item1.price == 3
    assert Item.all[0].price == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_name_setter():
    item = Item('Телефон', 10000, 5)
    assert item.name == 'Телефон'
    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмарт'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[1].price == 1000
    assert Item.all[2].quantity == 5


def test_str_repr_methods(data_for_tests):
    assert repr(Item.all[0]) == "Item('Кабель', 10, 5)"
    assert str(Item.all[2]) == 'Клавиатура'
