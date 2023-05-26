from PyQt5.QtWidgets import QHBoxLayout, QGroupBox
from PyQt5 import QtCore
from Label import Label


class HBoxLayoutStatic(QGroupBox):
    """
    Класс для настройки QHBoxLayout

    __color: цвет по умолчанию

    :arg
        text (str): заголовок QHBoxLayout
        color (str): цвет QHBoxLayout
    """
    __color = ''

    def __init__(self, text='', color='#ffffff') -> None:
        super().__init__()

        layout = QHBoxLayout(self)

        label = Label(text)
        label.setColor('#000000')
        layout.addWidget(label, QtCore.Qt.AlignLeft)

        countLabel = Label('0')
        countLabel.setColor('#000000')
        layout.addWidget(countLabel)
        self.setColor(color)

    def setColor(self, color: str) -> None:
        """
        Сеттер для установления цвета внутри QHBoxLayout
        :param color: цвет
        """
        if color:
            self.__color = color
            self.setStyleSheet('QGroupBox {background-color: ' + self.__color + '; border-radius: 4px; border: 15px}')
        else:
            raise Exception("Enter a color")



