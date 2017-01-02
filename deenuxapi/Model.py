

class Model:

    def __init__(self, id: str):
        self.__id = id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id