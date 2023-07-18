"""Здесь надо написать тесты с использованием pytest для модуля item."""
from pathlib import Path

import pytest

import settings
import src.item
from src.exceptions import InstantiateCSVError, CSVFileNotFound
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


def test_sum_classes():
    item1 = Item('Кабель', 10, 5)
    item2 = Item('Мышка', 20, 10)
    assert item1 + item2 == 15
    with pytest.raises(Exception):
        _ = item1 + 25


def test_exceptions():
    TEST_PATH = Path.joinpath(settings.ROOT, 'tests')

    # Test - FileNotFoundException - открываем несуществующий файл
    src.item.DATA_FILE = 'wrong_file.csv'
    src.item.DATA_PATH = Path.joinpath(settings.SRC_PATH, src.item.DATA_FILE)
    with pytest.raises(CSVFileNotFound):
        Item.instantiate_from_csv()

    # Test - KeyError - отсутствует один из заголовков колонок
    src.item.DATA_FILE = 'bad_data_title.csv'
    src.item.DATA_PATH = Path.joinpath(TEST_PATH, src.item.DATA_FILE)
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()

    # Test - TypeError - отсутствует одно из значений в строке
    src.item.DATA_FILE = 'bad_data_column.csv'
    src.item.DATA_PATH = Path.joinpath(TEST_PATH, src.item.DATA_FILE)
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()
