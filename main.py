from PyQt5.QtWidgets import (QMainWindow, QWidget, QGridLayout,
                             QApplication, QVBoxLayout, QMenuBar,
                             QAction, QMenu, QFileDialog, QHBoxLayout)
from PyQt5.QtGui import QImage, QPixmap, QIcon, QFont
from GroupBox import GroupBox
from Label import Label
from HBoxLayoutObject import HBoxLayoutObject
from HBoxLayoutStatic import HBoxLayoutStatic


class MainWindow(QMainWindow):
    """
    Класс главного окна.

    """

    def __init__(self):
        super().__init__()
        self.resize(1000, 470)

        self.PATH_TO_VIDEO = None

        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)
        # Creating actions using the second constructor
        self.openAction = QAction("&Открыть...", self)
        self.openAction.triggered.connect(self.openFile)
        self.saveAction = QAction("&Сохранить", self)
        fileMenu = QMenu("&Файл", self)
        fileMenu.setFont(QFont("Roboto", 10))
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)

        mainLayout = QGridLayout()

        videoPlayer = GroupBox()
        videoPlayer.setColor('black')
        mainLayout.addWidget(videoPlayer, 1, 0, 52, 10)

        label = Label('Обьекты отслеживания')
        mainLayout.addWidget(label, 0, 10)

        objectsGroupBox = GroupBox()

        layoutObjectGroupBox = QVBoxLayout(objectsGroupBox)

        layoutObjectGroupBox.addWidget(HBoxLayoutObject("Пешеходы", "#f4c8bd"))
        layoutObjectGroupBox.addSpacing(-15)

        layoutObjectGroupBox.addWidget(HBoxLayoutObject("Велосипеды", "#a0bfdc"))
        layoutObjectGroupBox.addSpacing(-15)

        layoutObjectGroupBox.addWidget(HBoxLayoutObject("Легковые автомобили", "#a9d193"))
        layoutObjectGroupBox.addSpacing(-15)

        layoutObjectGroupBox.addWidget(HBoxLayoutObject("Мотоциклы", "#b599c1"))
        layoutObjectGroupBox.addSpacing(-15)

        layoutObjectGroupBox.addWidget(HBoxLayoutObject("Автобусы", "#f9eeae"))
        layoutObjectGroupBox.addSpacing(-15)

        layoutObjectGroupBox.addWidget(HBoxLayoutObject("Грузовые автомобили", "#f5be6b"))

        mainLayout.addWidget(objectsGroupBox, 1, 10, 25, 2)

        label = Label('Статистика')
        mainLayout.addWidget(label, 28, 10)
        staticGroupBox = GroupBox()

        layoutStaticGroupBox = QVBoxLayout(staticGroupBox)

        layout = QHBoxLayout()
        label = Label('Обьект отслеживания')
        label.setColor('#ffffff')
        layout.addWidget(label)
        layout.addSpacing(10)

        label = Label('На кадре')
        label.setColor('#ffffff')
        layout.addWidget(label)

        widget = QWidget()
        widget.setLayout(layout)
        layoutStaticGroupBox.addWidget(widget)
        layoutStaticGroupBox.addSpacing(-15)

        layoutStaticGroupBox.addWidget(HBoxLayoutStatic("Пешеходы", "#f4c8bd"))
        layoutStaticGroupBox.addSpacing(-15)

        layoutStaticGroupBox.addWidget(HBoxLayoutStatic("Велосипеды", "#a0bfdc"))
        layoutStaticGroupBox.addSpacing(-15)

        layoutStaticGroupBox.addWidget(HBoxLayoutStatic("Легковые автомобили", "#a9d193"))
        layoutStaticGroupBox.addSpacing(-15)

        layoutStaticGroupBox.addWidget(HBoxLayoutStatic("Мотоциклы", "#b599c1"))
        layoutStaticGroupBox.addSpacing(-15)

        layoutStaticGroupBox.addWidget(HBoxLayoutStatic("Автобусы", "#f9eeae"))
        layoutStaticGroupBox.addSpacing(-15)

        layoutStaticGroupBox.addWidget(HBoxLayoutStatic("Грузовые автомобили", "#f5be6b"))

        mainLayout.addWidget(staticGroupBox, 29, 10, 30, 2)

        mainLayout.addWidget(GroupBox(), 53, 0, 6, 10)

        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

    def openFile(self):
        """

        :return:
        """
        try:
            self.PATH_TO_VIDEO = QFileDialog.getOpenFileName(self, 'Open file')[0]
        except:
            pass


if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()

    app.exec()
