# coding=utf-8
import lzma
import os
import platform
import shutil
import sys


def get_os_type() -> str:
    return platform.system()


def is_mac_os() -> bool:
    return get_os_type() == "Darwin"


def is_linux_os() -> bool:
    return get_os_type() == "Linux"


def is_window_os() -> bool:
    return not is_mac_os() and not is_linux_os()


def get_separator() -> str:
    sep = "\\"  # Windows default separator
    if (is_mac_os() or is_linux_os()):  # the OS is a macOS or Linux
        sep = "/"
    return sep


def abspath(path: str) -> str:
    cwd = os.getcwd()
    path = os.path.join(cwd, path)
    return path


def get_cur_dir() -> str:
    return os.path.dirname(abspath(os.curdir))


def get_asset_path() -> str:
    return get_cur_dir() + get_separator() + "assets" + get_separator()


def check_file(name: str) -> bool:
    d = get_cur_dir()
    path = d + get_separator() + name
    image_path = d + get_separator() + "images" + get_separator() + name
    news_path = d + get_separator() + "images" + get_separator() + "news" + name
    files_path = d + get_separator() + "data" + get_separator() + name
    return os.path.exists(path) or os.path.exists(image_path) or os.path.exists(files_path) or os.path.exists(news_path)


def check_assets_file(name: str) -> bool:
    if ("." not in name):
        name += ".png"
    d = get_cur_dir()
    icon_path = d + get_separator() + "assets" + get_separator() + "icon" + get_separator() + name
    image_path = d + get_separator() + "assets" + get_separator() + "image" + get_separator() + name
    validator_path = d + get_separator() + "assets" + get_separator() + "validator" + get_separator() + name
    return os.path.exists(icon_path) or os.path.exists(image_path) or os.path.exists(validator_path)


def check_folder(name: str) -> bool:
    d = get_cur_dir()
    return os.path.isdir(d + get_separator() + name)


def delete_file(path: str) -> None:
    if (os.path.exists(path)):
        os.remove(path)


def create_default_folder() -> None:
    d = get_cur_dir()
    if (not check_folder("images")):
        os.makedirs(d + get_separator() + "images")
    if (not check_folder("images" + get_separator() + "news")):
        os.makedirs(d + get_separator() + "images" + get_separator() + "news")
    if (not check_folder("data")):
        os.makedirs(d + get_separator() + "data")


def copy_bundled_files_to_current_dir() -> None:
    path = getattr(sys, '_MEIPASS', os.getcwd())
    shutil.copytree(path + get_separator() + "assets" + get_separator() + "icon", "assets" + get_separator() + "icon")
    shutil.copytree(path + get_separator() + "assets" + get_separator() + "image", "assets" + get_separator() + "image")
    shutil.copytree(path + get_separator() + "translation", "translation")


def decompress_lzma(data: bytes) -> bytes:
    results = []
    while True:
        decompressor = lzma.LZMADecompressor(lzma.FORMAT_AUTO, None, None)
        try:
            res = decompressor.decompress(data)
        except lzma.LZMAError:
            if results:
                break  # Leftover data is not a valid LZMA/XZ stream; ignore it.
            else:
                raise  # Error on the first iteration; bail out.
        results.append(res)
        data = decompressor.unused_data
        if not data:
            break
        if not decompressor.eof:
            raise lzma.LZMAError("Compressed data ended before the end-of-stream marker was reached")
    return b"".join(results)
