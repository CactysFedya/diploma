from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtGui import QFont


class GroupBox(QGroupBox):
    """
    Класс для настройки QGroupBox

    __color: цвет по умолчанию

    :arg
        text (str): заголовок GroupBox
        parent: родительский класс

    """

    __color: str = '#3a567f'

    def __init__(self, text='', parent=None):
        super().__init__(text, parent)

        self.setColor(self.__color)
        self.setFont(QFont("Roboto", 9))  # Шрифт по умолчанию

    def setColor(self, color: str) -> None:
        """
        Сеттер для установления цвета внутри QGroupBox
        :param color: цвет
        """
        if color:
            self.__color = color
            self.setStyleSheet('QGroupBox {background-color: ' + self.__color + '; border-radius: 4px;}')
        else:
            raise Exception("Enter a color")
