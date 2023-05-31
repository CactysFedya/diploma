from PyQt5.QtWidgets import (QMainWindow, QWidget, QGridLayout, QSlider,
                             QApplication, QVBoxLayout, QMenuBar,
                             QAction, QMenu, QFileDialog, QHBoxLayout, QLabel, QPushButton)
from PyQt5.QtGui import QImage, QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt
import os
from GroupBox import GroupBox
from Label import Label
from HBoxLayoutStatic import HBoxLayoutStatic
from PushButton import PushButton
from ThreadOpenCV import ThreadOpenCV


class MainWindow(QMainWindow):
    """
    Класс главного окна.

    """

    def __init__(self):
        super().__init__()
        self.resize(1315, 700)

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
        result = QMenu("&Результат", self)
        result.setFont(QFont("Roboto", 10))
        menuBar.addMenu(result)
        _help = QMenu("&Помощь", self)
        _help.setFont(QFont("Roboto", 10))
        menuBar.addMenu(_help)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)

        mainLayout = QGridLayout()

        videoPlayer = GroupBox()
        videoPlayer.setColor('black')
        mainLayout.addWidget(videoPlayer, 1, 0, 53, 10)

        layoutVideoPlayer = QVBoxLayout(videoPlayer)
        layoutVideoPlayer.setAlignment(Qt.AlignCenter)

        self.label_video = QLabel()
        layoutVideoPlayer.addWidget(self.label_video)

        self.PATH_TO_VIDEO = ''

        label = Label('Обьекты отслеживания')
        mainLayout.addWidget(label, 0, 10)

        objectsGroupBox = GroupBox()
        objectsGroupBox.setMinimumHeight(250)

        layoutObjectGroupBox = QVBoxLayout(objectsGroupBox)

        staticGroupBox = GroupBox()
        staticGroupBox.setMinimumHeight(250)

        layoutStaticGroupBox = QVBoxLayout(staticGroupBox)

        self.countPerson = HBoxLayoutStatic("Пешеходы", "#f4c8bd")
        layoutStaticGroupBox.addWidget(self.countPerson)
        self.countPerson.hide()

        self.countBicycle = HBoxLayoutStatic("Велосипеды", "#a0bfdc")
        layoutStaticGroupBox.addWidget(self.countBicycle)
        self.countBicycle.hide()

        self.countCar = HBoxLayoutStatic("Легковые автомобили", "#a9d193")
        layoutStaticGroupBox.addWidget(self.countCar)
        self.countCar.hide()

        self.countMotorbike = HBoxLayoutStatic("Мотоциклы", "#b599c1")
        layoutStaticGroupBox.addWidget(self.countMotorbike)
        self.countMotorbike.hide()

        self.countBus = HBoxLayoutStatic("Автобусы", "#f9eeae")
        layoutStaticGroupBox.addWidget(self.countBus)
        self.countBus.hide()

        self.countTruck = HBoxLayoutStatic("Грузовые автомобили", "#f5be6b")
        layoutStaticGroupBox.addWidget(self.countTruck)
        self.countTruck.hide()

        mainLayout.addWidget(staticGroupBox, 29, 10, 30, 2)

        self.btnPerson = PushButton("Пешеходы", "#f4c8bd")
        self.btnPerson.setConnect(self.countPerson)
        layoutObjectGroupBox.addWidget(self.btnPerson)

        self.btnBicycle = PushButton("Велосипеды", "#a0bfdc")
        self.btnBicycle.setConnect(self.countBicycle)
        layoutObjectGroupBox.addWidget(self.btnBicycle)

        self.btnCar = PushButton("Легковые автомобили", "#a9d193")
        self.btnCar.setConnect(self.countCar)
        layoutObjectGroupBox.addWidget(self.btnCar)

        self.btnMotorbike = PushButton("Мотоциклы", "#b599c1")
        self.btnMotorbike.setConnect(self.countMotorbike)
        layoutObjectGroupBox.addWidget(self.btnMotorbike)

        self.btnBus = PushButton("Автобусы", "#f9eeae")
        self.btnBus.setConnect(self.countBus)
        layoutObjectGroupBox.addWidget(self.btnBus)

        self.btnTruck = PushButton("Грузовые автомобили", "#f5be6b")
        self.btnTruck.setConnect(self.countTruck)
        layoutObjectGroupBox.addWidget(self.btnTruck)

        mainLayout.addWidget(objectsGroupBox, 1, 10, 25, 2)

        label = Label('Статистика')
        mainLayout.addWidget(label, 28, 10)

        groupBox = GroupBox()
        layoutGroupBox = QHBoxLayout(groupBox)

        self.btn_start = QPushButton()
        self.btn_start.setStyleSheet("border-image : url(icon/icons8-воспроизведение-50.png);")
        self.btn_start.setFixedSize(30, 30)
        layoutGroupBox.addWidget(self.btn_start)
        self.btn_start.clicked.connect(self.playVideo)

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

        self.thread = ThreadOpenCV(self.PATH_TO_VIDEO)
        self.thread.setTime([self.time_start, self.slider, self.time_stop])
        self.thread.changePixmap.connect(self.setImage)
        self.thread.running = False

    def setImage(self, image):
        """

        :param image:
        :return:
        """
        self.label_video.setPixmap(QPixmap.fromImage(image))

    def openFile(self):
        """

        :return:
        """
        try:
            self.PATH_TO_VIDEO = QFileDialog.getOpenFileName(self, 'Open file')[0]
            self.thread.read(self.PATH_TO_VIDEO)
        except:
            pass

    def playVideo(self):
        """

        :return:
        """
        if self.thread.running == False:
            self.thread.running = True
            self.btn_start.setStyleSheet("border-image : url(icon/icons8-пауза-50.png);")
            self.thread.setCheckState([self.btnPerson, self.btnBicycle, self.btnCar,
                                       self.btnMotorbike, self.btnBus, self.btnTruck],
                                      [self.countPerson, self.countBicycle, self.countCar,
                                       self.countMotorbike, self.countBus, self.countTruck])

            self.thread.read(self.PATH_TO_VIDEO)
            self.thread.start()
        else:
            self.thread.running = False
            self.btn_start.setStyleSheet("border-image : url(icon/icons8-воспроизведение-50.png);")


if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()

    app.exec()
