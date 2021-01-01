import ctypes
import select
from inotify.functions import inotify_init, inotify_add_watch, inotify_rm_watch
from inotify.const import IN_ALL_EVENTS
import inotify.structure
import os


class inotifier(Object):
    def __init__(self):
        self.__fd = inotify_init()
        self.__watches = {}
        self.__epoll = select.epoll()
        self.__epoll.register(self.__fd, select.POLLIN)


    def add_watch(self, path):
        value = inotify_add_watch(self.__fd, path, )
        self.__watches[path] = value


    def remove_watch(self, path):
        inotify_rm_watch(self.__fd, self.__watches[path])
        del self.__watches[path]


    def read_event(self, fd):
        return os.read(fd, inotify.structure.INOTIFY_EVENT_SIZE)


    def get_events():
        while True:
            events = self.__epoll.poll()
            for fd, _ in events:
                yield self.read_event(fd)