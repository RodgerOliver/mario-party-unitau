from Mario_Party_ui import *
from src.busca_local_sem_info import *

class MarioParty(Ui_MarioParty):
    def init(self, MarioPartyWindow):
        Ui_MarioParty.setupUi(self, MarioPartyWindow)
        self.retorno.setText('O retorno da solução aparecerá aqui!')
        self.setButtonsAction()

    def setButtonsAction(self):
        self.amplitude.clicked.connect(self.amplitude_clicked)
        self.profundidade.clicked.connect(self.profundidade_clicked)
        self.profundidade_limitada.clicked.connect(self.profundidade_limitada_clicked)
        self.aprofundamento_interativo.clicked.connect(self.aprofundamento_interativo_clicked)
        self.bidirecional.clicked.connect(self.bidirecional_clicked)

    def amplitude_clicked(self):
        self.button_clicked(busca().amplitude(origem, destino))

    def profundidade_clicked(self):
        self.button_clicked(busca().profundidade(origem, destino))

    def profundidade_limitada_clicked(self):
        limite = int(self.profundidade_limite.text())
        self.button_clicked(busca().prof_limitada(origem, destino, limite))

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
