class Mail:
    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password
