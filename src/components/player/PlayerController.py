from PyQt5.QtCore import QTimer
from time import sleep
import asyncio
from threading import Thread

class PlayerController:

    def __init__(self, view, context):
        self._context = context
        self._view = view

        self.pbar_timer = QTimer()
        self.pbar_timer.timeout.connect(self.update_progress_bar)
        self.pbar_timer.setInterval(1000)

    @property
    def view(self):
        return self._view

    @property
    def context(self):
        return self._context

    def on_track_content_loaded(self, sender, content_url, is_playing, active):
        self.now_playing = self._context.deezer.get_entity_from_dz_url(content_url)
        pb = self.view.progress_bar
        pb.setValue(0)
        pb.setFormat(str(self.now_playing))
        self.pbar_timer.start()

    def update_progress_bar(self):
        print('hit')