import os
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


def check_file(name):
    d = get_cur_dir()
    return os.path.exists(d + "\\" + name)
