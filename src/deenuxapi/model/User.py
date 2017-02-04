from src.deenuxapi.Model import Model

class User(Model):
    """
    Contains information about an user.
    """

    def __init__(self, id: int, username: str, firstname: str, lastname: str,
            email: str):
        """
        Constructor of User.
        :param id: user's ID
        :param username: user's nickname
        :param firstname: user's first name
        :param lastname: user's last name
        :param email: user's email
        """
        super().__init__(id)
        self.__username = username
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email

    """
    Getters and setters.
    """

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email
