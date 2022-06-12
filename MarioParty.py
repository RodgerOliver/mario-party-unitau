import sys
from PyQt5 import QtWidgets
from Mario_Party_ui import Ui_MarioParty
from PyQt5.QtWidgets import QMessageBox
from src.busca_local_sem_info import busca as busca_local_sem_info

class MarioParty(Ui_MarioParty):
    def setupUi(self, MarioPartyWindow):
        Ui_MarioParty.setupUi(self, MarioPartyWindow)
        self.retorno.setText('O retorno da solução aparecerá aqui!')
        self.updateInputs()
        self.setButtonsEvents()
        self.setInputsEvents()

    def showError(self, error):
        print(f"Unexpected {error=}, {type(error)=}")
        popup = QMessageBox()
        popup.setWindowTitle('Erro')
        popup.setText('Ocorreu um erro no algoritmo.')
        popup.setIcon(QMessageBox.Critical)
        popup.exec_()

    def updateInputs(self):
        self.input_origem = str(self.origem.currentText())
        self.input_destino = str(self.destino.currentText())
        self.input_limite = int(self.profundidade_limite.text())

    def setButtonsEvents(self):
        # busca local sem info
        self.amplitude.clicked.connect(self.amplitude_clicked)
        self.profundidade.clicked.connect(self.profundidade_clicked)
        self.profundidade_limitada.clicked.connect(self.profundidade_limitada_clicked)
        self.aprofundamento_interativo.clicked.connect(self.aprofundamento_interativo_clicked)
        self.bidirecional.clicked.connect(self.bidirecional_clicked)

    def setInputsEvents(self):
        self.origem.currentTextChanged.connect(self.updateInputs)
        self.destino.currentTextChanged.connect(self.updateInputs)
        self.profundidade_limite.textChanged.connect(self.updateInputs)

    def amplitude_clicked(self):
        try:
            self.button_clicked(busca_local_sem_info().amplitude(self.input_origem, self.input_destino),
                'Amplitude')
        except BaseException as err:
            self.showError(err)

    def profundidade_clicked(self):
        try:
            self.button_clicked(busca_local_sem_info().profundidade(self.input_origem, self.input_destino),
                'Profundidade')
        except BaseException as err:
            self.showError(err)

    def profundidade_limitada_clicked(self):
        try:
            self.button_clicked(busca_local_sem_info().prof_limitada(self.input_origem, self.input_destino, self.input_limite),
                'Profundidade Limitada')
        except BaseException as err:
            self.showError(err)

    def aprofundamento_interativo_clicked(self):
        try:
            self.button_clicked(busca_local_sem_info().aprof_iterativo(self.input_origem, self.input_destino, self.input_limite),
                'Aprofundamento Interativo')
        except BaseException as err:
            self.showError(err)

    def bidirecional_clicked(self):
        try:
            self.button_clicked(busca_local_sem_info().bidirecional(self.input_origem, self.input_destino),
                'Bidirecional')
        except BaseException as err:
            self.showError(err)

    def button_clicked(self, array_solucao, tipo_solucao):
        if self.input_origem == self.input_destino:
            self.retorno.setText('A origem e o destino devem ser diferentes.')
            return

        solucao = tipo_solucao + '\n'
        if array_solucao == []:
            self.retorno.setText(solucao + 'Solução não encontrada.')
            return

        solucao += 'Solução: '
        solucao += '[ ' + ', '.join(array_solucao) + ' ]'
        self.retorno.setText(solucao)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MarioPartyWindow = QtWidgets.QMainWindow()
    marioPartyUi = MarioParty()
    marioPartyUi.setupUi(MarioPartyWindow)
    MarioPartyWindow.show()
    sys.exit(app.exec_())