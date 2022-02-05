import json

from typing import Optional

from Basket import Basket


class InvalidPassword(Exception):
    pass


class User:
    """
    Класс пользователя.
    add_user: Добавить П.
    read_user: Авторизовать П.
    """

    def __init__(self, login: Optional['str'] = None, password: Optional['str'] = None):
        self._login = login
        self._password = password

        self._basket = Basket()
        self.__users = {}

    def add_user(self) -> None:
        """
        Функция добавления пользователя в users.json.
        :return: None
        """
        with open('users.json', 'r') as udb:
            self.__users = json.load(udb)
        self._login = str(input('Enter login: '))
        self._password = str(input('Enter password: '))
        self.__users[self._login] = self._password
        with open('users.json', 'w') as udb:
            json.dump(self.__users, udb)

    def add_to_basket(self, name: str) -> Basket:
        """
        Добавление товара в корзину по наименованию.
        :param name: str
        :return: Basket
        """
        self._basket.adding_goods(name)
        return self._basket

    def remove_from_basket(self, name: str) -> Basket:
        """
        Удаление товара из корзины по наименованию.
        :param name: str
        :return: Basket
        """
        self._basket.removing_goods(name)
        return self._basket

    @property
    def get_basket(self) -> Basket:
        """
        Получение содержимого корзины на вывод.
        :return: Basket
        """
        return self._basket

    def read_user(self) -> bool:
        """
        Функция чтения пары логин/пароль из users.json и
        проверки корректности введённой пары.
        :return: bool
        """
        self._login = str(input("Login: "))
        self._password = str(input("Password: "))
        with open('users.json', 'r') as udb:
            users = json.load(udb)
        if users.get(self._login) == self._password:
            print('Correct.')
            return True
        raise InvalidPassword("Incorrect password.")


if __name__ == '__main__':
    peter = User()
    # eric = User()
    # peter = User('Peter', '123')
    # peter.add_user()
    # eric.add_user()
    # peter.save_user()

    peter.read_user()
    # eric.read_user()
    peter.add_to_basket('Banana')
    print(peter.get_basket)
