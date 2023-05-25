from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtGui import QFont


class GroupBox(QGroupBox):
    """
    Класс для настройки QGroupBox

    """

    def __init__(self, text='', parent=None):
        """
        :param text: текст по умолчанию пуст
        :param parent: ---
        """
        super().__init__(text, parent)

        # Цвет по умолчанию
        self.color = '#3a567f'
        self.setStyleSheet('QGroupBox {background-color: ' + self.color + '; border-radius: 4px;}')
        # Шрифт по умолчанию
        self.setFont(QFont("Roboto", 9))

    def setColor(self, color):
        """
        Функция нужна, для того чтобы задать цвет
        :param color: цвет
        """
        self.color = color
        self.setStyleSheet('QGroupBox {background-color: ' + self.color + '; border-radius: 4px;}')
