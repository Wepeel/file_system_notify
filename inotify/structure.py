import ctypes

class inotify_event(ctypes.Structure):
    _fields_ = [
        ("wd", ctypes.c_int),
        ("mask", ctypes.c_uint32),
        ("cookie", ctypes.c_uint32),
        ("len", ctypes.c_uint32),
        ("name", ctypes.c_char_p)
    ]

INOTIFY_EVENT_SIZE = ctypes.sizeof(inotify)