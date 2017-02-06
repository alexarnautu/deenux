

class PlayerController:

    def __init__(self, context):
        self._context = context

    @property
    def context(self):
        return self._context

    def on_track_content_loaded(self, sender, content_url, is_playing, active):
        print(self._context.deezer.get_entity_from_dz_url(content_url))