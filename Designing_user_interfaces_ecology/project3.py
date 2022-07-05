import project
from content.gl import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QLineEdit, QLabel, QPushButton, QMainWindow, QAction)
from PyQt5.QtCore import QSize


class Window9(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Глава 4. Плотность популяции животного мира")
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
        self.label_1.move(200, 130)
        self.label_1.setText(fourth)
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

        self.label_1 = QLabel("", self)
        # moving position
        self.label_1.move(600, 190)
        # changing the text of label
        self.label_1.setText("Глава 4. Плотность популяции животного мира")
        font.setFamily('CeraPro-Bold')
        font.setPointSize(20)
        self.label_1.setFixedSize(1800, 70)
        self.label_1.setStyleSheet("color: green; font: bold")
        self.label_1.setFont(font)

        buttonw4 = QPushButton("Далее", self)
        buttonw4.move(1720, 900)
        buttonw4.setFixedSize(90, 70)
        buttonw4.setStyleSheet("background-color : green; color: white; font: bold; border: 3px solid lightgreen;")
        font = QtGui.QFont()
        font.setFamily('CeraPro-Bold')
        font.setPointSize(12)
        buttonw4.setFont(font)

        button.clicked.connect(self.window1)
        buttonw4.clicked.connect(self.window10)

        self.show()

    def window1(self):
        self.w = project.MenuGlav()
        self.w.showMaximized()
        self.hide()

    def window10(self):
        self.w10 = Window10()
        self.w10.showMaximized()
        self.hide()


class Window10(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Глава 4. Плотность популяции животного мира")
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
        self.label_1.move(200, -70)
        self.label_1.setText(fourth2)
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

        self.label_3 = QLabel("", self)
        self.label_3.move(200, 800)
        self.label_3.setText(fourth3)
        font.setFamily('CeraPro-Bold')
        font.setPointSize(15)
        self.label_3.setFixedSize(1800, 200)
        self.label_3.setStyleSheet("color: green;")
        self.label_3.setFont(font)

        but_pict = QPushButton(self)
        but_pict.setIcon(QIcon('content/planet.jpg'))
        but_pict.setIconSize(QSize(80, 80))
        but_pict.setFixedSize(80, 80)
        but_pict.move(1700, 30)

        but_pict1 = QPushButton(self)
        but_pict1.setIcon(QIcon('content/animals.PNG'))
        but_pict1.setIconSize(QSize(400, 500))
        but_pict1.setFixedSize(400, 250)
        but_pict1.move(1000, 720)

        but_pict2 = QPushButton(self)
        but_pict2.setIcon(QIcon('content/4gl.PNG'))
        but_pict2.setIconSize(QSize(600, 600))
        but_pict2.setFixedSize(140, 80)
        but_pict2.move(180, 750)

        buttonw4 = QPushButton("Далее", self)
        buttonw4.move(1720, 900)
        buttonw4.setFixedSize(90, 70)
        buttonw4.setStyleSheet("background-color : green; color: white; font: bold; border: 3px solid lightgreen;")
        font = QtGui.QFont()
        font.setFamily('CeraPro-Bold')
        font.setPointSize(12)
        buttonw4.setFont(font)

        buttonw3 = QPushButton("Назад", self)
        buttonw3.move(1630, 900)
        buttonw3.setFixedSize(90, 70)
        buttonw3.setStyleSheet("background-color : green; color: white; font: bold; border: 3px solid lightgreen;")
        font = QtGui.QFont()
        font.setFamily('CeraPro-Bold')
        font.setPointSize(12)
        buttonw3.setFont(font)

        button.clicked.connect(self.window1)
        buttonw4.clicked.connect(self.window11)
        buttonw3.clicked.connect(self.window9)

        self.show()

    def window1(self):
        self.w = project.MenuGlav()
        self.w.showMaximized()
        self.hide()

    def window11(self):
        self.w8 = Window11()
        self.w8.showMaximized()
        self.hide()

    def window9(self):
        self.w9 = Window9()
        self.w9.showMaximized()
        self.hide()

class Window11(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Глава 4. Плотность популяции животного мира')
        self.setWindowIcon(QIcon('content/planet.jpg'))
        self.setGeometry(500, 500, 500, 500)
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

        self.label_1 = QLabel("", self)
        self.label_1.move(350, 150)
        self.label_1.setText("Входные данные  (вещественные числа указывать через точку)")
        font.setFamily('CeraPro-Bold')
        font.setPointSize(20)
        self.label_1.setFixedSize(1800, 70)
        self.label_1.setStyleSheet("color: green; font: bold")
        self.label_1.setFont(font)

        self.label_4 = QLabel("", self)
        self.label_4.move(1, 650)
        self.label_4.setText("Решение: ")
        font.setFamily('CeraPro-Bold')
        font.setPointSize(20)
        self.label_4.setFixedSize(500, 70)
        self.label_4.setStyleSheet("color: green; font: bold")
        self.label_4.setFont(font)

        self.label_5 = QLabel("", self)
        self.label_5.move(1, 730)
        self.label_5.setText("Рассчитаем формулу плотности популяции одного вида животных "
                             "N / S1 = D")
        font.setFamily('CeraPro-Bold')
        font.setPointSize(12)
        self.label_5.setFixedSize(2600, 70)
        self.label_5.setStyleSheet("color: green; font: bold")
        self.label_5.setFont(font)

        button.clicked.connect(self.window1)

        self.text1 = QLineEdit(self)
        self.text1.setPlaceholderText("Введите N")
        self.text2 = QLineEdit(self)
        self.text2.setPlaceholderText("Введите S1")

        self.setGeometry(300, 200, 600, 450)

        self.text1.setGeometry(750, 250, 300, 30)
        self.text2.setGeometry(750, 350, 300, 30)

        button_count = QPushButton("Рассчитать", self)
        button_count.move(800, 500)
        button_count.setFixedSize(200, 80)
        button_count.setStyleSheet("background-color : green; color: white; font: bold; border: 3px solid lightgreen;")
        font = QtGui.QFont()
        font.setFamily('CeraPro-Bold')
        font.setPointSize(14)
        button_count.setFont(font)
        button_count.clicked.connect(self.checkstatus)

        self.label_4 = QLabel("", self)
        self.label_4.move(1, 900)
        self.label_4.setText("Ответ: ")
        font.setFamily('CeraPro-Bold')
        font.setPointSize(20)
        self.label_4.setFixedSize(500, 70)
        self.label_4.setStyleSheet("color: green; font: bold")
        self.label_4.setFont(font)

        self.label_answer = QLabel("N / S1 = ", self)
        self.label_answer.move(150, 903)
        font.setFamily('CeraPro-Bold')
        font.setPointSize(10)
        self.label_answer.setFixedSize(500, 70)
        self.label_answer.setStyleSheet("color: green; font: bold")
        self.label_answer.setFont(font)

        self.label4_answer = QLabel("D", self)
        self.label4_answer.move(250, 903)
        font.setFamily('CeraPro-Bold')
        font.setPointSize(10)
        self.label4_answer.setFixedSize(500, 70)
        self.label4_answer.setStyleSheet("color: green; font: bold")
        self.label4_answer.setFont(font)

        self.label6_answer = QLabel("", self)
        self.label6_answer.move(800, 903)
        font.setFamily('CeraPro-Bold')
        font.setPointSize(10)
        self.label6_answer.setFixedSize(900, 70)
        self.label6_answer.setStyleSheet("color: green; font: bold")
        self.label6_answer.setFont(font)

        buttonw4 = QPushButton("Назад", self)
        buttonw4.move(1720, 900)
        buttonw4.setFixedSize(90, 70)
        buttonw4.setStyleSheet("background-color : green; color: white; font: bold; border: 3px solid lightgreen;")
        font = QtGui.QFont()
        font.setFamily('CeraPro-Bold')
        font.setPointSize(12)
        buttonw4.setFont(font)

        buttonw4.clicked.connect(self.window10)

        self.show()

    def checkstatus(self):
        if self.text1.text() == "":
            print("")
            self.text1.setFocus()
        if self.text2.text() == "":
            print("")
            self.text2.setFocus()
        else:
            try:
                self.label6_answer.setText('| Плотность популяции данного вида животных')
                self.label4_answer.setText(str((float(self.text1.text()) / float(self.text2.text()))))
            except ValueError:
                self.label6_answer.setText("Введите корректные данные!")
            except ZeroDivisionError:
                self.label6_answer.setText("На 0 делить нельзя!")

    def window1(self):
        self.w = project.MenuGlav()
        self.w.showMaximized()
        self.hide()

    def window10(self):
        self.w10 = Window10()
        self.w10.showMaximized()
        self.hide()

