import os
import platform
import sys
import traceback


def print_traceback(mess):
    print(mess)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback)


def abspath(path):
    cwd = os.getcwd()
    path = os.path.join(cwd, path)
    return path


def get_cur_dir():
    return os.path.dirname(abspath(os.curdir))


def get_os_type():
    return platform.system()


def get_separator():
    sep = "\\"  # Windos default separator
    if (get_os_type() == "Darwin"):  # the OS is a MacOs
        sep = "/"
    return sep


def check_file(name):
    d = get_cur_dir()
    path = d + get_separator() + name
    return os.path.exists(path)
