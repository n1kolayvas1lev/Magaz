from typing import Optional

from Basket import Basket


class User:

    def __init__(self, login: str, password: str, basket: Optional['Basket'] = None):
        self._login = login
        self._password = password

        self._basket = basket
        self.__users = {}

    def add_user(self):
        self.__users[self._login] = self._password

    def save_user(self):
        UDB = "users.txt"
        with open(UDB, 'a') as udb:
            udb.write(str(self.__users))

    def read_user(self):
        UDB = "users.txt"
        with open(UDB) as udb:
            udb.read()



if __name__ == '__main__':
    eric = User('Eric', '123')
    eric.add_user()
    eric.save_user()

