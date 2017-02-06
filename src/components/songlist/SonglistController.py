

class SonglistController:

    def __init__(self, view, context):
        self._context = context
        self._view = view
    
    @property
    def view(self):
        return self._view

    @property
    def context(self):
        return self._context

    def on_line_double_click(self, index):
        self.context.deezer.jukebox.start(index.model().table_data[index.row()][0])