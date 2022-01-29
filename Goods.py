class Good:
    def __init__(self, name: str, price: float, rating: int):
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

    def __repr__(self) -> str:
        return f"{__class__.__name__}, {self.name}, {self.price}, {self.rating}"

    def __str__(self) -> str:
        return f"{self.name} Price {self.price}, Rating {self.rating}."


if __name__ == '__main__':
    banana = Good('banana', 10.1, 5)
    apple = Good('apple', 5.5, 4)
    peach = Good('peach', 8, 2)

    print(banana)
    print(apple)
    print(peach)
