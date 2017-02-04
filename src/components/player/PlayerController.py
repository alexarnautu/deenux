

class PlayerController:

    def __init__(self, context):
        self._context = context

    def on_track_content_loaded(self, sender):
        print(sender.last_played)