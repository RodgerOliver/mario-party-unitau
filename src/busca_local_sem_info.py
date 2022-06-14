class No(object):
    def __init__(self, pai=None, estado=None, valor1=None, valor2=None, anterior=None, proximo=None):
        self.pai = pai
        self.estado = estado
        self.valor1 = valor1
        self.valor2 = valor2
        self.anterior = anterior
        self.proximo = proximo


class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, st, v1, v2, p):
        novo_no = No(p, st, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
            self.head = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
            self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, st, v1, v2, p):

        novo_no = No(p, st, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior = self.tail
        self.tail = novo_no

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

    # RETORNA O PRIMEIRO DA LISTA
    def primeiro(self):
        return self.head

    # RETORNA O ÚLTIMO DA LISTA
    def ultimo(self):
        return self.tail

    # VERIFICA SE LISTA ESTÁ VAZIA
    def vazio(self):
        if self.head is None:
            return True
        else:
            return False

    # EXIBE O CONTEÚDO DA LISTA
    def exibeLista(self):

        aux = self.head
        str = []
        while aux != None:
            temp = []
            temp.append(aux.estado)
            temp.append(aux.valor1)
            temp.append(aux.valor2)
            str.append(temp)
            aux = aux.proximo

        return str

    # EXIBE O CAMINHO ENCONTRADO
    def exibeCaminho(self):

        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        caminho = caminho[::-1]
        return caminho

    # EXIBE O CAMINHO ENCONTRADO (BIDIRECIONAL)
    def exibeCaminho1(self, valor):

        atual = self.head
        while atual.estado != valor:
            atual = atual.proximo

        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho


class busca(object):
    # BUSCA EM AMPLITUDE
    def amplitude(self, inicio, fim):

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaPrimeiro()
            # if atual is None: break

            ind = nos.index(atual.estado)

            # varre todos as conexões dentro do grafo a partir de atual
            for i in range(len(grafo[ind])):

                novo = grafo[ind][i]
                # pressuponho que não foi visitado
                flag = True

                # controle de nós repetidos
                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= (atual.valor1+1):
                            flag = False
                        else:
                            visitado[j][1] = atual.valor1+1
                        break

                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.valor1 + 1, 0, atual)
                    l2.insereUltimo(novo, atual.valor1 + 1, 0, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor1+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        # print("Fila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho

        return []

    # BUSCA EM PROFUNDIDADE
    def profundidade(self, inicio, fim):

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaUltimo()
            # if atual is None: break

            ind = nos.index(atual.estado)

            # varre todos as conexões dentro do grafo a partir de atual
            for i in range(len(grafo[ind])):

                novo = grafo[ind][i]
                # pressuponho que não foi visitado
                flag = True

                # controle de nós repetidos
                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= (atual.valor1+1):
                            flag = False
                        else:
                            visitado[j][1] = atual.valor1+1
                        break

                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.valor1+1, 0, atual)
                    l2.insereUltimo(novo, atual.valor1+1, 0, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor1+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        # print("Fila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho
        return []

    # BUSCA EM PROFUNDIDADE LIMITADA
    def prof_limitada(self, inicio, fim, limite):

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaUltimo()

            if atual.valor1 != limite:

                ind = nos.index(atual.estado)

                # varre todos as conexões dentro do grafo a partir de atual
                for i in range(len(grafo[ind])):

                    novo = grafo[ind][i]
                    # pressuponho que não foi visitado
                    flag = True

                    # controle de nós repetidos
                    for j in range(len(visitado)):
                        if visitado[j][0] == novo:
                            if visitado[j][1] <= (atual.valor1+1):
                                flag = False
                            else:
                                visitado[j][1] = atual.valor1+1
                            break

                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo, atual.valor1+1, 0, atual)
                        l2.insereUltimo(novo, atual.valor1+1, 0, atual)

                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.valor1+1)
                        visitado.append(linha)

                        # verifica se é o objetivo
                        if novo == fim:
                            caminho = []
                            caminho += l2.exibeCaminho()
                            # print("Fila:\n",l1.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            return caminho
        return []

    # BUSCA EM APROFUNDAMENTO ITERATIVO
    def aprof_iterativo(self, inicio, fim, max_lim):

        for limite in range(max_lim):
            # manipular a FILA para a busca
            l1 = lista()

            # cópia para apresentar o caminho (somente inserção)
            l2 = lista()

            # insere ponto inicial como nó raiz da árvore
            l1.insereUltimo(inicio, 0, 0, None)
            l2.insereUltimo(inicio, 0, 0, None)

            # controle de nós visitados
            visitado = []
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)

            while l1.vazio() == False:
                # remove o primeiro da fila
                atual = l1.deletaUltimo()

                if atual.valor1 != limite:

                    ind = nos.index(atual.estado)

                    # varre todos as conexões dentro do grafo a partir de atual
                    for i in range(len(grafo[ind])):

                        novo = grafo[ind][i]
                        # pressuponho que não foi visitado
                        flag = True

                        # controle de nós repetidos
                        for j in range(len(visitado)):
                            if visitado[j][0] == novo:
                                if visitado[j][1] <= (atual.valor1+1):
                                    flag = False
                                else:
                                    visitado[j][1] = atual.valor1+1
                                break

                        # se não foi visitado inclui na fila
                        if flag:
                            l1.insereUltimo(novo, atual.valor1 + 1, 0, atual)
                            l2.insereUltimo(novo, atual.valor1 + 1, 0, atual)

                            # marca como visitado
                            linha = []
                            linha.append(novo)
                            linha.append(atual.valor1+1)
                            visitado.append(linha)

                            # verifica se é o objetivo
                            if novo == fim:
                                caminho = []
                                caminho += l2.exibeCaminho()
                                # print("Fila:\n",l1.exibeLista())
                                #print("\nÁrvore de busca:\n",l2.exibeLista())
                                return caminho
        return []

    # BUSCA EM AMPLITUDE
    def bidirecional(self, inicio, fim):

        # manipular a FILA para a busca
        l1 = lista()
        l3 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()
        l4 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)
        l3.insereUltimo(fim, 0, 0, None)
        l4.insereUltimo(fim, 0, 0, None)

        # controle de nós visitados
        visitado1 = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado1.append(linha)

        visitado2 = []
        linha = []
        linha.append(fim)
        linha.append(0)
        visitado2.append(linha)

        primeiro = True

        while l1.vazio() == False and primeiro == True:
            # remove o primeiro da fila
            atual = l1.deletaPrimeiro()

            ind = nos.index(atual.estado)

            # varre todos as conexões dentro do grafo a partir de atual
            for i in range(len(grafo[ind])):

                novo = grafo[ind][i]
                # pressuponho que não foi visitado
                flag = True

                # controle de nós repetidos
                for j in range(len(visitado1)):
                    if visitado1[j][0] == novo:
                        if visitado1[j][1] <= (atual.valor1+1):
                            flag = False
                        else:
                            visitado1[j][1] = atual.valor1+1
                        break

                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.valor1 + 1, 0, atual)
                    l2.insereUltimo(novo, atual.valor1 + 1, 0, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor1+1)
                    visitado1.append(linha)

                    # verifica se é o objetivo
                    flag = False
                    for j in range(len(visitado2)):
                        if visitado2[j][0] == novo:
                            flag = True
                            break

                    if flag:
                        caminho = []
                        # print("Fila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        #print("\nÁrvore de busca:\n",l4.exibeLista())
                        caminho += l2.exibeCaminho()
                        caminho += l4.exibeCaminho1(novo)
                        return caminho

            primeiro = False

        while l3.vazio() == False and primeiro == False:
            # remove o primeiro da fila
            atual = l3.deletaPrimeiro()

            ind = nos.index(atual.estado)

            # varre todos as conexões dentro do grafo a partir de atual
            for i in range(len(grafo[ind])):

                novo = grafo[ind][i]
                # pressuponho que não foi visitado
                flag = True

                # controle de nós repetidos
                for j in range(len(visitado2)):
                    if visitado2[j][0] == novo:
                        if visitado2[j][1] <= (atual.valor1+1):
                            flag = False
                        else:
                            visitado2[j][1] = atual.valor1+1
                        break

                # se não foi visitado inclui na fila
                if flag:
                    l3.insereUltimo(novo, atual.valor1 + 1, 0, atual)
                    l4.insereUltimo(novo, atual.valor1 + 1, 0, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor2+1)
                    visitado2.append(linha)

                    # verifica se é o objetivo
                    flag = False
                    for j in range(len(visitado1)):
                        if visitado1[j][0] == novo:
                            flag = True
                            break

                    if flag:
                        caminho = []
                        # print("Fila:\n",l3.exibeLista())
                        #print("\nÁrvore de busca:\n",l4.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        caminho += l4.exibeCaminho()
                        caminho += l2.exibeCaminho1(novo)
                        return caminho[::-1]

                primeiro = False

        return []


