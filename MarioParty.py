import sys
from PyQt5 import QtWidgets
from Mario_Party_ui import Ui_MarioParty
from PyQt5.QtWidgets import QMessageBox
from src.busca_local_sem_info import busca as busca_local_sem_info
import src.busca_local_com_info as busca_local_com_info

class MarioParty(Ui_MarioParty):

    GRAFO_LENG = 26 # Pontos no gráfico
    ARESTA_MIN = 5  # Limites mínimos da rotina RANDINT
    ARESTA_MAX = 25 # Limites máximos da rotina RANDINT

    def setupUi(self, MarioPartyWindow):
        Ui_MarioParty.setupUi(self, MarioPartyWindow)
        self.retorno.setText('O retorno da solução aparecerá aqui!')
        self.updateInputs()
        self.setButtonsEvents()
        self.setInputsEvents()

        self.valores_arestas = busca_local_com_info.gerar_ambiente(
            self.GRAFO_LENG, self.ARESTA_MIN, self.ARESTA_MAX)
        print(self.valores_arestas)

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
        self.input_tentativas = int(self.tentativas.text())
        self.input_temperatura_maxima = int(self.temperatura_maxima.text())
        self.input_temperatura_minima = float(self.temperatura_minima.text())
        self.input_fator_redutor = float(self.fator_redutor.text())

    def setButtonsEvents(self):
        # busca local sem info
        self.amplitude.clicked.connect(self.amplitude_clicked)
        self.profundidade.clicked.connect(self.profundidade_clicked)
        self.profundidade_limitada.clicked.connect(self.profundidade_limitada_clicked)
        self.aprofundamento_interativo.clicked.connect(self.aprofundamento_interativo_clicked)
        self.bidirecional.clicked.connect(self.bidirecional_clicked)
        # busca local com info
        self.cacheiro_viajante.clicked.connect(self.cacheiro_viajante_clicked)

    def setInputsEvents(self):
        self.origem.currentTextChanged.connect(self.updateInputs)
        self.destino.currentTextChanged.connect(self.updateInputs)
        self.profundidade_limite.textChanged.connect(self.updateInputs)
        self.tentativas.textChanged.connect(self.updateInputs)

    def amplitude_clicked(self):
        try:
            self.output_busca_local_sem_info(busca_local_sem_info().amplitude(self.input_origem, self.input_destino),
                'Amplitude')
        except BaseException as err:
            self.showError(err)

    def profundidade_clicked(self):
        try:
            self.output_busca_local_sem_info(busca_local_sem_info().profundidade(self.input_origem, self.input_destino),
                'Profundidade')
        except BaseException as err:
            self.showError(err)

    def profundidade_limitada_clicked(self):
        try:
            self.output_busca_local_sem_info(busca_local_sem_info().prof_limitada(self.input_origem, self.input_destino, self.input_limite),
                'Profundidade Limitada')
        except BaseException as err:
            self.showError(err)

    def aprofundamento_interativo_clicked(self):
        try:
            self.output_busca_local_sem_info(busca_local_sem_info().aprof_iterativo(self.input_origem, self.input_destino, self.input_limite),
                'Aprofundamento Interativo')
        except BaseException as err:
            self.showError(err)

    def bidirecional_clicked(self):
        try:
            self.output_busca_local_sem_info(busca_local_sem_info().bidirecional(self.input_origem, self.input_destino),
                'Bidirecional')
        except BaseException as err:
            self.showError(err)

    def cacheiro_viajante_clicked(self):
        try:
            solucao_inicial = busca_local_com_info.solucao_inicial(self.GRAFO_LENG)
            custo_solucao_inicial = busca_local_com_info.avalia(self.GRAFO_LENG, solucao_inicial, self.valores_arestas)
            solucao_final_encosta, custo_encosta = busca_local_com_info.encosta(
                self.GRAFO_LENG, solucao_inicial, custo_solucao_inicial, self.valores_arestas)

            tentativas1 = int(self.input_tentativas / 2)
            solucao_final_alt1, custo_encosta_alt1 = busca_local_com_info.encosta_alt(
                self.GRAFO_LENG, solucao_inicial, custo_solucao_inicial, self.valores_arestas, tentativas1)
            tentativas2 = int(self.input_tentativas * 0.1)
            solucao_final_encosta_alt2, custo_encosta_alt2 = busca_local_com_info.encosta_alt(
                self.GRAFO_LENG, solucao_inicial, custo_solucao_inicial, self.valores_arestas, tentativas2)
            solucao_final, custo_encosta_alt = busca_local_com_info.encosta_alt(
                self.GRAFO_LENG, solucao_inicial, custo_solucao_inicial, self.valores_arestas, self.input_tentativas)

            temperatura_maxima = 500
            temperatura_minima = 0.01
            fator_redutor = 0.7
            solucao_final_tempera, custo_tempera = busca_local_com_info.tempera(
                self.GRAFO_LENG, solucao_inicial, custo_solucao_inicial, self.valores_arestas,
                temperatura_maxima, temperatura_minima, fator_redutor)
            solucao_final_tempera2, custo_tempera2 = busca_local_com_info.tempera(
                self.GRAFO_LENG, solucao_inicial, custo_solucao_inicial, self.valores_arestas,
                self.input_temperatura_maxima, self.input_temperatura_minima, self.input_fator_redutor)

            retorno = 'Mario Viajante (Custos):\n'
            retorno += 'Solução inicial: ' + str(custo_solucao_inicial) + '\n'
            retorno += 'Subida de encosta: ' + str(custo_encosta) + '\n'
            retorno += 'Subida de encosta com ' + str(tentativas1) \
               + ' tentativas: ' + str(custo_encosta_alt1) + '\n'
            retorno += 'Subida de encosta com ' + str(tentativas2) \
               + ' tentativas: ' + str(custo_encosta_alt2) + '\n'
            retorno += 'Subida de encosta com ' + str(self.input_tentativas) \
               + ' tentativas: ' + str(custo_encosta_alt) + '\n'
            retorno += 'Têmpera simulada (500, 0.01, 0.7): ' + str(custo_tempera) + '\n'
            retorno += 'Têmpera simulada (inputs): ' + str(custo_tempera2) + '\n'

            self.retorno.setText(retorno)
        except BaseException as err:
            self.showError(err)

    def output_busca_local_sem_info(self, array_solucao, tipo_solucao):
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