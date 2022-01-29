from User import User

from Category import Category

from Basket import Basket

from Goods import Good


class Store:
    def __init__(self):
        ...

    def authentication(self) -> bool:
        ...

    def show_catalogue(self):
        ...

    def show_goods(self):
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
    ...
