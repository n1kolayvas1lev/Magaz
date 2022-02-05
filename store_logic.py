import json

from User import User

from Category import Category


class Store:
    def __init__(self):
        self.user = User()

    def authentication(self) -> bool:
        """
        Функция аутентификации пользователя.
        :return: bool
        """
        if self.user.read_user():
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

    def add_to_basket(self, item: str) -> None:
        """
        Должно добавлять в корзину товары по названию.
        :param item: str
        :return: None
        """
        self.user.get_basket.adding_goods(item)

    def remove_from_basket(self, item: str) -> None:
        """
        Должно удалять товары из корзины по названию.
        :param item: str
        :return: None
        """
        self.user.get_basket.removing_goods(item)

    def buy(self) -> None:
        """
        Должно получать общий ценник корзины и требовать оплаты до победного.
        :return: None
        """
        price = self.user.get_basket.average_price()
        print(price)
        income = float(input('Введите деньги.'))
        while price != income:
            print('Введите правильную сумму.')
            income = float(input('Введите деньги.'))
        print('Оплачено.')

    def show_basket(self) -> None:
        """
        Функция показа содержимого корзины.
        :return:
        """
        print(self.user.get_basket)
        print(self.user.get_basket.average_price())

    @staticmethod
    def show_options() -> None:
        """
        Вывод на печать списка действий.
        :return: None
        """
        print('Аутентификация,'
              'Просмотр каталогов,'
              'Просмотр каталога,'
              'Добавить в корзину,'
              'Удалить из корзины,'
              'Посчитать сумму,'
              'Купить')


if __name__ == '__main__':
    alpha = Store()
    alpha.show_options()  # 6. Перечисление содержащее значения для перечисленных операций.
    alpha.authentication()  # 1. Аутентификация пользователя.
    alpha.show_catalogue()  # 2. Просмотр списка каталогов товаров.
    alpha.show_goods()  # 3. Просмотр списка товаров определенного каталога.
    alpha.add_to_basket('Banana')  # 4. Выбор товара в корзину.
    alpha.show_basket()
    alpha.buy()  # 5. Покупка товаров, находящихся в корзине.
