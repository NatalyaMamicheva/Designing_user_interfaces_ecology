import project2
import project3
import project4
from content.gl import *
import sys
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QLineEdit, QLabel, QPushButton, QApplication, QMainWindow, QAction)
from PyQt5.QtCore import QSize

class Window5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Глава 2. Потребление природных ресурсов")
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
        self.label_1.move(200, -30)
        self.label_1.setText(second2)
        font.setFamily('CeraPro-Bold')
        font.setPointSize(15)
        self.label_1.setFixedSize(1800, 1000)
        self.label_1.setStyleSheet("color: green;")
        self.label_1.setFont(font)

        self.label_3 = QLabel("", self)
        self.label_3.move(500, 730)
        self.label_3.setText(second3)
        font.setFamily('CeraPro-Bold')
        font.setPointSize(15)
        self.label_3.setFixedSize(1800, 200)
        self.label_3.setStyleSheet("color: green;")
        self.label_3.setFont(font)

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

        but_form2g = QPushButton(self)
        but_form2g.setIcon(QIcon('content/2gl.png'))
        but_form2g.setIconSize(QSize(3000, 2000))
        but_form2g.setFixedSize(220, 100)
        but_form2g.move(150, 800)

        buttonw2 = QPushButton("Далее", self)
        buttonw2.move(1720, 900)
        buttonw2.setFixedSize(90, 70)
        buttonw2.setStyleSheet("background-color : green; color: white; font: bold; border: 3px solid lightgreen;")
        font = QtGui.QFont()
        font.setFamily('CeraPro-Bold')
        font.setPointSize(12)
        buttonw2.setFont(font)

        buttonw3 = QPushButton("Назад", self)
        buttonw3.move(1630, 900)
        buttonw3.setFixedSize(90, 70)
        buttonw3.setStyleSheet("background-color : green; color: white; font: bold; border: 3px solid lightgreen;")
        font = QtGui.QFont()
        font.setFamily('CeraPro-Bold')
        font.setPointSize(12)
        buttonw3.setFont(font)

        button.clicked.connect(self.window1)
        buttonw2.clicked.connect(self.window2)
        buttonw3.clicked.connect(self.window4)

        self.show()

    def window1(self):
        self.w = MenuGlav()
        self.w.showMaximized()
        self.hide()

    def window2(self):
        self.w2 = Window2()
        self.w2.showMaximized()
        self.hide()

    def window4(self):
        self.w4 = Window4()
        self.w4.showMaximized()
        self.hide()


class Window4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Глава 2. Потребление природных ресурсов")
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
        self.label_1.move(200, 100)
        self.label_1.setText(second)
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
        self.label_1.move(500, 190)
        # changing the text of label
        self.label_1.setText("Глава 2. Потребление природных ресурсов")
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
        buttonw4.clicked.connect(self.window5)

        self.show()

    def window1(self):
        self.w = MenuGlav()
        self.w.showMaximized()
        self.hide()

    def window5(self):
        self.w5 = Window5()
        self.w5.showMaximized()
        self.hide()


