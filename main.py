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

        VIDEO_NAME = '4_ons_black_bg_1920x1080.png'
        CWD_PATH = os.getcwd()
        self.PATH_TO_VIDEO = os.path.join(CWD_PATH, VIDEO_NAME)
        self.thread = ThreadOpenCV(self.PATH_TO_VIDEO)
        self.thread.start()
        # self.thread.setTime([self.time_start, self.slider, self.time_stop])
        self.thread.changePixmap.connect(self.setImage)
        self.thread.running = False

        label = Label('Обьекты отслеживания')
        mainLayout.addWidget(label, 0, 10)

        objectsGroupBox = GroupBox()
        objectsGroupBox.setMinimumHeight(250)

        layoutObjectGroupBox = QVBoxLayout(objectsGroupBox)

        staticGroupBox = GroupBox()
        staticGroupBox.setMinimumHeight(250)

        layoutStaticGroupBox = QVBoxLayout(staticGroupBox)

        countPerson = HBoxLayoutStatic("Пешеходы", "#f4c8bd")
        layoutStaticGroupBox.addWidget(countPerson)
        countPerson.hide()

        countBicycle = HBoxLayoutStatic("Велосипеды", "#a0bfdc")
        layoutStaticGroupBox.addWidget(countBicycle)
        countBicycle.hide()

        countCar = HBoxLayoutStatic("Легковые автомобили", "#a9d193")
        layoutStaticGroupBox.addWidget(countCar)
        countCar.hide()

        countMotorbike = HBoxLayoutStatic("Мотоциклы", "#b599c1")
        layoutStaticGroupBox.addWidget(countMotorbike)
        countMotorbike.hide()

        countBus = HBoxLayoutStatic("Автобусы", "#f9eeae")
        layoutStaticGroupBox.addWidget(countBus)
        countBus.hide()

        countTruck = HBoxLayoutStatic("Грузовые автомобили", "#f5be6b")
        layoutStaticGroupBox.addWidget(countTruck)
        countTruck.hide()

        mainLayout.addWidget(staticGroupBox, 29, 10, 30, 2)

        btn = PushButton("Пешеходы", "#f4c8bd", countPerson)
        layoutObjectGroupBox.addWidget(btn)

        btn = PushButton("Велосипеды", "#a0bfdc", countBicycle)
        layoutObjectGroupBox.addWidget(btn)

        btn = PushButton("Легковые автомобили", "#a9d193", countCar)
        layoutObjectGroupBox.addWidget(btn)

        btn = PushButton("Мотоциклы", "#b599c1", countMotorbike)
        layoutObjectGroupBox.addWidget(btn)

        btn = PushButton("Автобусы", "#f9eeae", countBus)
        layoutObjectGroupBox.addWidget(btn)

        btn = PushButton("Грузовые автомобили", "#f5be6b", countTruck)
        layoutObjectGroupBox.addWidget(btn)

        mainLayout.addWidget(objectsGroupBox, 1, 10, 25, 2)

        label = Label('Статистика')
        mainLayout.addWidget(label, 28, 10)

        groupBox = GroupBox()
        layoutGroupBox = QHBoxLayout(groupBox)

        self.btn_start = QPushButton()
        # self.btn_start.clicked.connect(self.playVideo)
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

    def setImage(self, image):
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

        if self.thread.running == False:
            self.thread.running = True
            self.btn_start.setStyleSheet("border-image : url(icon/icons8-пауза-50.png);")
            # self.thread.setCheckState([self.checkbox_person, self.checkbox_bicycle, self.checkbox_car,
            #                         self.checkbox_motorbike, self.checkbox_bus, self.checkbox_truck],
            #                           [self.count_person, self.count_bicycle, self.count_car,
            #                            self.count_motorbike, self.count_bus, self.count_truck]
            #                           )

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
