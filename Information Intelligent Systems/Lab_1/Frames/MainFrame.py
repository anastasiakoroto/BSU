from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 700)

        stylesheet = """
            MainWindow {
                background-image: url("/Users/Anastasia/Desktop/BSU_FAMCS/7_semester/Information Intelligent Systems/Lab1/background/ho-5.jpg"); 
                background-repeat: no-repeat; 
                background-position: center;
            }
        """
        MainWindow.setStyleSheet(stylesheet)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 791, 361))

        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label)

        self.label00 = QtWidgets.QLabel(self.centralwidget)
        self.label00.setObjectName("label00")
        self.verticalLayout.addWidget(self.label00)

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setObjectName("label_1")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_1)

        self.label000 = QtWidgets.QLabel(self.centralwidget)
        self.label000.setObjectName("label000")
        self.verticalLayout.addWidget(self.label000)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_2)

        self.combo = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.combo.setObjectName("comboBox")
        self.combo.setIconSize(QtCore.QSize(100, 30))
        self.verticalLayout.addWidget(self.combo)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(260, 475, 300, 100))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.pushButton.setText(_translate("MainWindow", "GIVE ANSWER"))
        self.pushButton.setFont(QtGui.QFont('Impact', 40))
        self.pushButton.setStyleSheet(  # #ECFFF5  border - #E2F1E9  back = D3D3D3
            """QPushButton {background-color: #CBC2AD; border-style: outset; border-width: 1px; border-radius: 5px;
            border-color: gray; color: #405B42} 
            QPushButton:pressed {background-color: #B2AA95; color: #354736}"""
        )

        self.label00.setText(_translate("MainWindow", " "))
        self.label00.setFont(QtGui.QFont("Impact", 40))

        self.label000.setText(_translate("MainWindow", " "))
        self.label000.setFont(QtGui.QFont("Impact", 48))

        self.label.setText(_translate("MainWindow", "ANSWER THE QUESTION BELOW, PLEASE: "))
        self.label.setFont(QtGui.QFont("Impact", 40))
        self.label.setStyleSheet("QLabel { color: #F3F2E1 }")
        self.label_1.setText(_translate("MainWindow", "QUESTION"))
        self.label_1.setFont(QtGui.QFont("Impact", 40))
        self.label_1.setStyleSheet('color: #FAF9ED')

        self.label_2.setText(
            _translate("MainWindow", "CHOOSE ONE OF THE OPTIONS:"))
        self.label_2.setFont(QtGui.QFont("Verdana", 16))
        self.label_2.setStyleSheet('color: #E2E1DC')

        self.combo.addItems(['Test', 'Test2', 'Test3'])
        self.combo.setFont(QtGui.QFont("Verdana", 20))
        self.combo.setStyleSheet('color: #43604F')
