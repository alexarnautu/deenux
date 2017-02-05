from src.deenuxapi.Model import Model
from src.deenuxapi.deezer.ResourceManager import ResourceManager
from src.deenuxapi.model.Track import Track
from src.deenuxapi.model.Artist import Artist
from src.deenuxapi.Utils import Utils

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

    @staticmethod
    def map(obj):
        return User(
            id=obj['id'],
            username=obj['name'],
            firstname=obj['firstname'],
            lastname=obj['lastname'],
            email=obj['email']
        )

    def get_favourite_tracks(self, skip: int = 0, take: int = 25) -> list:
        """
        Gets a list of user's favourite tracks
        Supports pagination parameters
        :param skip: Pagination param (.NET's LINQ-like, also self-explainatory)
        :param take: Like above
        :return: List of trakcs
        """
        data = Utils.request('GET', ResourceManager.get_endpoint('user_favs', self.id, {
            'index': skip,
            'limit': take
        })) # TODO 2

        return list(map(Track.map, data['data']))

    @staticmethod
    def get_from_token(token: str):
        """
        Gets the User of the authentication token
        :param token: The access token
        :return: A User record
        """
        data = Utils.request('GET', ResourceManager.get_endpoint('user', 'me', {
            'access_token': token
        })) # TODO 2

        return User.map(data)

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
