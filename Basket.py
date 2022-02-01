from Goods import Good


class Basket:
    def __init__(self):
        """
        Класс корзина, собирающий товары пользователя.
        """
        self.basket = []

    def adding_goods(self, name: str) -> list:
        self.basket.append(Good.return_good(name))
        return self.basket

    def removing_goods(self, name: str):
        self.basket.remove(Good.return_good(name))
        return self.basket

    def average_price(self):
        average_price = 0
        for _ in self.basket:
            average_price += Good.return_price()
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
    print(alpha)
    #alpha.removing_goods('Banana')
    print(alpha)
    alpha.adding_goods('Potato')
    print(alpha)
    #print(alpha.average_price())
