import project
from content.gl import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QLabel, QPushButton, QMainWindow, QAction)
from PyQt5.QtCore import QSize


class Window12(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Глава 5. Список литературы")
        self.setGeometry(500, 500, 500, 500)
        self.setWindowIcon(QIcon('content/planet.jpg'))
        self.setStyleSheet("background-color: white;")

        self.initUI()

    def initUI(self):
        exitAction = QAction('Если хотите закрыть программу нажмите сюда', self)
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Exit')
        fileMenu.addAction(exitAction)

        button = QPushButton("Оглавление", self)
        button.move(1, 30)
        button.setFixedSize(200, 80)
        button.setStyleSheet("background-color : green; color: white; font: bold; border: 3px solid lightgreen;")
        font = QtGui.QFont()
        font.setFamily('CeraPro-Bold')
        font.setPointSize(14)
        button.setFont(font)

        self.label_1 = QLabel("", self)
        self.label_1.move(400, -30)
        self.label_1.setText(book)
        font.setFamily('CeraPro-Bold')
        font.setPointSize(15)
        self.label_1.setFixedSize(1800, 1000)
        self.label_1.setStyleSheet("color: green;")
        self.label_1.setFont(font)

        self.label_2 = QLabel("", self)
        # moving position
        self.label_2.move(400, 30)
        # changing the text of label
        self.label_2.setText("  Рациональное природопользование")
        font.setFamily('CeraPro-Bold')
        font.setPointSize(30)
        self.label_2.setFixedSize(1050, 80)
        self.label_2.setStyleSheet("background-color : green; color: white; font: bold; border: 3px solid lightgreen;")
        self.label_2.setFont(font)

        but_pict = QPushButton(self)
        but_pict.setIcon(QIcon('content/planet.jpg'))
        but_pict.setIconSize(QSize(80, 80))
        but_pict.setFixedSize(80, 80)
        but_pict.move(1700, 30)

        but_pict1 = QPushButton(self)
        but_pict1.setIcon(QIcon('content/ppp.png'))
        but_pict1.setIconSize(QSize(380, 380))
        but_pict1.setFixedSize(380, 380)
        but_pict1.move(730, 625)

        self.label_1 = QLabel("", self)
        # moving position
        self.label_1.move(600, 190)
        # changing the text of label
        self.label_1.setText("Глава 5. Список литературы")
        font.setFamily('CeraPro-Bold')
        font.setPointSize(20)
        self.label_1.setFixedSize(1800, 70)
        self.label_1.setStyleSheet("color: green; font: bold")
        self.label_1.setFont(font)

        button.clicked.connect(self.window1)

        self.show()

    def window1(self):
        self.w = project.MenuGlav()
        self.w.showMaximized()
        self.hide()
