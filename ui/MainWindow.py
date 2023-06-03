# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(850, 800))
        MainWindow.setMaximumSize(QSize(850, 800))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"background-color: #F2E6DF;\n"
"font-family: Montserrat Alternates;\n"
"QPushButton { border-radius: 25px;\n"
"background-color: #D9C5C1; }\n"
"QLabel { background: transparent }")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QRect(0, 0, 850, 800))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMinimumSize(QSize(810, 800))
        self.scrollArea.setLayoutDirection(Qt.LeftToRight)
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 830, 1300))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(830, 1300))
        self.scrollAreaWidgetContents.setCursor(QCursor(Qt.ArrowCursor))
        self.scrollAreaWidgetContents.setLayoutDirection(Qt.LeftToRight)
        self.scrollAreaWidgetContents.setStyleSheet(u"*{background-color: #F2E6DF;\n"
"font-family: Montserrat Alternates;}\n"
"\n"
"QPushButton {border-radius: 25px;\n"
"background-color: #D9C5C1; }\n"
"\n"
"QPushButton:hover:enabled { \n"
"background-color: white;\n"
"border: 2px solid #D9C5C1; }\n"
"\n"
"QPushButton:enabled  { background-color: #D9C5C1;}\n"
"\n"
"QLabel { background: transparent; }\n"
"QTextEdit, QLineEdit {background-color: #D9C5C1;\n"
"color: #362121;\n"
"padding-left: 10px;}\n"
"\n"
"QRadioButton { background: transparent; }\n"
"QRadioButton::indicator {\n"
"width: 11px; \n"
"height: 11px; \n"
"border-radius: 5px;\n"
"background-color: #D9C5C1;\n"
"}\n"
"QRadioButton::indicator::checked{ \n"
"border: 3px solid #F2E6DF;\n"
"background-color: #362121;\n"
"border-radius: 4px;\n"
"width: 7px; \n"
"height: 7px; \n"
"}")
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 20, 741, 1230))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(30, 10, 10, 10)

        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)

        # row 0
        self.testLabel = QLabel(self.gridLayoutWidget)
        self.testLabel.setObjectName(u"testLabel")
        self.testLabel.setMinimumSize(QSize(0, 0))
        self.testLabel.setStyleSheet(u"font-size: 40px;")
        self.gridLayout.addWidget(self.testLabel, 0, 0, 1, 1)

        self.nameInput = QTextEdit(self.gridLayoutWidget)
        self.nameInput.setObjectName(u"nameInput")
        sizePolicy2.setHeightForWidth(self.nameInput.sizePolicy().hasHeightForWidth())
        self.nameInput.setSizePolicy(sizePolicy2)
        self.nameInput.setMinimumSize(QSize(250, 30))
        self.nameInput.setText("Ваше имя: ")
        self.nameInput.setMaximumHeight(30)
        self.nameInput.setStyleSheet(u"border-radius: 5px;")
        self.gridLayout.addWidget(self.nameInput, 0, 1, 1, 1)

        # row 1 spacer
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 2)

        # row 2
        self.cardImg = QLabel(self.gridLayoutWidget)
        self.cardImg.setObjectName(u"cardImg")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(40)
        sizePolicy3.setHeightForWidth(self.cardImg.sizePolicy().hasHeightForWidth())
        self.cardImg.setSizePolicy(sizePolicy3)
        self.cardImg.setMinimumSize(QSize(0, 0))
        self.cardImg.setMaximumSize(QSize(720, 400))
        self.cardImg.setLayoutDirection(Qt.LeftToRight)
        self.cardImg.setStyleSheet(u"background-color: #D9C5C1;")
        self.gridLayout.addWidget(self.cardImg, 2, 0, 1, 2)

        # row 3
        self.carlLabel = QLabel(self.gridLayoutWidget)
        self.carlLabel.setObjectName(u"carlLabel")
        self.carlLabel.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Montserrat Alternates"])
        font.setItalic(True)
        self.carlLabel.setFont(font)
        self.carlLabel.setStyleSheet(u"")
        self.gridLayout.addWidget(self.carlLabel, 3, 0, 1, 2)

        # row 4 spacer
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer_2, 4, 0, 1, 2)

        # row 5
        self.whatLbl = QLabel(self.gridLayoutWidget)
        self.whatLbl.setObjectName(u"whatLbl")
        self.whatLbl.setMinimumSize(QSize(0, 0))
        self.gridLayout.addWidget(self.whatLbl, 5, 0, 1, 2)

        # row 7
        self.whatInput = QTextEdit(self.gridLayoutWidget)
        self.whatInput.setObjectName(u"whatInput")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.whatInput.sizePolicy().hasHeightForWidth())
        self.whatInput.setSizePolicy(sizePolicy4)
        self.whatInput.setMinimumSize(QSize(0, 85))
        self.whatInput.setMaximumSize(QSize(750, 85))
        self.whatInput.setStyleSheet(u"border-radius: 10px;")
        self.gridLayout.addWidget(self.whatInput, 6, 0, 1, 2)

        # row 7 spacer
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer_3, 7, 0, 1, 2)

        # row 8
        self.formLbl = QLabel(self.gridLayoutWidget)
        self.formLbl.setObjectName(u"formLbl")
        self.formLbl.setMinimumSize(QSize(0, 0))
        self.gridLayout.addWidget(self.formLbl, 8, 0, 1, 2)

        # row 9-10
        self.formYesRadioBtn = QRadioButton(self.gridLayoutWidget)
        self.formYesRadioBtn.setObjectName(u"formYesRadioBtn")
        self.formYesRadioBtn.setMinimumSize(QSize(0, 0))
        self.gridLayout.addWidget(self.formYesRadioBtn, 9, 0, 1, 2)

        self.formNoRadioBtn = QRadioButton(self.gridLayoutWidget)
        self.formNoRadioBtn.setObjectName(u"formNoRadioBtn")
        self.formNoRadioBtn.setMinimumSize(QSize(0, 0))
        self.gridLayout.addWidget(self.formNoRadioBtn, 10, 0, 1, 2)

        self.formGroup = QButtonGroup(MainWindow)
        self.formGroup.setObjectName(u"formGroup")
        self.formGroup.addButton(self.formYesRadioBtn)
        self.formGroup.addButton(self.formNoRadioBtn)

        # row 11 spacer
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer_4, 11, 0, 1, 2)

        # row 12
        self.actionLbl = QLabel(self.gridLayoutWidget)
        self.actionLbl.setObjectName(u"actionLbl")
        self.actionLbl.setMinimumSize(QSize(0, 0))
        self.gridLayout.addWidget(self.actionLbl, 12, 0, 1, 2)

        # row 13-14
        self.actionYesRadioBtn = QRadioButton(self.gridLayoutWidget)
        self.actionYesRadioBtn.setObjectName(u"actionYesRadioBtn")
        self.actionYesRadioBtn.setMinimumSize(QSize(0, 0))
        self.actionYesRadioBtn.setStyleSheet(u"")
        self.gridLayout.addWidget(self.actionYesRadioBtn, 13, 0, 1, 2)

        self.actionNoRadioBtn = QRadioButton(self.gridLayoutWidget)
        self.actionNoRadioBtn.setObjectName(u"actionNoRadioBtn")
        self.actionNoRadioBtn.setMinimumSize(QSize(0, 0))
        self.gridLayout.addWidget(self.actionNoRadioBtn, 14, 0, 1, 2)

        self.actionGroup = QButtonGroup(MainWindow)
        self.actionGroup.setObjectName(u"actionGroup")
        self.actionGroup.addButton(self.actionYesRadioBtn)
        self.actionGroup.addButton(self.actionNoRadioBtn)

        # row 15 spacer
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer_5, 15, 0, 1, 2)

        # row 16
        self.partLbl = QLabel(self.gridLayoutWidget)
        self.partLbl.setObjectName(u"partLbl")
        self.partLbl.setMinimumSize(QSize(0, 0))
        self.gridLayout.addWidget(self.partLbl, 16, 0, 1, 2)

        # row 17-21
        self.allPartRadioBtn = QRadioButton(self.gridLayoutWidget)
        self.allPartRadioBtn.setObjectName(u"allPartRadioBtn")
        self.allPartRadioBtn.setMinimumSize(QSize(0, 0))
        self.gridLayout.addWidget(self.allPartRadioBtn, 17, 0, 1, 2)

        self.partPartRadioBtn = QRadioButton(self.gridLayoutWidget)
        self.partPartRadioBtn.setObjectName(u"partPartRadioBtn")
        self.partPartRadioBtn.setMinimumSize(QSize(0, 0))
        self.gridLayout.addWidget(self.partPartRadioBtn, 18, 0, 1, 2)

        self.partSeparateRadioBtn = QRadioButton(self.gridLayoutWidget)
        self.partSeparateRadioBtn.setObjectName(u"partSeparateRadioBtn")
        self.partSeparateRadioBtn.setMinimumSize(QSize(0, 0))
        self.gridLayout.addWidget(self.partSeparateRadioBtn, 19, 0, 1, 2)

        self.partBackRadioBtn = QRadioButton(self.gridLayoutWidget)
        self.partBackRadioBtn.setObjectName(u"partBackRadioBtn")
        self.partBackRadioBtn.setMinimumSize(QSize(0, 0))
        self.gridLayout.addWidget(self.partBackRadioBtn, 20, 0, 1, 2)

        self.partOtherRadioBtn = QRadioButton(self.gridLayoutWidget)
        self.partOtherRadioBtn.setObjectName(u"partOtherRadioBtn")
        self.partOtherRadioBtn.setMinimumSize(QSize(0, 0))
        self.gridLayout.addWidget(self.partOtherRadioBtn, 21, 0, 1, 2)

        self.partGroup = QButtonGroup(MainWindow)
        self.partGroup.setObjectName(u"partGroup")
        self.partGroup.addButton(self.allPartRadioBtn)
        self.partGroup.addButton(self.partPartRadioBtn)
        self.partGroup.addButton(self.partSeparateRadioBtn)
        self.partGroup.addButton(self.partBackRadioBtn)
        self.partGroup.addButton(self.partOtherRadioBtn)

        # row 22 spacer
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer_6, 22, 0, 1, 2)

        # row 23
        self.signLbl = QLabel(self.gridLayoutWidget)
        self.signLbl.setObjectName(u"signLbl")
        self.signLbl.setMinimumSize(QSize(0, 0))
        self.gridLayout.addWidget(self.signLbl, 23, 0, 1, 2)

        # row 24 - 26
        self.signFormColorRadioBtn = QRadioButton(self.gridLayoutWidget)
        self.signFormColorRadioBtn.setObjectName(u"signFormColorRadioBtn")
        self.signFormColorRadioBtn.setMinimumSize(QSize(0, 0))
        self.gridLayout.addWidget(self.signFormColorRadioBtn, 24, 0, 1, 2)

        self.signColorFormRadioBtn = QRadioButton(self.gridLayoutWidget)
        self.signColorFormRadioBtn.setObjectName(u"signColorFormRadioBtn")
        self.signColorFormRadioBtn.setMinimumSize(QSize(0, 0))
        self.gridLayout.addWidget(self.signColorFormRadioBtn, 25, 0, 1, 2)

        self.signColoRadioBtn = QRadioButton(self.gridLayoutWidget)
        self.signColoRadioBtn.setObjectName(u"signColoRadioBtn")
        self.signColoRadioBtn.setMinimumSize(QSize(0, 0))
        self.gridLayout.addWidget(self.signColoRadioBtn, 26, 0, 1, 2)

        self.signGroup = QButtonGroup(MainWindow)
        self.signGroup.setObjectName(u"signGroup")
        self.signGroup.addButton(self.signFormColorRadioBtn)
        self.signGroup.addButton(self.signColorFormRadioBtn)
        self.signGroup.addButton(self.signColoRadioBtn)

        # row 27 spacer
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer_7, 27, 0, 1, 2)

        # row 28
        self.rejectionBtn = QPushButton(self.gridLayoutWidget)
        self.rejectionBtn.setObjectName(u"rejectionBtn")
        self.rejectionBtn.setMinimumSize(QSize(150, 50))
        self.rejectionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.rejectionBtn.setStyleSheet(u"")
        self.rejectionBtn.setCheckable(True)
        sizePolicy2.setHeightForWidth(self.rejectionBtn.sizePolicy().hasHeightForWidth())
        self.rejectionBtn.setSizePolicy(sizePolicy2)
        self.gridLayout.addWidget(self.rejectionBtn, 28, 0, 1, 1)

        self.sendBtn = QPushButton(self.gridLayoutWidget)
        self.sendBtn.setObjectName(u"sendBtn")
        sizePolicy2.setHeightForWidth(self.sendBtn.sizePolicy().hasHeightForWidth())
        self.sendBtn.setSizePolicy(sizePolicy2)
        self.sendBtn.setMinimumSize(QSize(150, 50))
        self.sendBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.sendBtn.setStyleSheet(u"")
        self.sendBtn.setCheckable(True)
        self.gridLayout.addWidget(self.sendBtn, 28, 1, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442 \u0420\u043e\u0440\u0448\u0430\u0445\u0430", None))
        self.signColorFormRadioBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0436\u043d\u0435\u0435 \u0446\u0432\u0435\u0442, \u0444\u043e\u0440\u043c\u0430 \u0432\u0442\u043e\u0440\u0438\u0447\u043d\u0430", None))
        self.formYesRadioBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.partSeparateRadioBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u0435\u043b\u044c\u043d\u044b\u0435 \u043f\u044f\u0442\u043d\u0430 \u0438\u043b\u0438 \u043c\u0435\u043b\u043a\u0438\u0435 \u0434\u0435\u0442\u0430\u043b\u0438", None))
        self.rejectionBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0430\u0437\u0430\u0442\u044c\u0441\u044f \u043e\u0442 \u043e\u0442\u0432\u0435\u0442\u0430", None))
        self.allPartRadioBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0451 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0438\u043b\u0438 \u0431\u043e\u043b\u044c\u0448\u0430\u044f \u0435\u0433\u043e \u0447\u0430\u0441\u0442\u044c", None))
        self.testLabel.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442 \u0420\u043e\u0440\u0448\u0430\u0445\u0430", None))
        self.formNoRadioBtn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.cardImg.setText("")
        self.actionNoRadioBtn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.partOtherRadioBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0443\u0433\u043e\u0435", None))
        self.signColoRadioBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0436\u0435\u043d \u0442\u043e\u043b\u044c\u043a\u043e \u0446\u0432\u0435\u0442", None))
#if QT_CONFIG(whatsthis)
        self.carlLabel.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.carlLabel.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 1 \u0438\u0437 10", None))
        self.sendBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043e\u0442\u0432\u0435\u0442", None))
        self.partBackRadioBtn.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0435\u043b\u044b\u0439 \u0444\u043e\u043d", None))
        self.signLbl.setText(QCoreApplication.translate("MainWindow", u"5. \u041d\u0430 \u0432\u0430\u0448 \u043e\u0442\u0432\u0435\u0442 \u043f\u043e\u0432\u043b\u0438\u044f\u043b\u0438 \u0446\u0432\u0435\u0442 \u0438\u043b\u0438 \u0444\u043e\u0440\u043c\u0430?", None))
        self.formLbl.setText(QCoreApplication.translate("MainWindow", u"2. \u0423\u0432\u0438\u0434\u0435\u043d\u043d\u043e\u0435 \u0438\u043c\u0435\u0435\u0442 \u0447\u0451\u0442\u043a\u0443\u044e \u0444\u043e\u0440\u043c\u0443?", None))
        self.partLbl.setText(QCoreApplication.translate("MainWindow", u"4. \u0412 \u043a\u0430\u043a\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u0412\u044b \u0443\u0432\u0438\u0434\u0435\u043b\u0438 \u043e\u0431\u0440\u0430\u0437?", None))
        self.actionLbl.setText(QCoreApplication.translate("MainWindow", u"3. \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u0432\u0438\u0436\u0435\u0442\u0441\u044f \u0438\u043b\u0438 \u0438\u0441\u043a\u0430\u0436\u0430\u0435\u0442\u0441\u044f?", None))
        self.actionYesRadioBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.whatLbl.setText(QCoreApplication.translate("MainWindow", u"1. \u0427\u0442\u043e \u0412\u044b \u0432\u0438\u0434\u0438\u0442\u0435 \u043d\u0430 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0435?", None))
        self.partPartRadioBtn.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u044c \u0431\u043e\u043b\u044c\u0448\u043e\u0433\u043e \u043f\u044f\u0442\u043d\u0430", None))
        self.signFormColorRadioBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0436\u043d\u0435\u0435 \u0444\u043e\u0440\u043c\u0430, \u0446\u0432\u0435\u0442 \u0432\u0442\u043e\u0440\u0438\u0447\u0435\u043d", None))
    # retranslateUi

