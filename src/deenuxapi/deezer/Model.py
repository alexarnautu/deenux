import abc

from src.deenuxapi.deezer.ResourceManager import ResourceManager
from src.deenuxapi.deezer.Request import Request
from collections import defaultdict

class Model:
    """
    Generic class for the entities of the model. All model entities are derived
    from this class. All model entities have the ID as property.
    """

    basic_cache = defaultdict(lambda: {})

    @staticmethod
    @abc.abstractmethod
    def map(obj):
        """
        Mapping function is required if you want to extend this class
        :param obj: A dictionary with raw data received from the http api
        :return: A model object with mapped data
        """

    def __eq__(self, cpt):
        return cpt.__id == self.__id

    def __init__(self, id: int):
        """
        Constructor of Model.
        :param id: entity's ID
        """
        self.__id = id

    @classmethod
    def get(cls, id, params: dict = {}):
        """
        Gets instance of a record, by calling the Api using the static endpoint
        :param id: Id of the instance
        :param params: Additional params
        :return: The model entity
        """
        endpoint = cls.__name__.lower()
        if id in Model.basic_cache[endpoint]:
            return Model.basic_cache[endpoint][id]

        model = cls.map(
            Request.get(
                ResourceManager.get_endpoint((endpoint, id)), params)
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
