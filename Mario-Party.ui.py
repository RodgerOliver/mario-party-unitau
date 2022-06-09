# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mario-Party.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MarioParty(object):
    def setupUi(self, MarioParty):
        MarioParty.setObjectName("MarioParty")
        MarioParty.resize(825, 600)
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
        self.retorno.setText(_translate("MarioParty", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MarioParty = QtWidgets.QMainWindow()
    ui = Ui_MarioParty()
    ui.setupUi(MarioParty)
    MarioParty.show()
    sys.exit(app.exec_())
