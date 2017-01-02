#!/usr/bin/env python
# coding: utf8
from src.deenuxapi.Model import Model
from src.deenuxapi.deezer.wrapper.deezer_player import *
from src.deenuxapi.deezer.Config import Config
from enum import Enum

# TODO: clear debugging code and logs
class Jukebox():
    """
    A simple deezer application using NativeSDK
    Initialize a connection and a player, then load and play a song.
    """

    class AppContext(object):
        """
        Can be used to pass a context to store various info and pass them
        to your callbacks
        """
        def __init__(self):
            self.nb_track_played = 0
            self.dz_content_url = ""
            self.repeat_mode = 0
            self.is_shuffle_mode = False
            self.connect_handle = 0
            self.player_handle = 0

    def __init__(self, token: str, debug_mode=True):
        self.debug_mode = debug_mode

        if platform.system() == u'Windows':
            self.user_cache_path = u"c:\\dzr\\dzrcache_NDK_SAMPLE"  # SET the user cache path, the path must exist
        else:
            self.user_cache_path = u"/var/tmp/dzrcache_NDK_SAMPLE"  # SET the user cache path, the path must exist
        self.context = self.AppContext()

        self.connection = Connection(
            self,
            Config.get_app_setting('id'),
            Config.get_app_setting('name'),
            Config.get_app_setting('version'),
            self.user_cache_path,
            self.connection_event_callback, 0, 0
        )

        self.player_cb = dz_on_event_cb_func(self.player_event_callback)
        self.cache_path_set_cb = dz_activity_operation_cb_func()  # TODO: no callback for cache_path
        if not self.debug_mode:
            self.connection.debug_log_disable()
        else:
            print ("Device ID:", self.connection.get_device_id())
        self.player = Player(self, self.connection.handle)
        self.player.set_event_cb(self.player_cb)
        self.connection.cache_path_set(self.connection.user_profile_path.encode('utf8'), activity_operation_cb=self.cache_path_set_cb,
                                       operation_userdata=self)
        self.connection.set_access_token(token.encode('utf8'))
        self.connection.set_offline_mode(False)
        self.context.player_handle = self.player.handle
        self.context.connect_handle = self.connection.handle
        self.dz_player_deactivate_cb = dz_activity_operation_cb_func(self.player_on_deactivate_cb)
        self.dz_connect_deactivate_cb = dz_activity_operation_cb_func(self.connection_on_deactivate_cb)

    def log(self, message):
        """
        Print a log message unless debug_mode is False
        :param message: The message to display
        """
        if self.debug_mode:
            print (message)

    class Playables(Enum):
        TRACK = 'track'
        ALBUM = 'album'
        PLAYLIST = 'playlist'
        USER = "user"
        RADIO = "radio"

    def start_playback(self, playable: Playables, entity: Model):
        if (playable != Jukebox.Playables.USER and playable != Jukebox.Playables.RADIO):
            url = "dzmedia:///{0}/2222808742"
        else:
            url = "dzradio:///{0}-{1}"

        self._load_content(url.format(playable.value, entity.id).encode('utf8'))
        self.player.play()

    def stop_playback(self):
        if self.player.is_playing:
            self.player.stop()

    def toggle_play_pause(self):
        if self.player.is_playing:
            self.log("PAUSE track n° {} of => {}".format(self.context.nb_track_played, self.context.dz_content_url))
            self.player.pause()
        else:
            self.log("RESUME track n° {} of => {}".format(self.context.nb_track_played, self.context.dz_content_url))
            self.player.resume()

    def next(self):
        self.log("NEXT => {}".format(self.context.dz_content_url))
        self.player.play(command=PlayerCommand.START_TRACKLIST, index=PlayerIndex.NEXT)

    def previous(self):
        self.log("PREVIOUS => {}".format(self.context.dz_content_url))
        self.player.play(command=PlayerCommand.START_TRACKLIST, index=PlayerIndex.PREVIOUS)

    def playback_toggle_repeat(self):
        self.context.repeat_mode += 1
        if self.context.repeat_mode > PlayerRepeatMode.ALL:
            self.context.repeat_mode = PlayerRepeatMode.OFF
        self.log("REPEAT mode => {}".format(self.context.repeat_mode))
        self.player.set_repeat_mode(self.context.repeat_mode)

    def playback_toggle_random(self):
        self.context.is_shuffle_mode = not self.context.is_shuffle_mode
        self.log("SHUFFLE mode => {}".format("ON" if self.context.is_shuffle_mode else "OFF"))
        self.player.enable_shuffle_mode(self.context.is_shuffle_mode)

    def _load_content(self, content):
        """Load the given dzmedia content.
        It will replace the current_content of the player class
        :param content: The content to load
        :type content: str
        """
        self.log("LOAD => {}".format(self.context.dz_content_url))
        self.context.dz_content_url = content
        self.player.load(content)

    def shutdown(self):
        """Stop the connection and the player if they have been initialized"""
        if self.context.player_handle:
            self.log("SHUTDOWN PLAYER - player_handle = {}".format(self.context.player_handle))
            self.player.shutdown(activity_operation_cb=self.dz_player_deactivate_cb,
                                 operation_user_data=self)
        elif self.context.connect_handle:
            self.log("SHUTDOWN CONNECTION - connect_handle = {}".format(self.context.connect_handle))
            self.connection.shutdown(activity_operation_cb=self.dz_connect_deactivate_cb,
                                     operation_user_data=self)

    # We set the callback for player events, to print various logs and listen to events
    @staticmethod
    def player_event_callback(handle, event, userdata):
        """Listen to events and call the appropriate functions
        :param handle: The player handle.
        :type: p_type
        :param event: The corresponding event.
            Must be converted using Player.get_event
        :type: dz_player_event_t
        :param userdata: Any data you want to be passed and used here
        :type: ctypes.py_object
        :return: int
        """
        # We retrieve our deezer app
        app = cast(userdata, py_object).value
        event_type = Player.get_event(event)
        if event_type == PlayerEvent.QUEUELIST_TRACK_SELECTED:
            can_pause_unpause = c_bool()
            can_seek = c_bool()
            no_skip_allowed = c_int()
            is_preview = Player.is_selected_track_preview(event)
            Player.event_track_selected_rights(event, can_pause_unpause, can_seek, no_skip_allowed)
            selected_dz_api_info = Player.event_track_selected_dzapiinfo(event)
            next_dz_api_info = Player.event_track_selected_next_track_dzapiinfo(event)
            app.log(u"==== PLAYER_EVENT ==== {0} - is_preview: {1}"
                    .format(PlayerEvent.event_name(event_type), is_preview))
            app.log(u"\tcan_pause_unpause: {0} - can_seek: {1}"
                    .format(can_pause_unpause.value, can_seek.value))
            if selected_dz_api_info:
                app.log(u"\tnow:{0}".format(selected_dz_api_info))
            if next_dz_api_info:
                app.log(u"\tnext:{0}".format(next_dz_api_info))
            return 0
        app.log(u"==== PLAYER_EVENT ==== {0}".format(PlayerEvent.event_name(event_type)))
        if event_type == PlayerEvent.QUEUELIST_LOADED:
            app.player.play()
        if event_type == PlayerEvent.QUEUELIST_TRACK_RIGHTS_AFTER_AUDIOADS:
            app.player.play_audio_ads()
        return 0

    # We set the connection callback to launch the player after connection is established
    @staticmethod
    def connection_event_callback(handle, event, userdata):
        """Listen to events and call the appropriate functions
        :param handle: The connect handle.
        :type: p_type
        :param event: The corresponding event.
            Must be converted using Connection.get_event
        :type: dz_connect_event_t
        :param userdata: Any data you want to be passed and used here
        :type: ctypes.py_object
        :return: int
        """
        # We retrieve our deezerApp
        app = cast(userdata, py_object).value
        event_type = Connection.get_event(event)
        app.log(u"++++ CONNECT_EVENT ++++ {0}".format(ConnectionEvent.event_name(event_type)))
        # After User is authenticated we can start the player
        if event_type == ConnectionEvent.USER_LOGIN_OK:
            app.player.load(app.context.dz_content_url)
        if event_type == ConnectionEvent.USER_LOGIN_FAIL_USER_INFO:
            app.shutdown()
        return 0

    @staticmethod
    def player_on_deactivate_cb(delegate, operation_userdata, status, result):
        """The callback to the shutdown of the player"""
        app = cast(operation_userdata, py_object).value
        app.player.active = False
        app.context.player_handle = 0
        app.log("Player deactivated")
        if app.context.connect_handle:
            app.log("SHUTDOWN CONNECTION - connect_handle = {}".format(app.context.connect_handle))
            app.connection.shutdown(activity_operation_cb=app.dz_connect_deactivate_cb,
                                    operation_user_data=app)
        return 0

    @staticmethod
    def connection_on_deactivate_cb(delegate, operation_userdata, status, result):
        """The callback to the shutdown of the connection"""
        app = cast(operation_userdata, py_object).value
        if app.context.connect_handle:
            app.connection.active = False
            app.context.connect_handle = 0
        app.log("Connection deactivated")
        return 0
