from Goods import Good


class Basket:
    def __init__(self):
        """
        Класс корзина, собирающий товары пользователя.
        """
        self.basket = []

    def adding_goods(self, name: str) -> list:
        """
        Добавляет продукты в корзину по имени.
        :param name: str
        :return: list
        """
        self.basket.append(Good.return_good(name))
        return self.basket

    def removing_goods(self, name: str) -> list:
        """
        Должно удалять продукты из корзины, хз почему не работает.
        :param name: str
        :return: list
        """
        self.basket.remove(Good.return_good(name))
        return self.basket

    def average_price(self) -> float:
        """
        Считает общий ценник содержимого корзины.
        :return: float
        """
        average_price = 0
        for item in self.basket:
            average_price += Good.return_price(item)
        return average_price

    def __repr__(self) -> str:
        return f"{__class__.__name__}, {self.basket}"

    def __str__(self) -> str:
        return f"{[print(good) for good in self.basket]}"


if __name__ == '__main__':
    alpha = Basket()
    alpha.adding_goods('Apple')
    print(alpha)
    alpha.adding_goods('Banana')
    print(type(alpha))
    #alpha.removing_goods('Banana')
    # print(alpha)
    # alpha.adding_goods('Potato')
    # print(alpha)
    # print(alpha.average_price())