class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Глава 2. Потребление природных ресурсов')
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
        self.label_4.move(1, 750)
        self.label_4.setText("Решение: ")
        font.setFamily('CeraPro-Bold')
        font.setPointSize(20)
        self.label_4.setFixedSize(500, 70)
        self.label_4.setStyleSheet("color: green; font: bold")
        self.label_4.setFont(font)

        self.label_5 = QLabel("", self)
        self.label_5.move(1, 830)
        self.label_5.setText("Рассчитаем формулу природопользования (α + β) * N <(или >) P"
                             " и выясним больше или меньше темп возобновления "
                             "ресурсов P в сравнении с изъятием ресурсов (α + β) * N")
        font.setFamily('CeraPro-Bold')
        font.setPointSize(12)
        self.label_5.setFixedSize(2600, 70)
        self.label_5.setStyleSheet("color: green; font: bold")
        self.label_5.setFont(font)

        button.clicked.connect(self.window1)

        self.text1 = QLineEdit(self)
        self.text1.setPlaceholderText("Введите α")
        self.text2 = QLineEdit(self)
        self.text2.setPlaceholderText("Введите β")
        self.text3 = QLineEdit(self)
        self.text3.setPlaceholderText("Введите N")
        self.text4 = QLineEdit(self)
        self.text4.setPlaceholderText("Введите P")

        self.setGeometry(300, 200, 600, 450)

        self.text1.setGeometry(750, 250, 300, 30)
        self.text2.setGeometry(750, 350, 300, 30)
        self.text3.setGeometry(750, 450, 300, 30)
        self.text4.setGeometry(750, 550, 300, 30)

        button_count = QPushButton("Рассчитать", self)
        button_count.move(800, 650)
        button_count.setFixedSize(200, 80)
        button_count.setStyleSheet("background-color : green; color: white; font: bold; border: 3px solid lightgreen;")
        font = QtGui.QFont()
        font.setFamily('CeraPro-Bold')
        font.setPointSize(14)
        button_count.setFont(font)
        button_count.clicked.connect(self.checkstatus)

        buttonw4 = QPushButton("Назад", self)
        buttonw4.move(1720, 900)
        buttonw4.setFixedSize(90, 70)
        buttonw4.setStyleSheet("background-color : green; color: white; font: bold; border: 3px solid lightgreen;")
        font = QtGui.QFont()
        font.setFamily('CeraPro-Bold')
        font.setPointSize(12)
        buttonw4.setFont(font)
        buttonw4.clicked.connect(self.window5)

        self.label_4 = QLabel("", self)
        self.label_4.move(1, 900)
        self.label_4.setText("Ответ: ")
        font.setFamily('CeraPro-Bold')
        font.setPointSize(20)
        self.label_4.setFixedSize(500, 70)
        self.label_4.setStyleSheet("color: green; font: bold")
        self.label_4.setFont(font)

        self.label_answer = QLabel("(α + β) * N", self)
        self.label_answer.move(150, 903)
        font.setFamily('CeraPro-Bold')
        font.setPointSize(10)
        self.label_answer.setFixedSize(500, 70)
        self.label_answer.setStyleSheet("color: green; font: bold")
        self.label_answer.setFont(font)

        self.label3_answer = QLabel("< или (>)", self)
        self.label3_answer.move(250, 903)
        font.setFamily('CeraPro-Bold')
        font.setPointSize(10)
        self.label3_answer.setFixedSize(500, 70)
        self.label3_answer.setStyleSheet("color: green; font: bold")
        self.label3_answer.setFont(font)

        self.label4_answer = QLabel("P", self)
        self.label4_answer.move(340, 903)
        font.setFamily('CeraPro-Bold')
        font.setPointSize(10)
        self.label4_answer.setFixedSize(500, 70)
        self.label4_answer.setStyleSheet("color: green; font: bold")
        self.label4_answer.setFont(font)

        self.label6_answer = QLabel("", self)
        self.label6_answer.move(500, 903)
        font.setFamily('CeraPro-Bold')
        font.setPointSize(10)
        self.label6_answer.setFixedSize(900, 70)
        self.label6_answer.setStyleSheet("color: green; font: bold")
        self.label6_answer.setFont(font)

    def checkstatus(self):
        if self.text1.text() == "":
            print("")
            self.text1.setFocus()
        if self.text2.text() == "":
            print("")
            self.text2.setFocus()
        if self.text3.text() == "":
            print("")
            self.text3.setFocus()
        if self.text4.text() == "":
            print("")
            self.text4.setFocus()
        else:
            try:
                self.label_answer.setText(str((float(self.text1.text()) + float(self.text2.text())) *
                                              float(self.text3.text())))
                if (((float(self.text1.text()) + float(self.text2.text())) *
                     float(self.text3.text()))) > (((float(self.text4.text())))):
                    self.label3_answer.setText('>')
                    self.label6_answer.setText('| Значит изъятие ресурсов больше темпа их возобновления')
                else:
                    self.label3_answer.setText('<')
                    self.label6_answer.setText('| Значит изъятие ресурсов меньше темпа их возобновления')
                self.label4_answer.setText(str((float(self.text4.text()))))
            except ValueError:
                self.label6_answer.setText("Введите корректные данные!")



    def window1(self):
        self.w = MenuGlav()
        self.w.showMaximized()
        self.hide()

    def window5(self):
        self.w5 = Window5()
        self.w5.showMaximized()
        self.hide()


class Window3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Глава 1. Рациональное природопользование")
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
        self.label_1.move(400, 1)
        self.label_1.setText(first)
        font.setFamily('CeraPro-Bold')
        font.setPointSize(15)
        self.label_1.setFixedSize(1300, 1000)
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
        self.label_1.move(480, 190)
        # changing the text of label
        self.label_1.setText("Глава 1. Рациональное природопользование")
        font.setFamily('CeraPro-Bold')
        font.setPointSize(20)
        self.label_1.setFixedSize(1800, 70)
        self.label_1.setStyleSheet("color: green; font: bold")
        self.label_1.setFont(font)

        sxema = QPushButton(self)
        sxema.setIcon(QIcon('content/sxema.jpg'))
        sxema.setIconSize(QSize(500, 400))
        sxema.setFixedSize(500, 290)
        sxema.move(650, 700)

        button.clicked.connect(self.window1)

        self.show()

    def window1(self):
        self.w = MenuGlav()
        self.w.showMaximized()
        self.hide()


