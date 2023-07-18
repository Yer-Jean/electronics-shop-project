import csv

# Константа, содержащая путь до csv-файла с данными
from settings import DATA_PATH, DATA_FILE
from src.exceptions import InstantiateCSVError


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

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):  # метод складывания классов
        # Проверяем на принадлежность к подклассу, или к его родительскому классу
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        raise Exception(f'Ошибка: несовместимые объекты {self.__class__.__name__} и {other.__class__.__name__}')

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
        try:
            with open(DATA_PATH, encoding='windows-1251') as data_file:
                file_reader = csv.DictReader(data_file, delimiter=",")
                try:   # Инициализируем экземпляры класса данными построчно из файла
                    for row in file_reader:
                        Item(name=row['name'],
                             price=cls.string_to_number(row['price']),
                             quantity=cls.string_to_number(row['quantity']))
                except (TypeError, KeyError):
                    raise InstantiateCSVError(f'Файл {DATA_FILE} поврежден')
        except FileNotFoundError:
            print(f'Отсутствует файл {DATA_FILE}')

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
