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
