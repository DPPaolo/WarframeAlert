# coding=utf-8
import filecmp
import lzma
import os
import platform
import shutil
import sys


def get_os_type() -> str:
    return platform.system().lower()


def is_mac_os() -> bool:
    return get_os_type() == "darwin"


def is_linux_os() -> bool:
    return get_os_type() == "linux"


def is_windows_os() -> bool:
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
    # default folders for downloaded content
    if (not check_folder("images")):
        os.makedirs(d + get_separator() + "images")
    if (not check_folder("images" + get_separator() + "news")):
        os.makedirs(d + get_separator() + "images" + get_separator() + "news")
    if (not check_folder("data")):
        os.makedirs(d + get_separator() + "data")
    # default folders for mandatory files
    if (not check_folder("assets")):
        os.makedirs(d + get_separator() + "assets")
    if (not check_folder("assets" + get_separator() + "icon")):
        os.makedirs(d + get_separator() + "assets" + get_separator() + "icon")
    if (not check_folder("assets" + get_separator() + "image")):
        os.makedirs(d + get_separator() + "assets" + get_separator() + "image")
    if (not check_folder("translation")):
        os.makedirs(d + get_separator() + "translation")


def check_mandatory_files() -> None:
    create_default_folder()

    # Copy bundled files if missing
    if (getattr(sys, 'frozen', False)):
        check_bundled_files_missing()


def check_bundled_files_missing() -> None:
    path = getattr(sys, '_MEIPASS', os.getcwd())
    if (not are_dir_trees_equal(path + get_separator() + "assets", "assets")):
        shutil.copytree(path + get_separator() + "assets" + get_separator() + "icon",
                        "assets" + get_separator() + "icon", dirs_exist_ok=True)
        shutil.copytree(path + get_separator() + "assets" + get_separator() + "image",
                        "assets" + get_separator() + "image", dirs_exist_ok=True)
    if (not are_dir_trees_equal(path + get_separator() + "translation", "translation")):
        shutil.copytree(path + get_separator() + "translation", "translation", dirs_exist_ok=True)


def are_dir_trees_equal(directory1: str, directory2: str) -> bool:
    """
    Compare two directories recursively. Files in each directory are
    assumed to be equal if their names and contents are equal.

    @param directory1: First directory path
    @param directory2: Second directory path

    @return: True if the directory trees are the same and
        there were no errors while accessing the directories or files,
        False otherwise.
   """

    dirs_cmp = filecmp.dircmp(directory1, directory2)
    if len(dirs_cmp.left_only) > 0 or len(dirs_cmp.right_only) > 0 or len(dirs_cmp.funny_files) > 0:
        return False
    (_, mismatch, errors) = filecmp.cmpfiles(directory1, directory2, dirs_cmp.common_files, shallow=False)
    if len(mismatch) > 0 or len(errors) > 0:
        return False
    for common_dir in dirs_cmp.common_dirs:
        new_dir1 = os.path.join(directory1, common_dir)
        new_dir2 = os.path.join(directory2, common_dir)
        if not are_dir_trees_equal(new_dir1, new_dir2):
            return False
    return True


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
