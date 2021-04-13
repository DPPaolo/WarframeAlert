# coding=utf-8
import lzma
import os
import platform
import shutil
import sys


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
    image_path = d + get_separator() + "images" + get_separator() + name
    news_path = d + get_separator() + "images" + get_separator() + "news" + name
    files_path = d + get_separator() + "data" + get_separator() + name
    return os.path.exists(path) or os.path.exists(image_path) or os.path.exists(files_path) or os.path.exists(news_path)


def check_folder(name):
    d = get_cur_dir()
    return os.path.isdir(d + get_separator() + name)


def delete_file(path):
    if (os.path.exists(path)):
        os.remove(path)


def create_default_folder():
    d = get_cur_dir()
    if (not check_folder("images")):
        os.makedirs(d + get_separator() + "images")
    if (not check_folder("images" + get_separator() + "news")):
        os.makedirs(d + get_separator() + "images" + get_separator() + "news")
    if (not check_folder("data")):
        os.makedirs(d + get_separator() + "data")


def copy_bundled_files_to_current_dir():
    path = getattr(sys, '_MEIPASS', os.getcwd())
    shutil.copytree(path + get_separator() + "assets" + get_separator() + "icon", "assets" + get_separator() + "icon")
    shutil.copytree(path + get_separator() + "assets" + get_separator() + "image", "assets" + get_separator() + "image")
    shutil.copytree(path + get_separator() + "translation", "translation")


def decompress_lzma(data):
    results = []
    while True:
        decomp = lzma.LZMADecompressor(lzma.FORMAT_AUTO, None, None)
        try:
            res = decomp.decompress(data)
        except lzma.LZMAError:
            if results:
                break  # Leftover data is not a valid LZMA/XZ stream; ignore it.
            else:
                raise  # Error on the first iteration; bail out.
        results.append(res)
        data = decomp.unused_data
        if not data:
            break
        if not decomp.eof:
            raise lzma.LZMAError("Compressed data ended before the end-of-stream marker was reached")
    return b"".join(results)

