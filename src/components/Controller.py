from PyQt5.QtCore import QRunnable, QThreadPool


class Controller:

    thread_pool = QThreadPool()

    def __init__(self, view=None, context=None):
        self._view = view
        self._context = context

    @property
    def context(self):
        return self._context

    @property
    def view(self):
        return self._view

    class Worker(QRunnable):
        
        def __init__(self, fn, args, kwargs):
            super().__init__()
            self.__fn = fn
            self.__args = args
            self.__kwargs = kwargs

        def run(self):
            return self.__fn(*self.__args, **self.__kwargs)

    @staticmethod
    def async(decorated):

        def kick_off (*args, **kwargs):
            Controller.thread_pool.start(Controller.Worker(decorated, args, kwargs))

        return kick_off