from Goods import Good


class Basket:
    def __init__(self):
        """
        Класс корзина, собирающий товары пользователя.
        """
        self.basket = []

    def adding_goods(self, good: Good) -> list:
        """
        Функция добавления товаров в корзину.
        :param good: Good
        :return: list
        """
        self.basket.append(good)
        return self.basket

    def removing_goods(self, good: Good):
        self.basket.remove(good)
        return self.basket

    def __repr__(self) -> str:
        return f"{__class__.__name__}, {self.basket}"

    def __str__(self) -> str:
        return f"{[good for good in self.basket]}"


if __name__ == '__main__':
    ...
