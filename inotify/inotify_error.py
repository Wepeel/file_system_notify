import ctypes
import os

def inotify_error(Object):
    
    def __init__(self, message):
        self.__errno = ctypes.get_errno()
        self.message = message + f"Error: {os.strerror(self.__errno)}"
        super(inotify_error, self).__init__(self.message)