

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

    def on_line_selected(self, selected, deselected):
        item_selected = len(selected.indexes()) > 0
        self.context.player.play_pause_button.setEnabled(item_selected or self.context.player.active)
        if item_selected:
            self.context.player.to_play = self.view.songlist_model.table_data[selected.indexes()[0].row()][0]
            self.context.player.current_mix = self.view.songlist_model
            