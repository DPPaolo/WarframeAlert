# coding=utf-8
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt

from warframeAlert.utils.fileUtils import get_cur_dir, get_separator


class CommonImages():

    def __init__(self):
        self.pixmap = QtGui.QPixmap()
        self.image = QtWidgets.QLabel()
        self.image.setPixmap(self.pixmap)

    def set_image(self, url_image):
        res = self.pixmap.load(get_cur_dir() + get_separator() + url_image)
        if (not res):
            # if (not check_file(image1)):
            #    warframe.download_image_from_name(img1)
            # TODO remove and handle this with the download
            print("Immagine non valida : " + get_cur_dir() + url_image)
        else:
            self.image.setPixmap(self.pixmap)

    def set_image_dimension(self, width, height, aspect_ratio=Qt.IgnoreAspectRatio, trasform=Qt.SmoothTransformation):
        self.image.setPixmap(self.pixmap.scaled(width, height, aspect_ratio, trasform))

    def set_tooltip(self, tooltip):
        self.image.setToolTip(tooltip)

    def hide(self):
        self.image.hide()
