from PyQt5.QtCore import QRegExp
from PyQt5.QtCore import Qt
from src.components.Controller import Controller
from src.utils.Sequence import Sequence


class SonglistController(Controller):

    def __init__(self, view, context):
        super(SonglistController, self).__init__(view, context)

    def on_line_double_click(self, index):
        self.context.mix = self.view.songlist_model.table_raw_data
        self.context.sequence = Sequence(
            len(self.context.mix),
            index.row(),
            self.context.shuffle,
            True # for now, TODO change
        )
        self.context.deezer.jukebox.start(index.model().table_data[index.row()][0])

    def on_line_selected(self, selected, deselected):
        item_selected = len(selected.indexes()) > 0
        self.context.player.track_controls.play_pause_button.setEnabled(item_selected or self.context.player.active)
        if item_selected:
            self.context.to_play = self.view.songlist_model.table_data[selected.indexes()[0].row()][0]
            self.context.current_mix = self.view.songlist_model
