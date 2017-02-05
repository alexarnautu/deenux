import abc
from src.deenuxapi.Utils import Utils
from src.deenuxapi.deezer.ResourceManager import ResourceManager


class Model:
    """
    Generic class for the entities of the model. All model entities are derived
    from this class. All model entities have the ID as property.
    """

    basic_cache = {}

    @staticmethod
    @abc.abstractmethod
    def map(obj):
        """
        Mapping function is required if you want to extend this class
        :param obj: A dictionary with raw data received from the http api
        :return: A model object with mapped data
        """

    def __init__(self, id: int):
        """
        Constructor of Model.
        :param id: entity's ID
        """
        self.__id = id

    @classmethod
    def get(cls, id, params: dict = None):
        """
        Gets instance of a record, by calling the Api using the static endpoint
        :param id: Id of the instance
        :param params: Additional params
        :return: The model entity
        """
        endpoint = cls.__name__.lower()
        if endpoint not in Model.basic_cache:
            Model.basic_cache[endpoint] = {}
        if id in Model.basic_cache[endpoint]:
            return Model.basic_cache[endpoint][id]

        model = cls.map(
            Utils.request(
                'GET',
                ResourceManager.get_endpoint(endpoint, id, params)
            )
        )
        Model.basic_cache[endpoint][id] = model
        return model

    """
    Getters and setters.
    """

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

