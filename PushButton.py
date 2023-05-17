from PyQt5.QtWidgets import (QPushButton)
from PyQt5.QtGui import QFont


class PushButton(QPushButton):

    def __init__(self, text='', color='', parent=None):
        self.color = color
        self.flag = True

        super().__init__(text, parent)
        self.setStyleSheet("QPushButton {background-color: #ffffff;}"
                           "QPushButton::hover {background-color : " + color + ";}")

        self.setFont(QFont("Roboto", 12))

        self.clicked.connect(self.setStyleHover)

    def setStyleHover(self):
        if self.flag:
            self.flag = False
            self.setStyleSheet("QPushButton {background-color : " + self.color + ";}"
                               "QPushButton::hover {background-color : #ffffff;}")
        else:
            self.flag = True
            self.setStyleSheet("QPushButton {background-color: #ffffff;}"
                               "QPushButton::hover {background-color : " + self.color + ";}")