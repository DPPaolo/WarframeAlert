# coding=utf-8
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt

from warframeAlert.utils.fileUtils import get_cur_dir


class CommonImages():

    def __init__(self):
        self.pixmap = QtGui.QPixmap()
        self.image = QtWidgets.QLabel()
        self.image.setPixmap(self.pixmap)

    def set_image(self, url_image):
        res = self.pixmap.load(get_cur_dir() + url_image)
        if (not res):
            # TODO remove and handle this with the download
            print("Immagine non valida : " + url_image)
        else:
            self.image.setPixmap(self.pixmap)

    def set_image_dimension(self, width, height, aspect_ratio=Qt.IgnoreAspectRatio):
        self.image.setPixmap(self.pixmap.scaled(width, height, aspect_ratio))
