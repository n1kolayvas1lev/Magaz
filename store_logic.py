import json

from User import User

from Category import Category

from Basket import Basket

#from Goods import Good


class Store:
    def __init__(self):
        ...

    @staticmethod
    def authentication() -> bool:
        """
        Функция аутентификации пользователя.
        :return: bool
        """
        if User.read_user:
            print('Authentication passed.')
            return True
        return False

    @staticmethod
    def show_catalogue() -> None:
        """
        Функция показа каталога категорий товара.
        :return: dict
        """
        print(Category.show_categories())

    @staticmethod
    def show_goods() -> None:
        """
        Показать содержимое каталогов.
        :return: None
        """
        print('1 - фрукты, 2 - овощи')
        category = int(input('Введите категорию: '))
        if category == 1:
            file = 'fruits.json'
        if category == 2:
            file = 'vegetables.json'
        with open(file, 'r') as cat:
            goods = json.load(cat)
        print(goods)

    @staticmethod
    def add_to_basket(item: str):
        Basket.adding_goods(item) #Почему не заполнен?

    @staticmethod
    def remove_from_basket(item: str):
        Basket.removing_goods(item) #Почему не заполнен?

    @staticmethod
    def buy():
        price = Basket.average_price() #Почему не заполнен?
        print(price)
        income = int(input('Введите деньги.'))
        while price != income:
            print('Введите правильную сумму.')
            income = int(input('Введите деньги.'))

    @staticmethod
    def show_basket():
        print(Basket)

    def show_options(self):
        print(self.__dict__)


if __name__ == '__main__':
    alpha = Store()
    #alpha.authentication()
    #alpha.show_catalogue()
    #alpha.show_goods()
    alpha.add_to_basket('Banana')
    #alpha.show_basket()
