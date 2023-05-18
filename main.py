from PyQt5.QtWidgets import (QMainWindow, QWidget, QGridLayout, QSlider,
                             QApplication, QVBoxLayout, QMenuBar,
                             QAction, QMenu, QFileDialog, QHBoxLayout, QLabel, QPushButton)
from PyQt5.QtGui import QImage, QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt
from GroupBox import GroupBox
from Label import Label
from HBoxLayoutStatic import HBoxLayoutStatic
from PushButton import PushButton


class MainWindow(QMainWindow):
    """
    Класс главного окна.

    """

    def __init__(self):
        super().__init__()
        self.resize(1000, 0)

        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)
        menuBar.setFont(QFont("Roboto", 10))
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
        mainLayout.addWidget(videoPlayer, 1, 0, 53, 10)

        label = Label('Обьекты отслеживания')
        mainLayout.addWidget(label, 0, 10)

        objectsGroupBox = GroupBox()

        layoutObjectGroupBox = QVBoxLayout(objectsGroupBox)

        btn = PushButton("Пешеходы", "#f4c8bd")
        layoutObjectGroupBox.addWidget(btn)

        btn = PushButton("Велосипеды", "#a0bfdc")
        layoutObjectGroupBox.addWidget(btn)

        btn = PushButton("Легковые автомобили", "#a9d193")
        layoutObjectGroupBox.addWidget(btn)

        btn = PushButton("Мотоциклы", "#b599c1")
        layoutObjectGroupBox.addWidget(btn)

        btn = PushButton("Автобусы", "#f9eeae")
        layoutObjectGroupBox.addWidget(btn)

        btn = PushButton("Грузовые автомобили", "#f5be6b")
        layoutObjectGroupBox.addWidget(btn)

        mainLayout.addWidget(objectsGroupBox, 1, 10, 25, 2)

        label = Label('Статистика')
        mainLayout.addWidget(label, 28, 10)
        staticGroupBox = GroupBox()

        layoutStaticGroupBox = QVBoxLayout(staticGroupBox)

        layoutStaticGroupBox.addWidget(HBoxLayoutStatic("Пешеходы", "#f4c8bd"))

        layoutStaticGroupBox.addWidget(HBoxLayoutStatic("Велосипеды", "#a0bfdc"))

        layoutStaticGroupBox.addWidget(HBoxLayoutStatic("Легковые автомобили", "#a9d193"))

        layoutStaticGroupBox.addWidget(HBoxLayoutStatic("Мотоциклы", "#b599c1"))

        layoutStaticGroupBox.addWidget(HBoxLayoutStatic("Автобусы", "#f9eeae"))

        layoutStaticGroupBox.addWidget(HBoxLayoutStatic("Грузовые автомобили", "#f5be6b"))

        mainLayout.addWidget(staticGroupBox, 29, 10, 30, 2)

        groupBox = GroupBox()
        layoutGroupBox = QHBoxLayout(groupBox)

        self.btn_start = QPushButton()
        # self.btn_start.clicked.connect(self.playVideo)
        self.btn_start.setStyleSheet("border-image : url(icon/icons8-воспроизведение-50.png);")
        self.btn_start.setFixedSize(30, 30)
        layoutGroupBox.addWidget(self.btn_start)

        self.time_start = QLabel("00:00")
        self.time_start.setFont(QFont("Roboto", 12))
        self.time_start.setStyleSheet('QLabel {background-color: #3a567f; color: #ffffff;}')
        layoutGroupBox.addWidget(self.time_start)

        self.slider = QSlider(Qt.Horizontal)
        layoutGroupBox.addWidget(self.slider)

        self.time_stop = QLabel("00:00")
        self.time_stop.setFont(QFont("Roboto", 12))
        self.time_stop.setStyleSheet('QLabel {background-color: #3a567f; color: #ffffff;}')
        layoutGroupBox.addWidget(self.time_stop)

        mainLayout.addWidget(groupBox, 54, 0, 5, 10)

        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

    def setImage(self, image):
        self.label_video.setPixmap(QPixmap.fromImage(image))

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
