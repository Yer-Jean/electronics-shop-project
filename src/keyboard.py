from src.item import Item


class SwitchKbdMixin:

    def __init__(self):
        self.__language = 'EN'

    def change_lang(self):
        self.__language = {self.__language == 'EN': 'RU',
                           self.__language == 'RU': 'EN'}[True]
        return self

    @property
    def language(self):
        return self.__language


class Keyboard(Item, SwitchKbdMixin):  # Описываем подкласс от класса Item и добавляем миксин SwitchKbdMixin

    def __init__(self, name: str, price: int, quantity: int):
        super().__init__(name, price, quantity)  # используем инициализатор родительского класса
        SwitchKbdMixin.__init__(self)            # и инициализатор миксина
