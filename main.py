import csv

from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow
import sys

from neural.animal import Animal
from neural.popular import Popular
from ui.MainWindow import Ui_MainWindow


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sendBtn.clicked.connect(self.countSlideNumber)
        self.ui.sendBtn.clicked.connect(self.countScore)
        self.ui.rejectionBtn.clicked.connect(self.countSlideNumber)
        self.ui.cardImg.setPixmap(QPixmap('cards/1.jpg'))

        self.slideNumber = int(0)
        self.p, self.a, self.f, self.m, self.w, self.s, self.d, self.c = 0, 0, 0, 0, 0, 0, 0, 0
        self.numberOfReplies = int(0)
        self.elements_to_hide = [self.ui.carlLabel, self.ui.whatLbl, self.ui.whatInput, self.ui.formLbl, self.ui.formYesRadioBtn, self.ui.formNoRadioBtn,
                            self.ui.actionLbl, self.ui.actionYesRadioBtn, self.ui.actionNoRadioBtn, self.ui.partLbl, self.ui.allPartRadioBtn, self.ui.partPartRadioBtn,
                            self.ui.partSeparateRadioBtn, self.ui.partBackRadioBtn, self.ui.partOtherRadioBtn, self.ui.signLbl, self.ui.signFormColorRadioBtn,
                            self.ui.signColorFormRadioBtn, self.ui.signColoRadioBtn, self.ui.rejectionBtn, self.ui.sendBtn]

    # Загрузка изображения по порядковому номеру
    def setImg(self, numCard):
        pixmap = QPixmap(('cards/{numCard}.jpg').format(numCard=numCard))
        self.ui.cardImg.setPixmap(pixmap)

    # Подсчёт ответа по категории в процентах
    def countScoreInPercent(self, param):
        return param / self.numberOfReplies * 100

    # Подсчёт количества ответов по животным
    def countAnimal(self, score):
        if score == 1:
            self.a += 1
        return self.a

    # Подсчёт количества популярных ответов
    def countPopular(self, category):
        if (category != "другое"):
            match self.slideNumber:
                case 0:
                    if (category == "летучая мышь" or "бабочка" or "птица" or "человек"):
                        self.p += 1
                case 1:
                    if (category == "медведь" or "слон" or "собака" or "человек"):
                        self.p += 1
                case 2:
                    if (category == "человек"):
                        self.p += 1
                case 3:
                    if (category == "летучая мышь" or "бабочка"):
                        self.p += 1
                case 4:
                    if (category == "летучая мышь" or "бабочка" or "птица"):
                        self.p += 1
                case 5:
                    if (category == "черепаха"):
                        self.p += 1
                case 6:
                    if (category == "облако"):
                        self.p += 1
                case 7:
                    if (category == "собака" or "ящерица" or "тигр"):
                        self.p += 1
                case 8:
                    if (category == "голова человека"):
                        self.p += 1
                case 9:
                    if (category == "краб" or "осьминог" or "паук" or "собака" or "кролик" or "заяц" or "лев"):
                        self.p += 1
        return self.p

    # Соответствие ответа критериям, постановка преддиагноза
    def chooseDiagnosis(self):
        scoreP = self.countScoreInPercent(self.p)
        scoreA = self.countScoreInPercent(self.a)
        scoreF = self.countScoreInPercent(self.f)
        scoreM = self.countScoreInPercent(self.m)
        scoreW = self.countScoreInPercent(self.w)
        scoreS = self.countScoreInPercent(self.s)
        scoreD = self.countScoreInPercent(self.d)
        scoreC = self.countScoreInPercent(self.c)

        if (scoreP>90 and 30>scoreA>35 and 70>scoreF>80 and scoreM<10 and 65<scoreW<70 and 14<scoreC<18):
            self.diagnosis = "Здоровый тестируемый"
        elif (18>scoreP>22 and 58>scoreA>62 and scoreF<50 and 5>scoreF>9 and 25>scoreW>29 and 4>scoreS>7 and 56>scoreD>60 and 5>scoreC>9):
            self.diagnosis = "Больные с алкогольным делирием"
        elif (65>scoreF>69 and 8>scoreM>12 and 40>scoreW>44 and 5>scoreD>9 and 14>scoreC>18):
            self.diagnosis = "Больные с остбредовыми формами шизофрении"
        elif (27>scoreP>31 and 48>scoreA>52 and 68>scoreF>72 and 8>scoreM>12 and 26>scoreW>30 and 1>scoreD>5 and 3>scoreC>7):
            self.diagnosis = "Атеросклероз"
        elif (scoreP>25 and scoreF>70 and scoreM>10 and scoreC<90):
            self.diagnosis = "Органические поражения головного мозга"
        else:
            self.diagnosis = "Ваши показатели не подходят к категориям, которые тестирует данное приложение"
        # Сохранение результата в базу данных
        with open('result.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.ui.nameInput.toPlainText(), self.diagnosis])
        return "Предварительный диагноз: "+self.diagnosis

    @Slot()
    def countScore(self):
        self.numberOfReplies += 1
        what_result = self.ui.whatInput.toPlainText()
        self.p = self.countPopular(Popular.isPopular(what_result))
        self.a = self.countAnimal(Animal.isAnimal(what_result))

        if self.ui.formYesRadioBtn.isChecked(): #f (ответы с чёткой формой)
            self.f += 1
        if self.ui.actionYesRadioBtn.isChecked():   #m (ответы по движению)
            self.m += 1
        if self.ui.allPartRadioBtn.isChecked(): #w (целостные ответы)
            self.w += 1
        if self.ui.partBackRadioBtn.isChecked(): #s (ответы на белый фон)
            self.s += 1
        if self.ui.partSeparateRadioBtn.isChecked(): #d (ответы на мелкие детали)
            self.d += 1
        if self.ui.signColorFormRadioBtn.isChecked() or self.ui.signColoRadioBtn.isChecked(): #c (цветоформовые ответы и первичные по цвету)
            self.c += 1


    @Slot()
    def countSlideNumber(self):
        self.slideNumber += 1
        match self.slideNumber:
            case 0:
                self.setImg(1)
            case 1:
                self.setImg(2)
            case 2:
                self.setImg(3)
            case 3:
                self.setImg(4)
            case 4:
                self.setImg(5)
            case 5:
                self.setImg(6)
            case 6:
                self.setImg(7)
            case 7:
                self.setImg(8)
            case 8:
                self.setImg(9)
            case 9:
                self.setImg(10)
            case _:
                self.ui.cardImg.setText(self.chooseDiagnosis())
                for i in self.elements_to_hide:
                    i.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()

    sys.exit(app.exec())
