from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QApplication, QVBoxLayout
from GroupBox import GroupBox
from Label import Label


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
        layout.addWidget(GroupBox(), 1, 7, 24, 2)

        label = Label('Статистика')
        layout.addWidget(label, 26, 7)
        layout.addWidget(GroupBox(), 27, 7, 24, 2)

        layout.addWidget(GroupBox(), 47, 0, 4, 7)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()

    app.exec()