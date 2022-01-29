from Goods import Good


class Category:
    def __init__(self, name: str):
        """
        Класс категория товаров. Список товаров, которые относятся к какой-то категории
        по выбору пользователя.
        :param name: str
        """
        self.name = name
        self.goods = []

    def adding_goods(self, good: Good) -> list:
        """
        Функция добавления товаров в категорию.
        :param good: Good
        :return: list
        """
        self.goods.append(good)
        return self.goods

    def __repr__(self) -> str:
        return f"{__class__.__name__}, {self.goods}"

    def __str__(self) -> str:
        return f"{[good for good in self.goods]}"


if __name__ == '__main__':
    banana = Good('banana', 10.1, 5)
    apple = Good('apple', 5.5, 4)
    peach = Good('peach', 8, 2)

    fruits = Category('Fruits')
    fruits.adding_goods(banana)
    print(fruits)
    fruits.adding_goods(apple)
    print(fruits)
    fruits.adding_goods(peach)
    print(fruits)

