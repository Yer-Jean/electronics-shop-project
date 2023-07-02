import csv

# Константа, содержащая путь до csv-файла с данными
from settings import DATA_PATH


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate: float = 1.0
    all: list = []

    def __init__(self, name: str, price: int, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name: str = name
        self.price: int = price
        self.quantity: int = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        # Проверяем название товара на длину в 10 букв
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            print('\nДлина наименования товара превышает 10 символов.\n')
            self.__name = new_name[:10]  # Обрезаем название до 10 символов

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод инициализирует экземпляры класса `Item`
        данными из файла _src/items.csv
        """
        Item.all = []   # Очищаем список экземпляров класса
        # Считываем данные из csv-файла
        with open(DATA_PATH, encoding='windows-1251') as data_file:
            file_reader = csv.DictReader(data_file, delimiter=",")
            # Инициализируем экземпляры класса данными построчно из файла
            for row in file_reader:
                Item(name=row['name'],
                     price=cls.string_to_number(row['price']),
                     quantity=cls.string_to_number(row['quantity']))

    @staticmethod
    def string_to_number(string_with_digits: str) -> int:
        """
        Преобразует и возвращает целочисленное число из строки
        """
        return int(float(string_with_digits))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate
