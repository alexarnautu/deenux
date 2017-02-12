from src.components.Controller import Controller


class TrackcontrolsController(Controller):

    def __init__(self, view, context):
        super(TrackcontrolsController, self).__init__(view, context)

    @staticmethod
    def _get_from_mix(playing, mix, direction):
        return mix[mix.index(playing) + (1 if direction else -1)] # for now

    def on_next_clicked(self):
        self.context.deezer.jukebox.start(self._get_from_mix(
            self.context.now_playing,
            self.context.mix,
            True
        ))

    def on_prev_clicked(self, *args):
        self.context.deezer.jukebox.start(self._get_from_mix(
            self.context.now_playing,
            self.context.mix,
            False
        ))

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
