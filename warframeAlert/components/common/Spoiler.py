# coding=utf-8
from typing import Union

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QParallelAnimationGroup, QPropertyAnimation, QAbstractAnimation
from PyQt5.QtWidgets import QSizePolicy


class Spoiler(QtWidgets.QWidget):

    def __init__(self, title: str = "") -> None:
        super().__init__()
        self.checked = True

        self.toggleButton = QtWidgets.QToolButton()
        self.toggleButton.setStyleSheet("QToolButton { border: none; }")
        self.toggleButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toggleButton.setArrowType(QtCore.Qt.RightArrow)

        self.toggleButton.setText(title)
        self.toggleButton.setCheckable(True)
        self.toggleButton.setChecked(False)

        self.headerLine = QtWidgets.QFrame()

        self.headerLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.headerLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.headerLine.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)

        self.contentArea = QtWidgets.QScrollArea()

        self.contentArea.setStyleSheet("QScrollArea { background-color: white; border: none; }")
        self.contentArea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.contentArea.setWidgetResizable(True)

        # start outcollapsed
        self.contentArea.setMaximumHeight(0)
        self.contentArea.setMinimumHeight(0)

        # let the entire widget grow and shrink with its content
        self.toggleAnimation = QParallelAnimationGroup()
        self.toggleAnimation.addAnimation(QPropertyAnimation(self, b"minimumHeight"))
        self.toggleAnimation.addAnimation(QPropertyAnimation(self, b"maximumHeight"))
        self.toggleAnimation.addAnimation(QPropertyAnimation(self.contentArea, b"maximumHeight"))

        # don't waste space
        self.mainLaoyut = QtWidgets.QGridLayout()
        self.mainLaoyut.setVerticalSpacing(0)
        self.mainLaoyut.setContentsMargins(0, 0, 0, 0)

        self.mainLaoyut.addWidget(self.toggleButton, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.mainLaoyut.addWidget(self.headerLine, 1, 2, 1, 1)
        self.mainLaoyut.addWidget(self.contentArea, 1, 0, 1, 3)

        self.setLayout(self.mainLaoyut)

        self.toggleButton.clicked.connect(self.spoiler_clicked)

    def spoiler_clicked(self) -> None:
        self.toggleButton.setArrowType(QtCore.Qt.DownArrow if self.checked else QtCore.Qt.RightArrow)
        self.toggleAnimation.setDirection(QAbstractAnimation.Forward if self.checked else QAbstractAnimation.Backward)
        self.toggleAnimation.start()
        self.checked = not self.checked

    # TODO: Use | instead of Union
    def set_content_layout(self, spoiler_content: Union[QtWidgets.QHBoxLayout, QtWidgets.QVBoxLayout]):
        self.contentArea.setLayout(spoiler_content)

        collapsed_height = self.mainLaoyut.sizeHint().height() - self.contentArea.maximumHeight()
        content_height = spoiler_content.sizeHint().height()
        for i in range(self.toggleAnimation.animationCount() - 1):
            spoiler_animation = self.toggleAnimation.animationAt(i)
            spoiler_animation.setDuration(300)
            spoiler_animation.setStartValue(collapsed_height)
            spoiler_animation.setEndValue(collapsed_height + content_height)

        content_animation = self.toggleAnimation.animationAt(self.toggleAnimation.animationCount() - 1)
        content_animation.setDuration(300)
        content_animation.setStartValue(0)
        content_animation.setEndValue(content_height)

        self.contentArea.resize(self.contentArea.maximumHeight(), self.contentArea.maximumWidth())
