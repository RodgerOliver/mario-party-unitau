# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mario-Party.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from array import array
from ast import If
from PyQt5 import QtCore, QtGui, QtWidgets
from src.Mario_Party import *

class Ui_MarioParty(object):
    def setupUi(self, MarioParty):
        MarioParty.setObjectName("MarioParty")
        MarioParty.resize(825, 694)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/mario-logo.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MarioParty.setWindowIcon(icon)
        MarioParty.setStyleSheet("background-color: rgb(37, 40, 61);")
        MarioParty.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.centralwidget = QtWidgets.QWidget(MarioParty)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.amplitude = QtWidgets.QPushButton(self.centralwidget)
        self.amplitude.setGeometry(QtCore.QRect(30, 20, 141, 61))
        self.amplitude.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.amplitude.setStyleSheet("background-color: rgb(143, 57, 133);\n"
"font: 75 10pt \"Noto Sans CJK HK\";\n"
"color: rgb(255, 255, 255);")
        self.amplitude.setObjectName("amplitude")
        self.buttonGroup = QtWidgets.QButtonGroup(MarioParty)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.amplitude)
        self.imgCharacterSelect = QtWidgets.QLabel(self.centralwidget)
        self.imgCharacterSelect.setGeometry(QtCore.QRect(360, 20, 431, 221))
        self.imgCharacterSelect.setText("")
        self.imgCharacterSelect.setPixmap(QtGui.QPixmap("img/character-select.jpeg"))
        self.imgCharacterSelect.setScaledContents(True)
        self.imgCharacterSelect.setObjectName("imgCharacterSelect")
        self.imgPath = QtWidgets.QLabel(self.centralwidget)
        self.imgPath.setGeometry(QtCore.QRect(360, 260, 431, 271))
        self.imgPath.setText("")
        self.imgPath.setPixmap(QtGui.QPixmap("img/path.jpeg"))
        self.imgPath.setScaledContents(True)
        self.imgPath.setObjectName("imgPath")
        self.profundidade = QtWidgets.QPushButton(self.centralwidget)
        self.profundidade.setGeometry(QtCore.QRect(180, 20, 141, 61))
        self.profundidade.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profundidade.setStyleSheet("background-color: rgb(143, 57, 133);\n"
"font: 75 10pt \"Noto Sans CJK HK\";\n"
"color: rgb(255, 255, 255);")
        self.profundidade.setObjectName("profundidade")
        self.buttonGroup.addButton(self.profundidade)
        self.profundidade_limitada_l6 = QtWidgets.QPushButton(self.centralwidget)
        self.profundidade_limitada_l6.setGeometry(QtCore.QRect(180, 100, 141, 61))
        self.profundidade_limitada_l6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profundidade_limitada_l6.setStyleSheet("background-color: rgb(143, 57, 133);\n"
"font: 75 10pt \"Noto Sans CJK HK\";\n"
"color: rgb(255, 255, 255);")
        self.profundidade_limitada_l6.setObjectName("profundidade_limitada_l6")
        self.buttonGroup.addButton(self.profundidade_limitada_l6)
        self.profundidade_limitada_l2 = QtWidgets.QPushButton(self.centralwidget)
        self.profundidade_limitada_l2.setGeometry(QtCore.QRect(30, 100, 141, 61))
        self.profundidade_limitada_l2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profundidade_limitada_l2.setStyleSheet("background-color: rgb(143, 57, 133);\n"
"font: 75 10pt \"Noto Sans CJK HK\";\n"
"color: rgb(255, 255, 255);")
        self.profundidade_limitada_l2.setObjectName("profundidade_limitada_l2")
        self.buttonGroup.addButton(self.profundidade_limitada_l2)
        self.bidirecional = QtWidgets.QPushButton(self.centralwidget)
        self.bidirecional.setGeometry(QtCore.QRect(180, 180, 141, 61))
        self.bidirecional.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bidirecional.setStyleSheet("background-color: rgb(143, 57, 133);\n"
"font: 75 10pt \"Noto Sans CJK HK\";\n"
"color: rgb(255, 255, 255);")
        self.bidirecional.setObjectName("bidirecional")
        self.buttonGroup.addButton(self.bidirecional)
        self.aprofundamento_interativo = QtWidgets.QPushButton(self.centralwidget)
        self.aprofundamento_interativo.setGeometry(QtCore.QRect(30, 180, 141, 61))
        self.aprofundamento_interativo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aprofundamento_interativo.setStyleSheet("background-color: rgb(143, 57, 133);\n"
"font: 75 10pt \"Noto Sans CJK HK\";\n"
"color: rgb(255, 255, 255);")
        self.aprofundamento_interativo.setObjectName("aprofundamento_interativo")
        self.buttonGroup.addButton(self.aprofundamento_interativo)
        self.retorno = QtWidgets.QLabel(self.centralwidget)
        self.retorno.setGeometry(QtCore.QRect(30, 260, 291, 271))
        self.retorno.setStyleSheet("font: 75 10pt \"Noto Sans CJK HK\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(52, 138, 167);\n"
"padding: 10px;")
        self.retorno.setWordWrap(True)
        self.retorno.setObjectName("retorno")
        self.origem = QtWidgets.QComboBox(self.centralwidget)
        self.origem.setGeometry(QtCore.QRect(360, 540, 91, 41))
        self.origem.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.origem.setStyleSheet("background-color: rgb(93, 211, 158);\n"
"font: 75 15pt \"Noto Sans CJK HK\";")
        self.origem.setObjectName("origem")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem.addItem("")
        self.origem_label = QtWidgets.QLabel(self.centralwidget)
        self.origem_label.setGeometry(QtCore.QRect(370, 590, 71, 31))
        self.origem_label.setStyleSheet("font: 75 10pt \"Noto Sans CJK HK\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(52, 138, 167);\n"
"padding: 2px;")
        self.origem_label.setAlignment(QtCore.Qt.AlignCenter)
        self.origem_label.setWordWrap(True)
        self.origem_label.setObjectName("origem_label")
        self.destino = QtWidgets.QComboBox(self.centralwidget)
        self.destino.setGeometry(QtCore.QRect(700, 540, 91, 41))
        self.destino.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.destino.setStyleSheet("background-color: rgb(93, 211, 158);\n"
"font: 75 15pt \"Noto Sans CJK HK\";")
        self.destino.setObjectName("destino")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino.addItem("")
        self.destino_label = QtWidgets.QLabel(self.centralwidget)
        self.destino_label.setGeometry(QtCore.QRect(710, 590, 71, 31))
        self.destino_label.setStyleSheet("font: 75 10pt \"Noto Sans CJK HK\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(52, 138, 167);\n"
"padding: 2px;")
        self.destino_label.setAlignment(QtCore.Qt.AlignCenter)
        self.destino_label.setWordWrap(True)
        self.destino_label.setObjectName("destino_label")
        MarioParty.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MarioParty)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 20))
        self.menubar.setObjectName("menubar")
        MarioParty.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MarioParty)
        self.statusbar.setObjectName("statusbar")
        MarioParty.setStatusBar(self.statusbar)

        self.retranslateUi(MarioParty)
        QtCore.QMetaObject.connectSlotsByName(MarioParty)
        self.setButtonsAction()

    def retranslateUi(self, MarioParty):
        _translate = QtCore.QCoreApplication.translate
        MarioParty.setWindowTitle(_translate("MarioParty", "Mario Party"))
        self.amplitude.setText(_translate("MarioParty", "Amplitude"))
        self.profundidade.setText(_translate("MarioParty", "Profundidade"))
        self.profundidade_limitada_l6.setText(_translate("MarioParty", "Profundidade\n"
"Limitada L6"))
        self.profundidade_limitada_l2.setText(_translate("MarioParty", "Profundidade\n"
"Limitada L2"))
        self.bidirecional.setText(_translate("MarioParty", "Bidirecional"))
        self.aprofundamento_interativo.setText(_translate("MarioParty", "Aprofundamento\n"
"Interativo"))
        self.retorno.setText(_translate("MarioParty", "O retorno da solução aparecerá aqui!"))
        self.origem.setItemText(0, _translate("MarioParty", "A"))
        self.origem.setItemText(1, _translate("MarioParty", "B"))
        self.origem.setItemText(2, _translate("MarioParty", "C"))
        self.origem.setItemText(3, _translate("MarioParty", "D"))
        self.origem.setItemText(4, _translate("MarioParty", "E"))
        self.origem.setItemText(5, _translate("MarioParty", "F"))
        self.origem.setItemText(6, _translate("MarioParty", "G"))
        self.origem.setItemText(7, _translate("MarioParty", "H"))
        self.origem.setItemText(8, _translate("MarioParty", "I"))
        self.origem.setItemText(9, _translate("MarioParty", "J"))
        self.origem.setItemText(10, _translate("MarioParty", "K"))
        self.origem.setItemText(11, _translate("MarioParty", "L"))
        self.origem.setItemText(12, _translate("MarioParty", "M"))
        self.origem.setItemText(13, _translate("MarioParty", "N"))
        self.origem.setItemText(14, _translate("MarioParty", "O"))
        self.origem.setItemText(15, _translate("MarioParty", "P"))
        self.origem.setItemText(16, _translate("MarioParty", "Q"))
        self.origem.setItemText(17, _translate("MarioParty", "S"))
        self.origem.setItemText(18, _translate("MarioParty", "T"))
        self.origem.setItemText(19, _translate("MarioParty", "U"))
        self.origem.setItemText(20, _translate("MarioParty", "V"))
        self.origem.setItemText(21, _translate("MarioParty", "W"))
        self.origem.setItemText(22, _translate("MarioParty", "X"))
        self.origem.setItemText(23, _translate("MarioParty", "Y"))
        self.origem.setItemText(24, _translate("MarioParty", "Z"))
        self.origem_label.setText(_translate("MarioParty", "Origem"))
        self.destino.setItemText(0, _translate("MarioParty", "A"))
        self.destino.setItemText(1, _translate("MarioParty", "B"))
        self.destino.setItemText(2, _translate("MarioParty", "C"))
        self.destino.setItemText(3, _translate("MarioParty", "D"))
        self.destino.setItemText(4, _translate("MarioParty", "E"))
        self.destino.setItemText(5, _translate("MarioParty", "F"))
        self.destino.setItemText(6, _translate("MarioParty", "G"))
        self.destino.setItemText(7, _translate("MarioParty", "H"))
        self.destino.setItemText(8, _translate("MarioParty", "I"))
        self.destino.setItemText(9, _translate("MarioParty", "J"))
        self.destino.setItemText(10, _translate("MarioParty", "K"))
        self.destino.setItemText(11, _translate("MarioParty", "L"))
        self.destino.setItemText(12, _translate("MarioParty", "M"))
        self.destino.setItemText(13, _translate("MarioParty", "N"))
        self.destino.setItemText(14, _translate("MarioParty", "O"))
        self.destino.setItemText(15, _translate("MarioParty", "P"))
        self.destino.setItemText(16, _translate("MarioParty", "Q"))
        self.destino.setItemText(17, _translate("MarioParty", "S"))
        self.destino.setItemText(18, _translate("MarioParty", "T"))
        self.destino.setItemText(19, _translate("MarioParty", "U"))
        self.destino.setItemText(20, _translate("MarioParty", "V"))
        self.destino.setItemText(21, _translate("MarioParty", "W"))
        self.destino.setItemText(22, _translate("MarioParty", "X"))
        self.destino.setItemText(23, _translate("MarioParty", "Y"))
        self.destino.setItemText(24, _translate("MarioParty", "Z"))
        self.destino_label.setText(_translate("MarioParty", "Destino"))

    def setButtonsAction(self):
        self.amplitude.clicked.connect(self.amplitude_clicked)
        self.profundidade.clicked.connect(self.profundidade_clicked)
        self.profundidade_limitada_l2.clicked.connect(self.profundidade_limitada_l2_clicked)
        self.profundidade_limitada_l6.clicked.connect(self.profundidade_limitada_l6_clicked)
        self.aprofundamento_interativo.clicked.connect(self.aprofundamento_interativo_clicked)
        self.bidirecional.clicked.connect(self.bidirecional_clicked)

    def amplitude_clicked(self):
        self.button_clicked(busca().amplitude(origem, destino))

    def profundidade_clicked(self):
        self.button_clicked(busca().profundidade(origem, destino))

    def profundidade_limitada_l2_clicked(self):
        self.button_clicked(busca().prof_limitada(origem, destino, 2))

    def profundidade_limitada_l6_clicked(self):
        self.button_clicked(busca().prof_limitada(origem, destino, 6))

    def aprofundamento_interativo_clicked(self):
        self.button_clicked(busca().aprof_iterativo(origem, destino, 6))

    def bidirecional_clicked(self):
        self.button_clicked(busca().bidirecional(origem, destino))

    def button_clicked(self, array_solucao):
        origem = str(self.origem.currentText())
        destino = str(self.destino.currentText())
        if origem == destino:
            self.retorno.setText('A origem e o destino devem ser diferentes.')
            return

        if array_solucao == []:
            self.retorno.setText('Solução não encontrada.')
            return

        solucao = 'Solução: '
        solucao += '[ ' + ', '.join(array_solucao) + ' ]'
        self.retorno.setText(solucao)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MarioParty = QtWidgets.QMainWindow()
    ui = Ui_MarioParty()
    ui.setupUi(MarioParty)
    MarioParty.show()
    sys.exit(app.exec_())
