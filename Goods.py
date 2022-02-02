import json

from typing import Optional


class Good:
    def __init__(self, name: Optional['str'] = None, price: Optional['float'] = None,
                 rating: Optional['int'] = None):
        """
        Класс описывающий товар в магазине. Товар имеет 3 параметра:
        Имя
        Стоимость
        Рейтинг
        :param name: str
        :param price: float
        :param rating: int
        """
        self.name = name
        self.price = price
        self.rating = rating

    # @staticmethod
    # def deserialize():
    #     print('1 - фрукты, 2 - овощи')
    #     category = int(input('Введите категорию для добавления: '))
    #     if category == 1:
    #         file = 'fruits.json'
    #     if category == 2:
    #         file = 'vegetables.json'
    #     with open(file, 'r') as cat:
    #         goods = json.load(cat)
    #     return goods

    def add_goods(self) -> None:
        """
        Позволяет добавлять в файл соответствующей категории товары.
        :return: None
        """
        print('1 - фрукты, 2 - овощи')
        category = int(input('Введите категорию для добавления: '))
        if category == 1:
            file = 'fruits.json'
        if category == 2:
            file = 'vegetables.json'
        with open(file, 'r') as cat:
            goods = json.load(cat)
        # self.deserialize()
        self.name = str(input('Введите название: '))
        self.price = float(input('Введите цену: '))
        self.rating = int(input('Введите рейтинг: '))
        goods[self.name] = (self. price, self.rating)
        with open(file, 'w') as cat:
            json.dump(goods, cat)

    @staticmethod
    def return_good(name: str):
        """
        Считывает из файла товар по названию и выдаёт его в виде экземпляра класса Good.
        :param name: str
        :return: class Good
        """
        with open('fruits.json', 'r') as fruits:
            fruits = json.load(fruits)
        with open('vegetables.json', 'r') as vegetables:
            vegetables = json.load(vegetables)
        if name in fruits:
            # self.name = name
            # self.price = fruits.get(name)[0]
            # self.rating = fruits.get(name)[1]
            # print(f"{__class__.__name__}, {self.name}, {self.price}, {self.rating}")
            price = fruits.get(name)[0]
            rating = fruits.get(name)[1]
        if name in vegetables:
            # self.name = name
            # self.price = vegetables.get(name)[0]
            # self.rating = vegetables.get(name)[1]
            # print(f"{__class__.__name__}, {self.name}, {self.price}, {self.rating}")
            price = vegetables.get(name)[0]
            rating = vegetables.get(name)[1]
        return Good(name, price, rating)

    def return_price(self) -> float:
        """
        Возвращает ценник конкретного товара.
        :return: float
        """
        return self.price

    def __repr__(self) -> str:
        return f"{__class__.__name__}, {self.name}, {self.price}, {self.rating}"

    def __str__(self) -> str:
        return f"{self.name} Price {self.price}, Rating {self.rating}."


if __name__ == '__main__':

    a = Good()
    print(a.return_good("Apple"))
    print(type(a.return_good("Potato")))
    # banana = Good('banana', 10.1, 5)
    # print(banana.return_price())
    # apple = Good('apple', 5.5, 4)
    # peach = Good('peach', 8, 2)
    #
    # print(banana)
    # print(apple)
    # print(peach)
