class View:

    def __init__(self, context=None, controller=None):
        self._controller = context
        self._context = controller

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
