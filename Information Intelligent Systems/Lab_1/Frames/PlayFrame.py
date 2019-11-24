from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize


class Ui_PlayWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("PlayWindow")
        MainWindow.resize(810, 700)

        stylesheet = """
                    PlayWindow {
                        background-image: url("/Users/Anastasia/Desktop/BSU_FAMCS/7_semester/Information Intelligent Systems/Lab1/background/p.jpg"); 
                        background-repeat: no-repeat; 
                        background-position: center;
                    }
                """
        MainWindow.setStyleSheet(stylesheet)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 791, 511))

        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label)

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setObjectName("label_1")
        movie = QtGui.QMovie("/Users/Anastasia/Desktop/BSU_FAMCS/7_semester/Information Intelligent Systems/Lab1/background/main.gif")
        movie.setScaledSize(QSize(640, 320))
        self.label_1.setMovie(movie)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        movie.start()
        self.verticalLayout.addWidget(self.label_1)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(260, 575, 300, 100))

        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("PlayWindow", "PlayWindow"))

        self.pushButton.setText(_translate("PlayWindow", "PLAY"))
        self.pushButton.setFont(QtGui.QFont('Impact', 40))
        self.pushButton.setStyleSheet(
            """QPushButton {background-color: #CBC2AD; border-style: outset; border-width: 1px; border-radius: 5px;
            border-color: gray; color: #405B42}
            QPushButton:pressed {background-color: #B2AA95; color: #354736}"""
        )

        self.label.setText(
            _translate("MainWindow", "HI, DEAR! LETS PLAY THE GAME. I'D LIKE TO PREDICT, \nWHO YOU ARE..."))
        self.label.setFont(QtGui.QFont("Impact", 40))
        self.label.setStyleSheet("QLabel { color: #CBC2AD }")
