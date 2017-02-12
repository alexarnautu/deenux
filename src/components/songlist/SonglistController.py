from PyQt5.QtCore import QRegExp
from PyQt5.QtCore import Qt
from src.components.Controller import Controller


class SonglistController(Controller):

    def __init__(self, view, context):
        super(SonglistController, self).__init__(view, context)

    def on_line_double_click(self, index):
        self.context.deezer.jukebox.start(index.model().track(index))

    def on_line_selected(self, selected, deselected):
        item_selected = len(selected.indexes()) > 0
        self.context.player.track_controls.play_pause_button.setEnabled(item_selected or self.context.player.active)
        if item_selected:
            self.context.to_play = self.view.songlist_model.table_data[selected.indexes()[0].row()][0]
            self.context.current_mix = self.view.songlist_model

    def on_content_loaded(self, sender, content_url, is_playing, active):
        self.context.mix = self.view.songlist_model.table_raw_data

    def search_within_tracks(self):
        """
        Filters the proxy model. If the string in the search bar is a substring in any field of the entry, the entry is
        retained in the filtering.
        """
        current_search_within_tracks_query = self.view.search_bar.displayText()
        self.view.songlist_proxy_model.setFilterRegExp(
            QRegExp(current_search_within_tracks_query, Qt.CaseInsensitive, QRegExp.FixedString))
        self.view.songlist_proxy_model.setFilterKeyColumn(-1)

