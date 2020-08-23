# coding=utf-8
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from warframeAlert.components.common.CommonImages import CommonImages


class CommonLabelWithImage():

    def __init__(self, url_image, before="", after=""):
        self.TextBefore = QtWidgets.QLabel(before)
        self.Image = CommonImages()
        self.Image.set_image(url_image)
        self.Image.set_image_dimension(20, 20)
        self.TextAfter = QtWidgets.QLabel(after)

        self.LabelWithImage = QtWidgets.QHBoxLayout()
        self.LabelWithImage.addWidget(self.TextBefore)
        self.LabelWithImage.addWidget(self.Image.image)
        self.LabelWithImage.addWidget(self.TextAfter)
        self.LabelWithImage.addStretch(1)

    def set_after_text(self, text):
        self.TextAfter.setText(text)

    def set_before_text(self, text):
        self.TextBefore.setText(text)

    def set_image(self, url_image):
        self.Image.set_image(url_image)

    def set_image_dimension(self, width, height, aspect_ratio=Qt.IgnoreAspectRatio):
        self.Image.set_image_dimension(width, height, aspect_ratio)

    def hide(self):
        self.Image.hide()
        self.TextAfter.hide()
        self.TextBefore.hide()
