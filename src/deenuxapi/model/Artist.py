from src.deenuxapi.Model import Model


class Artist(Model):
    """
    Contains information about an artist.
    """

    def __init__(self, id: int, name: str):
        """
        Constructor of Artist.
        :param id: artist's ID
        :param name: artist's name 
        """
        super().__init__(id)
        self.__name = name

    """
    Getters and setters.
    """

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
