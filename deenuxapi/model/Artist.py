from Model import Model


class Artist(Model):

    def __init__(self, id: str, name: str):
        super().__init__(id)
        self.name = name