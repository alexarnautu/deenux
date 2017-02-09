from PyQt5.QtCore import QTimer
from time import sleep
from threading import Thread
import time

class PlayerController:

    def __init__(self, view, context):
        self._context = context
        self._view = view

        self.__pbar_timer = QTimer()
        self.__pbar_timer.timeout.connect(self.update_progress_bar)
        self.__pbar_timer.setInterval(100) # 1/10 seconds, 1000 milliseconds

    @property
    def view(self):
        return self._view

    @property
    def context(self):
        return self._context

    def on_track_content_loaded(self, sender, content_url, is_playing, active):
        self.now_playing = self._context.deezer.get_entity_from_dz_url(content_url)
        pb = self.view.progress_bar
        pb.setMaximum(self.now_playing.duration * 10)
        pb.setValue(0)
        pb.setFormat(str(self.now_playing))

    def on_track_play_start(self, *args):
        self.update_progress_bar()
        self.view.play_pause_button.setText('▮▮')
        self.view.active = True
        self.view.next_button.setEnabled(True)
        self.view.prev_button.setEnabled(True)
        self.__pbar_timer.start()

    def update_progress_bar(self):
        pb_v = self.view.progress_bar.value()
        self.view.progress_bar.setValue(pb_v + 1)
        if (pb_v == self.now_playing.duration * 10):
            self.__pbar_timer.stop()

    def on_track_pause(self):
        self.view.play_pause_button.setText('▶')
        self.__pbar_timer.stop()

    def on_track_resume(self):
        self.view.play_pause_button.setText('▮▮')
        self.__pbar_timer.start()

    def on_play_pause_click(self):
        jb = self.context.deezer.jukebox
        if not self.view.active:
            jb.start(self.view.to_play)
        else:
            jb.toggle_play_pause()

    def on_track_stop(self):
        self.view.active = False
        self.view.play_pause_button.setText('▶')

    def on_volume_change(self, val):

        was_blocked = self.view.volume_slider.blockSignals(True)
        self.context.deezer.jukebox.set_volume(val // 3)
        self.view.volume_slider.blockSignals(was_blocked)

