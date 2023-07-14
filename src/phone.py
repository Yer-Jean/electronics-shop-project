from src.item import Item


class Phone(Item):  # Описываем подкласс от класса Item
    def __init__(self, name: str, price: int, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)  # используем инициализатор родительского класса
        self.__number_of_sim = None              # и добавляем свой новый атрибут,
        self.number_of_sim = number_of_sim       # поверяя его корректность через сеттер

    # Переопределяем метод __repr__ из родительского класса
    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, num_of_sim: int):
        # Проверяем на количество SIM-карт в телефоне(должно быть больше 0)
        if num_of_sim > 0:
            self.__number_of_sim = num_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
