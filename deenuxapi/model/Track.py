
from Model import Model
from model.Artist import Artist

class Track(Model):

    def __init__(self, id: int, title: str, artist: Artist):
        super().__init__(id)
        self.title = title
        self.artist = artist

