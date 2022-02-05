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
            user = User(None, None, basket=Basket)
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

    # @staticmethod
    # def add_to_basket(item: str) -> None:
    #     """
    #     Должно добавлять в корзину товары по названию.
    #     :param item: str
    #     :return: None
    #     """
    #     User._basket.adding_goods(item) #Почему не заполнен name?

    # @staticmethod
    # def remove_from_basket(item: str) -> None:
    #     """
    #     Должно удалять товары из корзины по названию.
    #     :param item: str
    #     :return: None
    #     """
    #     Basket.removing_goods(item) #Почему не заполнен name?

    @staticmethod
    def buy() -> None:
        """
        Должно получать общий ценник корзины и требовать оплаты до победного.
        :return: None
        """
        price = Basket.average_price()
        print(price)
        income = int(input('Введите деньги.'))
        while price != income:
            print('Введите правильную сумму.')
            income = int(input('Введите деньги.'))
        print('Оплачено.')

    # @staticmethod
    # def show_basket() -> None:
    #     """
    #     Функция показа содержимого корзины.
    #     :return:
    #     """
    #     print(Basket.average_price())
    #     print(Basket())

    @staticmethod
    def show_options():
        print('Аутентификация, Просмотр каталогов, Просмотр каталога, Добавить в корзину, Удалить из корзины, Посчитать сумму, Купить')


if __name__ == '__main__':
    alpha = Store()
    #alpha.authentication()
    #alpha.show_catalogue()
    #alpha.show_goods()
    # alpha.add_to_basket('Banana')
    alpha.show_basket()
    alpha.show_options()
    alpha.buy()
