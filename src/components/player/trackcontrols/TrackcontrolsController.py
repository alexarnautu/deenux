from src.components.Controller import Controller
from random import shuffle
from src.deenuxapi.deezer.DeezerProvider import DeezerProvider
from src.utils.Sequence import Sequence


class TrackcontrolsController(Controller):

    def __init__(self, view, context):
        super(TrackcontrolsController, self).__init__(view, context)

    def on_track_play_start(self, sender, content_url, is_playing, active):
        pass

    def on_shuffle_click(self):
        self.context.deezer.jukebox.toggle_random()
        self.view.shuffle_button.setText('not' if self.context.shuffle else 'sh')
    
        self.context.shuffle = not self.context.shuffle

    def on_next_clicked(self):
        self.context.deezer.jukebox.start(
            self.context.mix[self.context.sequence.next]
        )

    def on_prev_clicked(self, *args):
        self.context.deezer.jukebox.start(
            self.context.mix[self.context.sequence.prev]
        )

    def on_play_pause_click(self):
        jb = self.context.deezer.jukebox
        if not self.context.player.active:
            jb.start(self.context.to_play)
        else:
            jb.toggle_play_pause()

    def on_volume_change(self, val):
        was_blocked = self.view.volume_slider.blockSignals(True)
        self.context.deezer.jukebox.set_volume(val * 5)
        self.view.volume_slider.blockSignals(was_blocked)

    def on_track_stop(self):
        self.view.active = False
        self.view.play_pause_button.setText('▶')

        self.on_next_clicked()

