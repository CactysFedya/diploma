from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QApplication, QVBoxLayout
from GroupBox import GroupBox
from Label import Label
from HBoxLayout import HBoxLayout


class MainWindow(QMainWindow):
    """
    Класс главного окна.

    """

    def __init__(self):
        super().__init__()
        self.resize(871, 470)

        layout = QGridLayout()

        videoPlayer = GroupBox()
        videoPlayer.setColor('black')
        layout.addWidget(videoPlayer, 1, 0, 46, 7)

        label = Label('Обьекты отслеживания')
        layout.addWidget(label, 0, 7)

        objectsGroupBox = GroupBox()

        layoutGroupBox = QVBoxLayout(objectsGroupBox)

        layoutGroupBox.addWidget(HBoxLayout("Пешеходы", "#f4c8bd"))
        layoutGroupBox.addSpacing(-15)

        layoutGroupBox.addWidget(HBoxLayout("Велосипеды", "#a0bfdc"))
        layoutGroupBox.addSpacing(-15)

        layoutGroupBox.addWidget(HBoxLayout("Легковые автомобили", "#a9d193"))
        layoutGroupBox.addSpacing(-15)

        layoutGroupBox.addWidget(HBoxLayout("Мотоциклы", "#b599c1"))
        layoutGroupBox.addSpacing(-15)

        layoutGroupBox.addWidget(HBoxLayout("Автобусы", "#f9eeae"))
        layoutGroupBox.addSpacing(-15)

        layoutGroupBox.addWidget(HBoxLayout("Грузовые автомобили", "#f5be6b"))

        layout.addWidget(objectsGroupBox, 1, 7, 25, 2)

        label = Label('Статистика')
        layout.addWidget(label, 26, 7)
        layout.addWidget(GroupBox(), 27, 7, 26, 2)

        layout.addWidget(GroupBox(), 47, 0, 6, 7)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()

    app.exec()