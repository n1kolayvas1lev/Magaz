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

    def __init__(self, login: Optional['str'] = None, password: Optional['str'] = None,
                 basket: Optional['Basket'] = None):
        self._login = login
        self._password = password

        self._basket = basket
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
    eric = User()
    # peter = User('Peter', '123')
    # peter.add_user()
    # eric.add_user()
    # peter.save_user()

    peter.read_user()
    eric.read_user()

