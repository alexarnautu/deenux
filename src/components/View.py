class View:

    def __init__(self):
        self._controller = None
        self._context = None

    @property
    def controller(self):
        return self._controller

    @property
    def context(self):
        return self._context

    def setup_ui(self):
        pass

    def retranslate_ui(self):
        pass

    def create_connections(self):
        pass
