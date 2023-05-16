from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont


class Label(QLabel):
    """
    Класс для настройки Qlabel
    """

    def __init__(self, text='', parent=None):
        super().__init__(text, parent)

        # Размер шрифта по умолчанию
        self.setFont(QFont("Roboto", 12))

    def setColor(self, color):
        """
        Функция нужна, для того чтобы задать цвет
        :param color: цвет
        """
        self.color = color
        self.setStyleSheet('QLabel {color: ' + self.color + '; border-radius: 4px;}')

    def setSize(self, size):
        """
        Функция нужна, для того чтобы задать размер шрифта
        :param size: размер
        """
        self.setFont(QFont("Roboto", size))
