

class SonglistController:

    @property
    def context(self):
        return self._context

    def __init__(self, context):
        self._context = context

    def on_line_double_click(self, index):
        self.context.deezer_service.jukebox.start(index.model().table_data[index.row()][0])