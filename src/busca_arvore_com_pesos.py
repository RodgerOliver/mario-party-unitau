class No(object):
    def __init__(self, pai=None, estado=None, valor1=None, valor2=None, anterior=None, proximo=None):
        self.pai       = pai
        self.estado    = estado
        self.valor1    = valor1        # valor do nó na árvore
        self.valor2    = valor2        # custo do caminho até o nó atual
        self.anterior  = anterior
        self.proximo   = proximo

class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, s, v1, v2, p):
        novo_no = No(p, s, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
        self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, s, v1, v2, p):

        novo_no = No(p, s, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
        self.tail = novo_no

    # INSERE NO FIM DA LISTA
    def inserePos_X(self, s, v1, v2, p):

        # se lista estiver vazia
        if self.head is None:
            self.inserePrimeiro(s,v1,v2,p)
        else:
            atual = self.head
            while atual.valor1 < v1:
                atual = atual.proximo
                if atual is None: break

            if atual == self.head:
                self.inserePrimeiro(s,v1,v2,p)
            else:
                if atual is None:
                    self.insereUltimo(s,v1,v2,p)
                else:
                    novo_no = No(p,s,v1,v2,None,None)
                    aux = atual.anterior
                    aux.proximo = novo_no
                    novo_no.anterior = aux
                    atual.anterior = novo_no
                    novo_no.proximo = atual


    # REMOVE NO INÍCIO DA LISTA
    def deletaPrimeiro(self):
        if self.head is None:
            return None
        else:
            no = self.head
            self.head = self.head.proximo
            if self.head is not None:
                self.head.anterior = None
            else:
                self.tail = None
            return no

    # REMOVE NO FIM DA LISTA
    def deletaUltimo(self):
        if self.tail is None:
            return None
        else:
            no = self.tail
            self.tail = self.tail.anterior
            if self.tail is not None:
                self.tail.proximo = None
            else:
                self.head = None
            return no

    def vazio(self):
        if self.head is None:
            return True
        else:
            return False

    def exibeLista(self):

        aux = self.head
        str = []
        while aux != None:
            str.append(aux.estado)
            aux = aux.proximo

        return str

    def exibeArvore(self):

        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho

    def exibeArvore1(self,s):


        atual = self.head
        while atual.estado != s:
            atual = atual.proximo

        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho


    def exibeArvore2(self, s, v1):

        atual = self.tail

        while atual.estado != s or atual.valor1 != v1:
            atual = atual.anterior

        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho


    def primeiro(self):
        return self.head

    def ultimo(self):
        return self.tail

class busca(object):

    def custo_uniforme(self, inicio, fim):

        l1 = lista()
        l2 = lista()
        visitado = []

        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                return caminho, atual.valor2

            ind = nos.index(atual.estado)
            for i in range(len(grafo[ind])):
                novo = grafo[ind][i][0]

                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + grafo[ind][i][1]  # custo do caminho
                v1 = v2 # f1(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo, v1 , v2, atual)
                    l2.inserePos_X(novo, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v2)
                        visitado.append(linha)

        return "Caminho não encontrado"

    def greedy(self, inicio, fim):

        l1 = lista()
        l2 = lista()
        visitado = []
        2
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                return caminho, atual.valor2

            ind = nos.index(atual.estado)
            for i in range(len(grafo[ind])):
                novo = grafo[ind][i][0]
                j = nos.index(novo)

                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + grafo[ind][i][1]  # custo do caminho
                v1 = h[j] # f2(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo, v1 , v2, atual)
                    l2.inserePos_X(novo, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v2)
                        visitado.append(linha)

        return "Caminho não encontrado"


    def a_estrela(self, inicio, fim):

        l1 = lista()
        l2 = lista()
        visitado = []

        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                return caminho, atual.valor1

            ind = nos.index(atual.estado)
            for i in range(len(grafo[ind])):
                novo = grafo[ind][i][0]
                j = nos.index(novo)

                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + grafo[ind][i][1]  # custo do caminho
                v1 = h[j] + v2 # f1(n) + f2(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo, v1 , v2, atual)
                    l2.inserePos_X(novo, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v2)
                        visitado.append(linha)

        return "Caminho não encontrado"



nos = ["ARAD", "BUCARESTE", "CRAIOVA", "DOBRETA", "EFORIE", "FAGARAS", "GIURGIU", "HIRSOVA", "IASI", "LUGOJ",
        "MEHADIA", "NEAMT", "ORADEA","PITESTI", "RIMINCU VILCEA", "SIBIU", "TIMISOARA", "URZICENI", "VASLUI",
        "ZERIND"]

grafo = [
        [["ZERIND",75], ["TIMISOARA",118], ["SIBIU",140]],
        [["URZICENI",85], ["PITESTI",101], ["GIURGIU",90], ["FAGARAS",211]],
        [["RIMINCU VILCEA",146], ["PITESTI",138], ["DOBRETA",120]],
        [["MEHADIA",75], ["CRAIOVA",120]],
        [["HIRSOVA",86]],
        [["SIBIU",99], ["BUCARESTE",211]],
        [["BUCARESTE",90]],
        [["URZICENI",98], ["EFORIE",86]],
        [["VASLUI",92], ["NEAMT",87]],
        [["TIMISOARA",111],["MEHADIA",70]],
        [["LUGOJ",70], ["DOBRETA",75]],
        [["IASI",87]],
        [["ZERIND",71], ["SIBIU",151]],
        [["RIMINCU VILCEA",97], ["CRAIOVA",138], ["BUCARESTE",101]],
        [["SIBIU",80], ["PITESTI",97], ["CRAIOVA",146]],
        [["RIMINCU VILCEA",80], ["ORADEA",151], ["FAGARAS",99], ["ARAD",140]],
        [["LUGOJ",111], ["ARAD",118]],
        [["VASLUI",142], ["HIRSOVA",98], ["BUCARESTE",85]],
        [["URZICENI",142], ["IASI",92]],
        [["ORADEA",71], ["ARAD",75]]
        ]

# HEURISTICA SERVE SOMENTE PARA DESTINO BUCARESTE
h = [366,0,160,242,161,178,77,151,226,244,241,234,380,98,193,253,329,80,199,374]


sol = busca()
caminho = []

caminho, custo = sol.custo_uniforme("ARAD","BUCARESTE")
print("Custo Uniforme: ",caminho[::-1],"\ncusto do caminho: ",custo)

caminho, custo = sol.greedy("ARAD","BUCARESTE")
print("\nGreedy: ",caminho[::-1],"\ncusto do caminho: ",custo)

caminho, custo = sol.a_estrela("ARAD","BUCARESTE")
print("\nA estrela: ",caminho[::-1],"\ncusto do caminho: ",custo)