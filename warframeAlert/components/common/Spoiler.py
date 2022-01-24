# coding=utf-8
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import QParallelAnimationGroup, QPropertyAnimation, QAbstractAnimation
from PyQt6.QtWidgets import QSizePolicy


class Spoiler(QtWidgets.QWidget):

    def __init__(self, title: str = "") -> None:
        super().__init__()

        # toggle button to open/close the spoiler
        self.toggleButton = QtWidgets.QToolButton()
        self.toggleButton.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toggleButton.setArrowType(QtCore.Qt.ArrowType.RightArrow)
        self.toggleButton.setText(title)
        self.toggleButton.setCheckable(True)
        self.toggleButton.setChecked(False)

        # header line for more visibility
        self.headerLine = QtWidgets.QFrame()
        self.headerLine.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.headerLine.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.headerLine.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)

        # content area of the spoiler
        self.contentArea = QtWidgets.QScrollArea()
        self.contentArea.setStyleSheet("QScrollArea { background-color: white; border: none; }")
        self.contentArea.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.contentArea.setWidgetResizable(True)
        # start auto collapsed
        self.contentArea.setMaximumHeight(0)
        self.contentArea.setMinimumHeight(0)

        # let the entire widget grow and shrink with its content
        self.toggleAnimation = QParallelAnimationGroup()
        self.toggleAnimation.addAnimation(QPropertyAnimation(self, b"minimumHeight"))
        self.toggleAnimation.addAnimation(QPropertyAnimation(self, b"maximumHeight"))
        self.toggleAnimation.addAnimation(QPropertyAnimation(self.contentArea, b"maximumHeight"))

        # don't waste space
        self.mainLayout = QtWidgets.QGridLayout()
        self.mainLayout.setVerticalSpacing(0)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        self.mainLayout.addWidget(self.toggleButton, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.mainLayout.addWidget(self.headerLine, 0, 2, 1, 1)
        self.mainLayout.addWidget(self.contentArea, 1, 0, 1, 3)

        self.setLayout(self.mainLayout)

        self.toggleButton.clicked.connect(self.spoiler_clicked)

    def spoiler_clicked(self, checked) -> None:
        arrow_type = QtCore.Qt.ArrowType.DownArrow if checked else QtCore.Qt.ArrowType.RightArrow
        self.toggleButton.setArrowType(arrow_type)
        direction = QAbstractAnimation.Direction.Forward if checked else QAbstractAnimation.Direction.Backward
        self.toggleAnimation.setDirection(direction)
        self.toggleAnimation.start()

    def set_content_layout(self, spoiler_content: QtWidgets.QHBoxLayout | QtWidgets.QVBoxLayout):
        self.contentArea.setLayout(spoiler_content)

        collapsed_height = self.mainLayout.sizeHint().height() - self.contentArea.maximumHeight()
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
    