import os

from warframeAlert.utils.commonUtils import get_separator


def abspath(path):
    cwd = os.getcwd()
    path = os.path.join(cwd, path)
    return path


def get_cur_dir():
    return os.path.dirname(abspath(os.curdir))


def get_asset_path():
    return get_cur_dir() + get_separator() + "assets" + get_separator()


def check_file(name):
    d = get_cur_dir()
    path = d + get_separator() + name
    return os.path.exists(path)


def check_folder(name):
    d = get_cur_dir()
    return os.path.isdir(d + get_separator() + name)


def create_default_folder():
    d = get_cur_dir()
    if (not check_folder("images")):
        os.makedirs(d + get_separator() + "images")
    if (not check_folder("data")):
        os.makedirs(d + get_separator() + "data")
