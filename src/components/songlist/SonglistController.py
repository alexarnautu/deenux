from PyQt5.QtCore import QRegExp
from PyQt5.QtCore import Qt
from src.components.Controller import Controller
from src.utils.Sequence import Sequence
from src.utils.Constants import Constants

class SonglistController(Controller):

    def __init__(self, view, context):
        super(SonglistController, self).__init__(view, context)

    def on_line_double_click(self, proxy_index):
        model = proxy_index.model()
        self.context.mix = list(map(
            lambda i : model.data(proxy_index.sibling(i, 0), Constants.FULL_DATA_ROLE),
            range(model.rowCount())
        ))
        self.context.sequence = Sequence(
            len(self.context.mix),
            proxy_index.row(),
            self.context.shuffle,
            True # for now, TODO change
        )
        self.context.deezer.jukebox.start(model.data(proxy_index, Constants.FULL_DATA_ROLE))

    def on_line_selected(self, selected, deselected):
        item_selected = len(selected.indexes()) > 0
        self.context.player.track_controls.play_pause_button.setEnabled(item_selected or self.context.player.active)
        if item_selected:
            self.context.to_play = self.view.songlist_model.table_data[selected.indexes()[0].row()][0]
            self.context.current_mix = self.view.songlist_model

    @Controller.async
    def on_searchbar_text_changed(self, *args):
        """
        Filters the proxy model. If the string in the search bar is a substring in any field of the entry, the entry is
        retained in the filtering.
        """
        current_search_within_tracks_query = self.view.search_bar.displayText()
        self._mx.lock()
        self.view.songlist_proxy_model.setFilterRegExp(
            QRegExp(current_search_within_tracks_query, Qt.CaseInsensitive, QRegExp.FixedString)
        )
        self.view.songlist_proxy_model.setFilterKeyColumn(-1)
        self._mx.unlock()