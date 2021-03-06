

class AppContext:
    """
    Provides context to the application, such as Services
    """

    def __init__(self, **kwargs):
        self.hook(**kwargs)

    def hook(self, **kwargs):
        for k in kwargs:
            setattr(self, k, kwargs[k])
