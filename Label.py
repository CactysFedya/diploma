from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont


class Label(QLabel):
    """
    Класс для настройки Qlabel

    __color: цвет
    __size: размер

    :arg
        text (str): заголовок GroupBox
        parent: родительский класс

    """

    __color = ''
    __size = 0

    def __init__(self, text='', parent=None) -> None:
        super().__init__(text, parent)

        self.setFont(QFont("Roboto", 13))  # Размер шрифта по умолчанию

    def setColor(self, color: str) -> None:
        """
        Сеттер для установления цвета внутри Qlabel
        :param color: цвет
        """
        self.__color = color
        self.setStyleSheet('QLabel {color: ' + self.__color + '; border-radius: 4px;}')

    def setSize(self, size: int) -> None:
        """
        Сеттер для установления размера шрифта внутри Qlabel
        :param size: размер
        """
        self.__size = size
        self.setFont(QFont("Roboto", self.__size))
