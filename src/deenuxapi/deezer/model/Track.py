from src.deenuxapi.deezer.Model import Model

from src.deenuxapi.deezer.model.Artist import Artist


class Track(Model):
    """
    Contains information about a track.
    """

    def __init__(self, id: int, title: str, artist: Artist, duration: int = -1):
        """
        Constructor of Track.
        :param id: track's ID
        :param title: track's full title
        :param artist: track's artist
        :param duration: track's duration in seconds (default is -1)
        """
        super().__init__(id)
        self.__title = title
        self.__artist = artist
        self.__duration = duration

    @staticmethod
    def map(obj):
        return Track(
            id=obj['id'],
            title=obj['title'],
            artist=Artist(
                id=obj['artist']['id'],
                name=obj['artist']['name']
            )
        )

    def __str__(self):
        return '{} - {}'.format(self.__artist.name, self.__title)

    """
    Getters and setters.
    """

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def artist(self):
        return self.__artist

    @artist.setter
    def artist(self, artist: Artist):
        self.__artist = artist

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

