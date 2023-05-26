from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont


class PushButton(QPushButton):
    """
    Класс для настройки QPushButton

    flag: индикатор активации кнопки
    __color: цвет
    __conn: подключение к обьекты статистики

    """

    __color = ''
    __conn = None

    def __init__(self, text='', color='', parent=None) -> None:
        super().__init__(text, parent)
        self.__color = color
        self.flag = True
        self.setStyleSheet("QPushButton {background-color: #ffffff;}"
                           "QPushButton::hover {background-color : " + self.__color + ";}")

        self.setFont(QFont("Roboto", 12))
        self.setMinimumHeight(35)
        self.setMinimumWidth(250)

        self.clicked.connect(self.setStyleHover)

    def setConnect(self, conn) -> None:
        """
        Сеттер для подключения к обьекту статистики

        :param conn: обьект статистики
        """
        self.__conn = conn

    def setStyleHover(self) -> None:
        """
        Сеттер для установления цвета внутри QPushButton при нажатии на кнопку

        """
        if self.flag:
            self.__conn.show()  # Вывод обьекта статистики
            self.flag = False
            self.setStyleSheet("QPushButton {background-color : " + self.__color + ";}"
                               "QPushButton::hover {background-color : #ffffff;}")
        else:
            self.__conn.hide()  # Скрытие обьекта статистики
            self.flag = True
            self.setStyleSheet("QPushButton {background-color: #ffffff;}"
                               "QPushButton::hover {background-color : " + self.__color + ";}")