import sys
import vlc
from PyQt5 import QtCore
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSize

from algorythm import RollingGame
from const import GIFS, HEROS
from Frames.MainFrame import Ui_MainWindow
from Frames.PersonFrame import Ui_PersonWindow
from Frames.PlayFrame import Ui_PlayWindow


class PlayWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(PlayWindow, self).__init__()
        self.ui = Ui_PlayWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        p = vlc.MediaPlayer("/Users/Anastasia/Downloads/Музыка/Musica Paradiso-Harry Potter Main Theme-kissvk.com.mp3")
        p.play()

        self.ui.pushButton.clicked.connect(self.play_game)

    def play_game(self):
        self.w = MainWindow()
        self.w.show()


class PersonWindow(QtWidgets.QMainWindow):
    def __init__(self, person):
        super(PersonWindow, self).__init__()
        self.ui = Ui_PersonWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.ui.label.setText(f"{person}")
        if person in ["Granny Kowalski", "Anyone except Dudley Dursley"]:
            pic = QtGui.QPixmap(HEROS[person])
            self.ui.label_1.setPixmap(pic)
            self.ui.label_1.setAlignment(QtCore.Qt.AlignCenter)
        else:
            mov = QtGui.QMovie(GIFS[person])
            mov.setScaledSize(QSize(800, 300))
            self.ui.label_1.setMovie(mov)
            self.ui.label_1.setAlignment(QtCore.Qt.AlignCenter)
            mov.start()

        self.ui.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.close()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.game = RollingGame()
        self.rules_list = self.game.rules_list
        self.answers = []
        self.user_answer = ""
        self.answers_list = []
        self.then_list = []
        self.play()

        self.ui.pushButton.clicked.connect(self.some_function)

    def button_clicked(self):
        question, self.answers = self.game.find_rule(self.game.rules, self.game.attributes, self.rules_list)
        self.ui.label_1.setText(question)
        self.ui.combo.clear()
        self.ui.combo.addItems(self.answers)

    def play(self):
        self.ui.label_1.setText(self.game.first_question)
        self.ui.combo.clear()
        self.ui.combo.addItems(self.game.first_answers)

    def some_function(self):
        question = self.ui.label_1.text()
        if '\n' in question:
            question = question.replace('\n', '')
        user_answer = self.ui.combo.currentText()
        f = False
        for vocabulary in self.game.rules:
            inside_voc = vocabulary['if']
            for i in range(len(inside_voc)):
                inside_length = len(inside_voc)
                if inside_voc[i]['attribute'] == question and inside_voc[i]['value'] == user_answer:
                    if inside_voc[i] == inside_voc[-1]:
                        self.answers_list.append(user_answer)
                        error = False
                        for i in range(inside_length):
                            inside_ans = inside_voc[i]['value']
                            if inside_ans != self.answers_list[i]:
                                error = True
                                break
                        if error is True:
                            continue

                        then = (vocabulary['then']['attribute'], vocabulary['then']['value'])
                        self.then_list.clear()
                        self.then_list.append(then)
                        self.rules_list.append(then[0])

                        if then[0] == 'Person':
                            print('Person found. You are', then[1])
                            self.win = PersonWindow(then[1])
                            self.win.show()
                            self.close()
                        else:
                            text_len = len(then[0])
                            text = then[0]
                            if text_len > 41:
                                text = text[:41] + '\n' + text[41:]
                            self.ui.label_1.setText(text)
                            self.ui.combo.clear()
                            self.ui.combo.addItem(then[1])

                        self.answers_list.clear()
                        f = True
                        break
                    else:
                        self.answers_list.append(user_answer)
                        print(inside_voc[i + 1]['attribute'])
                        self.rules_list.append(inside_voc[i + 1]['attribute'])
                        question, self.answers = self.game.find_rule(self.game.rules, self.game.attributes, self.rules_list)
                        text_len = len(question)
                        text = question
                        if text_len > 41:
                            question = text[:41] + '\n' + text[41:]
                        self.ui.label_1.setText(question)
                        self.ui.combo.clear()
                        self.ui.combo.addItems(self.answers)
                        f = True
                        break
            if f is True:
                f = False
                break


app = QtWidgets.QApplication([])
application = PlayWindow()
application.show()

sys.exit(app.exec())
