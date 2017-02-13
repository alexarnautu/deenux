from PyQt5.QtCore import QTimer
from time import sleep
from threading import Thread
import time

from src.components.Controller import Controller


class PlayerController(Controller):

    def __init__(self, view, context):
        super(PlayerController, self).__init__(view, context)

    @Controller.async
    def on_track_content_loaded(self, sender, content_url, is_playing, active):
        self.context.now_playing = None
        pb = self.view.track_info.progress_bar
        pb.setValue(0)
        pb.setMaximum(99999999)
        self.view.track_info.playing_label.setText("Loading...")
        self.context.now_playing = self._context.deezer.get_entity_from_dz_url(content_url)
        pb.setMaximum(self.context.now_playing.duration * 10)
        self.view.track_info.playing_label.setText(str(self.context.now_playing))

    def on_track_play_start(self, *args):
        v = self.view
        v.track_info.controller.update_progress_bar()
        v.track_info.pbar_timer.start()

        v.track_controls.play_pause_button.setText('▮▮')
        v.active = True
        v.track_controls.next_button.setEnabled(True)
        v.track_controls.prev_button.setEnabled(True)

    def on_track_pause(self):
        self.view.track_controls.play_pause_button.setText('▶')
        self.view.track_info.pbar_timer.stop()

    def on_track_resume(self):
        self.view.track_controls.play_pause_button.setText('▮▮')
        self.view.track_info.pbar_timer.start()

