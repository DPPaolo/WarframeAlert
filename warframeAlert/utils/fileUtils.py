# coding=utf-8
import os
import platform


def get_os_type():
    return platform.system()


def is_mac_os():
    return get_os_type() == "Darwin"


def is_linux_os():
    return get_os_type() == "Linux"


def get_separator():
    sep = "\\"  # Windows default separator
    if (is_mac_os() or is_linux_os()):  # the OS is a MacOs or Linux
        sep = "/"
    return sep


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
    images_path = d + get_separator() + "images" + get_separator() + name
    files_path = d + get_separator() + "data" + get_separator() + name
    return os.path.exists(path) or os.path.exists(images_path) or os.path.exists(files_path)


def check_folder(name):
    d = get_cur_dir()
    return os.path.isdir(d + get_separator() + name)


def create_default_folder():
    d = get_cur_dir()
    if (not check_folder("images")):
        os.makedirs(d + get_separator() + "images")
    if (not check_folder("data")):
        os.makedirs(d + get_separator() + "data")