"""
********************************************************************
                    PROBLEMA: MAPA DA ROMÊNIA
********************************************************************

nos = ["ARAD", "BUCARESTE", "CRAIOVA", "DOBRETA",
        "EFORIE", "FAGARAS", "GIORGIU", "HIRSOVA",
        "IASI", "LUGOJ", "MEHADIA", "NEAMT", "ORADEA",
        "PITESTI", "RIMNICU VILCEA", "SIBIU", "TIMISOARA",
        "URZICENI", "VASLUI", "ZERIND"]

# ORDEM DECRESCENTE
grafo = [
    ["ZERIND", "TIMISOARA", "SIBIU"],
    ["URZICENI", "PITESTI", "GIORGIU", "FAGARAS"],
    ["RIMNICU VILCEA", "PITESTI", "DOBRETA"],
    ["MEHADIA", "CRAIOVA"],
    ["HIRSOVA"],
    ["SIBIU", "BUCARESTE"],
    ["BUCARESTE"],
    ["URZICENI", "EFORIE"],
    ["VASLUI", "NEAMT"],
    ["TIMISOARA", "MEHADIA"],
    ["LUGOJ", "DOBRETA"],
    ["IASI"],
    ["ZERIND", "SIBIU"],
    ["RIMNICU VILCEA", "CRAIOVA", "BUCARESTE"],
    ["SIBIU", "PITESTI", "CRAIOVA"],
    ["RIMNICU VILCEA", "ORADEA", "FAGARAS", "ARAD"],
    ["LUGOJ", "ARAD"],
    ["VASLUI", "HIRSOVA", "BUCARESTE"],
    ["URZICENI", "IASI"],
    ["ORADEA", "ARAD"]
]


********************************************************************
                    PROBLEMA: VALE DO PARAÍBA
********************************************************************


nos = ["Ap","Ca","Cg","CJ","CP","Cr","Gu","Ja","Jc","Lo","ML",
        "NS","Pa","Pi","Ro","RS","SA","SJ","SL","Ta","Tr","Ub"]

# ORDEM DECRESCENTE
grafo = [
    ["Ro","Gu"],
    ["Ja","SJ","Ta"],
    ["Pa","Ub"],
    ["SA","Ta","Tr"],
    ["Cr","Lo"],
    ["CP"],
    ["Ap","Lo"],
    ["Ca","Pa","SJ"],
    ["SJ"],
    ["CP","Gu"],
    ["SA","SJ"],
    ["RS","SL"],
    ["Cg","Ja","SJ"],
    ["Ro","Ta","Tr"],
    ["Pi","Ap"],
    ["NS","SL","Ta"],
    ["CJ","ML","Ta","Tr"],
    ["Ca","Jc","ML","Pa","Ja"],
    ["Ub","Ta","NS","RS"],
    ["Ca","Tr","Pi","RS","CJ","SL","SA"],
    ["Ta","CJ","Pi","SA"],
    ["SL","Cg"]
]
"""

