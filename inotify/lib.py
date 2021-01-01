import ctypes
from ctypes.util import find_library

_lib_path = find_library("c")
LIBRARY = ctypes.cdll.LoadLibrary(_lib_path)