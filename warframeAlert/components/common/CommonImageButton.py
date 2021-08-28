# coding=utf-8
import webbrowser

from PyQt5 import QtGui, QtWidgets, QtCore

from warframeAlert.components.common.CommonImages import CommonImages
from warframeAlert.utils.fileUtils import get_separator


class CommonImageButton():

    def __init__(self, news_id: str) -> None:
        font = QtGui.QFont()
        font.setBold(True)

        self.url = ""
        self.news_id = news_id
        self.common_image = CommonImages()

        self.palette = QtGui.QPalette()
        self.palette.setColor(QtGui.QPalette.Button, QtGui.QColor(255, 255, 255))

        self.news_button = QtWidgets.QPushButton()
        self.newsLabel = QtWidgets.QLabel("")
        self.newsLabel.setFont(font)
        self.newsLabel.setAlignment(QtCore.Qt.AlignLeft)

        self.news_button.setFixedSize(300, 150)
        self.news_button.setPalette(self.palette)
        self.news_button.setFlat(True)

        self.NewsBox = QtWidgets.QVBoxLayout()

        self.NewsBox.addWidget(self.news_button)
        self.NewsBox.addWidget(self.newsLabel)
        self.news_button.clicked.connect(self.open_link)

    def get_news_id(self) -> str:
        return self.news_id

    def set_image_news(self, image: str, url: str) -> None:
        assets_path = "assets" + get_separator() + "image"
        default_image = assets_path + get_separator() + "default_news_image.jpg"
        if ("default_news_image" in image or "imageproxy.php" in image):
            self.common_image.set_image(default_image)
        else:
            image_path = "images" + get_separator() + "news" + get_separator() + image
            res = self.common_image.set_image(image_path, url)
            if (not res):
                self.common_image.set_image(default_image)
        self.update_image_news_button()

    def update_image_news_button(self) -> None:
        self.news_button.setIcon(QtGui.QIcon(self.common_image.pixmap))
        self.news_button.setIconSize(QtCore.QSize(600, 200))

    def set_text_news_button(self, mess: str) -> None:
        self.newsLabel.setText(mess)

    def set_news_url(self, url: str) -> None:
        self.url = url

    def open_link(self) -> None:
        if (self.url == ""):
            return
        else:
            webbrowser.open(self.url)

    def get_title(self) -> str:
        return self.newsLabel.text()

    def set_tooltip(self, tooltip: str) -> None:
        self.news_button.setToolTip(tooltip)

    def show(self) -> None:
        self.news_button.show()
