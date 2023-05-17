from PyQt5.QtWidgets import QHBoxLayout, QCheckBox, QGroupBox, QWidget
from PyQt5 import QtCore
from Label import Label


class HBoxLayoutStatic(QWidget):
    """
    Класс для настройки QHBoxLayout
    """

    def __init__(self, text='', color='#ffffff'):
        super().__init__()

        layout = QHBoxLayout()

        groupBox = QGroupBox()
        groupBox.setFixedSize(5, 20)
        groupBox.setStyleSheet('QGroupBox {background-color: ' + color + '; border-radius: 4px;}')
        layout.addWidget(groupBox,  QtCore.Qt.AlignRight)

        label = Label(text)
        label.setColor('#ffffff')
        layout.addWidget(label, QtCore.Qt.AlignLeft)

        label = Label('0')
        label.setColor('#ffffff')
        layout.addWidget(label)

        self.setLayout(layout)


