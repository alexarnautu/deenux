from src.components.Controller import Controller

class TrackinfoController(Controller):

    def __init__(self, view, context):
        super(TrackinfoController, self).__init__(view, context)

    def update_progress_bar(self):
        pb_v = self.view.progress_bar.value()
        self.view.progress_bar.setValue(pb_v + 1)
        tm, ts = divmod(self.context.now_playing.duration, 60)
        cm, cs = divmod(pb_v // 10, 60)
        self.view.time_label.setText("%02d:%02d / %02d:%02d" % (cm, cs, tm, ts))
        if pb_v == self.context.now_playing.duration * 10:
            self.__pbar_timer.stop()

    def on_progress_bar_pressed(self):
        pass

    def on_progress_bar_released(self):
        val = self.view.progress_bar.value()
        if val == self.context.now_playing.duration * 10:
            val -= 1
            self.context.deezer.jukebox.seek(val * 100)

    def on_progress_bar_value_changed(self):
        pass