class MenuGlav(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")
        self.initUI()

    def initUI(self):
        exitAction = QAction('Если хотите закрыть программу нажмите сюда', self)
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Exit')
        fileMenu.addAction(exitAction)

        button = QPushButton("На главную", self)
        button.move(1, 30)
        button.setFixedSize(200, 80)
        button.setStyleSheet("background-color : green; color: white; font: bold; border: 3px solid lightgreen;")
        font = QtGui.QFont()
        font.setFamily('CeraPro-Bold')
        font.setPointSize(14)
        button.setFont(font)
        button.clicked.connect(self.titul)

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

        but = QPushButton(self)
        but.setIcon(QIcon('content/planet.jpg'))
        but.setIconSize(QSize(80, 80))
        but.setFixedSize(80, 80)
        but.move(1700, 30)

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Рациональное природопользование')
        self.setWindowIcon(QIcon('content/planet.jpg'))

        button1 = QPushButton("Глава 1. Рациональное природопользование", self)
        button1.move(600, 400)
        button1.hide()
        self.button1 = button1
        button1.setFixedSize(600, 80)
        font.setFamily('CeraPro-Bold')  # сам шрифт
        font.setPointSize(14)  # размер шрифта
        button1.setFont(font)
        button1.setStyleSheet("background-color : green; color: white; font: bold; border: 3px solid lightgreen;")

        button2 = QPushButton("Глава 2. Потребление природных ресурсов", self)
        button2.move(600, 500)
        button2.hide()
        self.button2 = button2
        button2.setFixedSize(600, 80)
        font.setFamily('CeraPro-Bold')  # сам шрифт
        font.setPointSize(14)  # размер шрифта
        button2.setFont(font)
        button2.setStyleSheet("background-color : green; color: white; font: bold; border: 3px solid lightgreen;")

        button3 = QPushButton("Глава 3. Углекислый газ в атмосфере Земли", self)
        button3.move(600, 600)
        button3.hide()
        self.button3 = button3
        button3.setFixedSize(600, 80)
        font.setFamily('CeraPro-Bold')  # сам шрифт
        font.setPointSize(14)  # размер шрифта
        button3.setFont(font)
        button3.setStyleSheet("background-color : green; color: white; font: bold; border: 3px solid lightgreen;")

        button4 = QPushButton("Глава 4. Плотность популяции животного мира", self)
        button4.move(600, 700)
        button4.hide()
        self.button4 = button4
        button4.setFixedSize(600, 80)
        font.setFamily('CeraPro-Bold')  # сам шрифт
        font.setPointSize(14)  # размер шрифта
        button4.setFont(font)
        button4.setStyleSheet("background-color : green; color: white; font: bold; border: 3px solid lightgreen;")

        button5 = QPushButton("Глава 5. Список литературы", self)
        button5.move(600, 800)
        button5.hide()
        self.button5 = button5
        button5.setFixedSize(600, 80)
        font.setFamily('CeraPro-Bold')  # сам шрифт
        font.setPointSize(14)  # размер шрифта
        button5.setFont(font)
        button5.setStyleSheet("background-color : green; color: white; font: bold; border: 3px solid lightgreen;")

        self.label_1 = QLabel("", self)
        # moving position
        self.label_1.move(720, 250)
        # changing the text of label
        self.label_1.setText("Оглавление")
        font.setFamily('CeraPro-Bold')
        font.setPointSize(30)
        self.label_1.setFixedSize(320, 70)
        self.label_1.setStyleSheet("color: green; font: bold")
        self.label_1.setFont(font)

        self.button1.show()
        self.button2.show()
        self.button3.show()
        self.button4.show()
        self.button5.show()
        self.label_1.show()

        self.button1.clicked.connect(self.window3)
        self.button2.clicked.connect(self.window4)
        self.button3.clicked.connect(self.window6)
        self.button4.clicked.connect(self.window9)
        self.button5.clicked.connect(self.window12)


    def window3(self):  # <===
        self.w3 = Window3()
        self.w3.showMaximized()
        self.hide()

    def window4(self):
        self.w4 = Window4()
        self.w4.showMaximized()
        self.hide()

    def window6(self):
        self.w6 = project2.Window6()
        self.w6.showMaximized()
        self.hide()

    def window9(self):
        self.w9 = project3.Window9()
        self.w9.showMaximized()
        self.hide()

    def window12(self):
        self.w12 = project4.Window12()
        self.w12.showMaximized()
        self.hide()

    def titul(self):
        self.ttl = Titul()
        self.ttl.showMaximized()
        self.hide()

class Titul(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Рациональное природопользование")
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


        sxema = QPushButton(self)
        sxema.setIcon(QIcon('content/ppp.png'))
        sxema.setIconSize(QSize(800, 800))
        sxema.setFixedSize(790, 770)
        sxema.move(520, 230)

        button.clicked.connect(self.window1)

        self.show()

    def window1(self):
        self.w = MenuGlav()
        self.w.showMaximized()
        self.hide()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mg = Titul()
    mg.showMaximized()
    sys.exit(app.exec_())


