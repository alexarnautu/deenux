

class ToolbarController:

    @property
    def context(self):
        return self._context

    @property
    def view(self):
        return self._view

    def __init__(self, view, context):
        self._context = context
        self._view = view