"""
********************************************************************
                    PROBLEMA: MARIO PARTY
********************************************************************
"""

nos = [
    "A", "B", "C", "D", "E", "F", "G", "H",
    "I", "J", "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T", "U", "V",
    "W", "X", "Y", "Z",
]

# ORDEM DESORDENADA
grafo = [
    ["C", "S", "R", "B"],
    ["P", "U", "G", "A"],
    ["D", "Z", "H", "A"],
    ["S", "R", "F"],
    ["P", "I", "X", "T"],
    ["D", "Z", "K", "T", "X"],
    ["B", "J", "V"],
    ["C", "K", "Y", "N"],
    ["E", "J", "U", "L", "M", "X"],
    ["G", "I", "W"],
    ["F", "H", "X", "L"],
    ["N", "I", "K", "X"],
    ["O", "W", "V", "I"],
    ["Y", "L", "O", "H"],
    ["N", "M"],
    ["B", "Q", "E"],
    ["R", "T", "P"],
    ["A", "Q", "D"],
    ["A", "Z", "C", "D"],
    ["Q", "F", "E"],
    ["B", "I", "E"],
    ["G", "W", "M"],
    ["J", "V", "M"],
    ["E", "I", "L", "F", "K"],
    ["N", "H"],
    ["S", "C", "F", "D"],
]


# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    sol = busca()
    caminho = []

    # DEFINIÇÃO DO PROBLEMA (Romênia)
    # origem, destino  = "ARAD", "LUGOJ"
    # DEFINIÇÃO DO PROBLEMA (Mario Party)
    origem, destino = "A", "O"

    caminho = sol.amplitude(origem, destino)
    print("\n*****AMPLITUDE*****\n", caminho)

    caminho = sol.profundidade(origem, destino)
    print("\n*****PROFUNDIDADE*****\n", caminho)

    lim = 2
    caminho = sol.prof_limitada(origem, destino, lim-1)
    print("\n***** PROFUNDIDADE LIMITADA ( L =", lim-1, ")*****\n", caminho)

    caminho = sol.prof_limitada(origem, destino, lim)
    print("\n*****PROFUNDIDADE LIMITADA ( L =", lim, ")*****\n", caminho)

    caminho = sol.prof_limitada(origem, destino, lim+4)
    print("\n*****PROFUNDIDADE LIMITADA ( L =", lim+4, ")*****\n", caminho)

    lim = len(nos)
    caminho = sol.aprof_iterativo(origem, destino, lim)
    print("\n*****APROFUNDAMENTO ITERATIVO*****\n", caminho)

    caminho = sol.bidirecional(origem, destino)
    print("\n*****BIDIRECIONAL*****\n", caminho)
