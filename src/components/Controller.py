class Controller:

    def __init__(self, view=None, context=None):
        self._view = view
        self._context = context

    @property
    def context(self):
        return self._context

    @property
    def view(self):
        return self._view
