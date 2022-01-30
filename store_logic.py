from User import User

from Category import Category

from Basket import Basket

from Goods import Good


class Store:
    def __init__(self):
        ...

    @staticmethod
    def authentication() -> bool:
        """
        Функция аутентификации пользователя.
        :return: bool
        """
        if User.read_user():
            print('Authentication passed.')
            return True
        return False

    @staticmethod
    def show_catalogue() -> dict:
        """
        Функция показа каталога категорий товара.
        :return: dict
        """
        print(Category.show_categories())

    @staticmethod
    def show_goods():
        ...

    @staticmethod
    def add_to_basket(good: Good):
        Basket.adding_goods(good)

    @staticmethod
    def remove_from_basket(good: Good):
        Basket.removing_goods(good)

    def buy(self):
        ...

    def show_options(self):
        print()


if __name__ == '__main__':
    alpha = Store()
    alpha.show_catalogue()
