from PyQt5.QtWidgets import QHBoxLayout, QCheckBox, QGroupBox, QWidget
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette, QColor
from Label import Label


class HBoxLayoutStatic(QGroupBox):
    """
    Класс для настройки QHBoxLayout
    """

    def __init__(self, text='', color='#ffffff'):
        super().__init__()

        layout = QHBoxLayout(self)

        # groupBox = QGroupBox()
        # self.setFixedSize(20, 100)

        # layout.addWidget(groupBox,  QtCore.Qt.AlignRight)

        label = Label(text)
        label.setColor('#000000')
        layout.addWidget(label, QtCore.Qt.AlignLeft)

        label = Label('0')
        label.setColor('#000000')
        layout.addWidget(label)
        self.setStyleSheet('QGroupBox {background-color: ' + color + '; border-radius: 4px; border: 15px}')



