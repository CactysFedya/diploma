from PyQt5.QtWidgets import QHBoxLayout, QCheckBox, QGroupBox, QWidget
from PyQt5 import QtCore
from Label import Label


class HBoxLayoutObject(QWidget):
    """
    Класс для настройки QHBoxLayout
    """

    def __init__(self, text='', color='#ffffff'):
        super().__init__()

        layout = QHBoxLayout()

        checkBox = QCheckBox('')
        layout.addWidget(checkBox)
        layout.setSpacing(-10)

        label = Label(text)
        label.setColor('#ffffff')
        layout.addWidget(label, QtCore.Qt.AlignLeft)

        groupBox = QGroupBox()
        groupBox.setFixedSize(20, 20)
        groupBox.setStyleSheet('QGroupBox {background-color: ' + color + '; border-radius: 4px;}')
        layout.addWidget(groupBox, QtCore.Qt.AlignRight)

        self.setLayout(layout)


