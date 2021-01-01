from inotify.lib import LIBRARY
from inotify.inotify_error import inotify_error
import ctypes

def _check_not_neg1(value):
    if -1 == value:
        raise inotify_error("Return value should not be -1.")
    return value

inotify_init = LIBRARY.inotify_init
inotify_init.restype = _check_not_neg1

inotify_add_watch = LIBRARY.inotify_add_watch
inotify_add_watch.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_uint32]
inotify_add_watch.restype = _check_not_neg1

inotify_rm_watch = LIBRARY.inotify_rm_watch
inotify_rm_watch.argtypes = [ctypes.c_int, ctypes.c_int]
inotify_rm_watch.restype = _check_not_neg1