class Model:
    """
    Generic class for the entities of the model. All model entities are derived
    from this class. All model entities have the ID as property.
    """

    def __init__(self, id: int):
        """
        Constructor of Model.
        :param id: entity's ID
        """
        self.__id = id

    """
    Getters and setters.
    """

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id
