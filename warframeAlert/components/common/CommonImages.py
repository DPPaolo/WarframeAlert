# coding=utf-8
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt

from warframeAlert.services import networkService
from warframeAlert.utils.fileUtils import get_cur_dir, get_separator, check_file, delete_file


class CommonImages():

    def __init__(self):
        self.pixmap = QtGui.QPixmap()
        self.image = QtWidgets.QLabel()
        self.image.setPixmap(self.pixmap)
        self.width = 50
        self.height = 50
        self.aspect_ratio = Qt.IgnoreAspectRatio
        self.trasform = Qt.SmoothTransformation
        self.downloader_thread = None

    def set_image(self, path_image, url_download_image=None):
        current_dir = get_cur_dir()
        path = current_dir + get_separator() + path_image
        if ("assets" in path_image):
            res = self.pixmap.load(path)
            if (res):
                self.image.setPixmap(self.pixmap)
            return res
        elif (not check_file(path_image)):
            url = url_download_image
            self.downloader_thread = networkService.Downloader(url, path)
            self.downloader_thread.start()
            self.downloader_thread.download_completed.connect(lambda: self.set_image(path_image, url_download_image))
            return False
        else:
            res = self.pixmap.load(path)
            if (res):
                self.image.setPixmap(self.pixmap)
                self.set_image_dimension(self.width, self.height, self.aspect_ratio, self.trasform)
            else:
                # the downloaded file is corrupted
                delete_file(path_image)
            return res

    def set_image_dimension(self, width, height, aspect_ratio=Qt.IgnoreAspectRatio, trasform=Qt.SmoothTransformation):
        self.width = width
        self.height = height
        self.aspect_ratio = aspect_ratio
        self.trasform = trasform
        self.image.setPixmap(self.pixmap.scaled(width, height, aspect_ratio, trasform))

    def set_tooltip(self, tooltip):
        self.image.setToolTip(tooltip)

    def hide(self):
        self.image.hide()
