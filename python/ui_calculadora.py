# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadora.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(291, 428)
        icon = QIcon()
        icon.addFile(u"../img/calcu.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 311, 391))
        self.frame.setStyleSheet(u"QObject{\n"
"	background-color: #04030F; \n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txtmostrar = QLineEdit(self.frame)
        self.txtmostrar.setObjectName(u"txtmostrar")
        self.txtmostrar.setGeometry(QRect(10, 10, 271, 71))
        self.txtmostrar.setStyleSheet(u"QObject{\n"
"	background-color: #ccc;\n"
"	color:black;\n"
"	\n"
"	font: 75 20pt \"Arial\";\n"
"	border: 2px solid blue;\n"
"}")
        self.btncero = QPushButton(self.frame)
        self.btncero.setObjectName(u"btncero")
        self.btncero.setGeometry(QRect(10, 320, 131, 51))
        self.btncero.setStyleSheet(u"QObject{\n"
"	background-color:#F00707;\n"
"	color: black;\n"
"	font: 75 19pt \"Georgia\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: #ccc;\n"
"}")
        self.btnuno = QPushButton(self.frame)
        self.btnuno.setObjectName(u"btnuno")
        self.btnuno.setGeometry(QRect(10, 260, 61, 51))
        self.btnuno.setStyleSheet(u"QObject{\n"
"	background-color:#F00707;\n"
"	color: black;\n"
"	font: 75 19pt \"Georgia\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: #ccc;\n"
"}")
        self.btndos = QPushButton(self.frame)
        self.btndos.setObjectName(u"btndos")
        self.btndos.setGeometry(QRect(80, 260, 61, 51))
        self.btndos.setStyleSheet(u"QObject{\n"
"	background-color:#F00707;\n"
"	color: black;\n"
"	font: 75 19pt \"Georgia\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: #ccc;\n"
"}")
        self.btnpunto = QPushButton(self.frame)
        self.btnpunto.setObjectName(u"btnpunto")
        self.btnpunto.setGeometry(QRect(150, 320, 61, 51))
        self.btnpunto.setStyleSheet(u"QObject{\n"
"	background-color:#F00707;\n"
"	color: black;\n"
"	font: 75 15pt \"Georgia\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: #ccc;\n"
"}")
        self.btnsuma = QPushButton(self.frame)
        self.btnsuma.setObjectName(u"btnsuma")
        self.btnsuma.setGeometry(QRect(220, 320, 61, 51))
        self.btnsuma.setStyleSheet(u"QObject{\n"
"	background-color:#F00707;\n"
"	color: black;\n"
"	font: 75 15pt \"Georgia\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: #ccc;\n"
"}")
        self.btntres = QPushButton(self.frame)
        self.btntres.setObjectName(u"btntres")
        self.btntres.setGeometry(QRect(150, 260, 61, 51))
        self.btntres.setStyleSheet(u"QObject{\n"
"	background-color:#F00707;\n"
"	color: black;\n"
"	font: 75 15pt \"Georgia\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: #ccc;\n"
"}")
        self.btnresta = QPushButton(self.frame)
        self.btnresta.setObjectName(u"btnresta")
        self.btnresta.setGeometry(QRect(220, 260, 61, 51))
        self.btnresta.setStyleSheet(u"QObject{\n"
"	background-color:#F00707;\n"
"	color: black;\n"
"	font: 75 15pt \"Georgia\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: #ccc;\n"
"}")
        self.btncuatro = QPushButton(self.frame)
        self.btncuatro.setObjectName(u"btncuatro")
        self.btncuatro.setGeometry(QRect(10, 200, 61, 51))
        self.btncuatro.setStyleSheet(u"QObject{\n"
"	background-color:#F00707;\n"
"	color: black;\n"
"	font: 75 15pt \"Georgia\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: #ccc;\n"
"}")
        self.btncinco = QPushButton(self.frame)
        self.btncinco.setObjectName(u"btncinco")
        self.btncinco.setGeometry(QRect(80, 200, 61, 51))
        self.btncinco.setStyleSheet(u"QObject{\n"
"	background-color:#F00707;\n"
"	color: black;\n"
"	font: 75 15pt \"Georgia\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: #ccc;\n"
"}")
        self.btnseis = QPushButton(self.frame)
        self.btnseis.setObjectName(u"btnseis")
        self.btnseis.setGeometry(QRect(150, 200, 61, 51))
        self.btnseis.setStyleSheet(u"QObject{\n"
"	background-color:#F00707;\n"
"	color: black;\n"
"	font: 75 15pt \"Georgia\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: #ccc;\n"
"}")
        self.btndiv = QPushButton(self.frame)
        self.btndiv.setObjectName(u"btndiv")
        self.btndiv.setGeometry(QRect(220, 200, 61, 51))
        self.btndiv.setStyleSheet(u"QObject{\n"
"	background-color:#F00707;\n"
"	color: black;\n"
"	font: 75 15pt \"Georgia\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: #ccc;\n"
"}")
        self.btnsiete = QPushButton(self.frame)
        self.btnsiete.setObjectName(u"btnsiete")
        self.btnsiete.setGeometry(QRect(10, 140, 61, 51))
        self.btnsiete.setStyleSheet(u"QObject{\n"
"	background-color:#F00707;\n"
"	color: black;\n"
"	font: 75 15pt \"Georgia\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: #ccc;\n"
"}")
        self.btnocho = QPushButton(self.frame)
        self.btnocho.setObjectName(u"btnocho")
        self.btnocho.setGeometry(QRect(80, 140, 61, 51))
        self.btnocho.setStyleSheet(u"QObject{\n"
"	background-color:#F00707;\n"
"	color: black;\n"
"	font: 75 15pt \"Georgia\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: #ccc;\n"
"}")
        self.btnnueve = QPushButton(self.frame)
        self.btnnueve.setObjectName(u"btnnueve")
        self.btnnueve.setGeometry(QRect(150, 140, 61, 51))
        self.btnnueve.setStyleSheet(u"QObject{\n"
"	background-color:#F00707;\n"
"	color: black;\n"
"	font: 75 15pt \"Georgia\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: #ccc;\n"
"}")
        self.btnmulti = QPushButton(self.frame)
        self.btnmulti.setObjectName(u"btnmulti")
        self.btnmulti.setGeometry(QRect(220, 140, 61, 51))
        self.btnmulti.setStyleSheet(u"QObject{\n"
"	background-color:#F00707;\n"
"	color: black;\n"
"	font: 75 15pt \"Georgia\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: #ccc;\n"
"}")
        self.btnclear = QPushButton(self.frame)
        self.btnclear.setObjectName(u"btnclear")
        self.btnclear.setGeometry(QRect(10, 90, 131, 41))
        self.btnclear.setStyleSheet(u"QObject{\n"
"	background-color:#F00707;\n"
"	color: black;\n"
"	font: 75 15pt \"Georgia\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: #ccc;\n"
"}")
        self.btnenter = QPushButton(self.frame)
        self.btnenter.setObjectName(u"btnenter")
        self.btnenter.setGeometry(QRect(150, 90, 131, 41))
        self.btnenter.setStyleSheet(u"QObject{\n"
"	background-color:#F00707;\n"
"	color: black;\n"
"	font: 75 15pt \"Georgia\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: #ccc;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 291, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculadora", None))
        self.txtmostrar.setText("")
        self.btncero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnuno.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btndos.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btnpunto.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btnsuma.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btntres.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btnresta.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btncuatro.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btncinco.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btnseis.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btndiv.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.btnsiete.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btnocho.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btnnueve.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btnmulti.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.btnclear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.btnenter.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
    # retranslateUi

