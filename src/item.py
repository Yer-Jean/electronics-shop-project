import csv

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
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        Item.all = []
        with open(DATA_PATH, encoding='windows-1251') as data_file:
            file_reader = csv.DictReader(data_file, delimiter=",")
            for row in file_reader:
                Item(name=row['name'],
                     price=cls.string_to_number(row['price']),
                     quantity=cls.string_to_number(row['quantity']))

    @staticmethod
    def string_to_number(string_with_digits: str) -> int:
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
