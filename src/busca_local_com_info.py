import libs as lib

# ROTINA PARA GERAR O AMBIENTE DO PROBLEMA
def gerar_ambiente(n, minimo, maximo):

    mat = lib.np.zeros((n, n), int)

    for j in range(n):
        for k in range(n):
            if j != k:
                mat[j][k] = lib.rd.randint(minimo, maximo)

    return mat

# ROTINA PARA GERAR O AMBIENTE DO PROBLEMA
def solucao_inicial(n):
    s = lib.np.zeros(n, int)

    for i in range(n):
        s[i] = i

    lib.rd.shuffle(s)

    return s

# ROTINA PARA CALCULAR O CUSTO DO CAMINHO
def avalia(n, s, mat):
    v = 0

    for i in range(n-1):
        v += mat[s[i]][s[i+1]]

    v += mat[s[n-1]][s[0]]

    return v

# ROTINA PARA GERAR SUCESSORES PARA SUBIDA DE ENCOSTA
def sucessores(n, atual, va, mat):
    melhor = lib.cp.deepcopy(atual)
    vmelhor = va

    c = lib.rd.randint(0, n-1)

    for i in range(n):
        aux = lib.cp.deepcopy(atual)

        x = aux[i]
        aux[i] = aux[c]
        aux[c] = x

        vaux = avalia(n, aux, mat)

        if vaux < vmelhor:
            melhor = lib.cp.deepcopy(aux)
            vmelhor = vaux

    return melhor, vmelhor

# ROTINA PARA GERAR SUCESSORES PARA TÊMPERA SIMULADA
def sucessores1(n, atual, mat):
    aux = lib.cp.deepcopy(atual)

    c1 = lib.rd.randint(0, n-1)
    c2 = lib.rd.randint(0, n-1)

    x = aux[c1]
    aux[c1] = aux[c2]
    aux[c2] = x

    vaux = avalia(n, aux, mat)

    return aux, vaux

# ROTINA SUBIDA DE ENCOSTA
def encosta(n, si, vi, mat):
    atual = lib.cp.deepcopy(si)
    va = vi
    while True:
        novo, vn = sucessores(n, atual, va, mat)
        if vn >= va:
            return atual, va
        else:
            atual = novo
            va = vn

# ROTINA SUBIDA DE ENCOSTA COM TENTATIVAS
def encosta_alt(n, si, vi, mat, tmax):
    t = 0
    atual = lib.cp.deepcopy(si)
    va = vi
    while True:
        novo, vn = sucessores(n, atual, va, mat)
        if vn >= va:
            if t <= tmax:
                t = t + 1
            else:
                return atual, va
        else:
            atual = novo
            va = vn
            t = 0

# ROTINA TÊMPERA SIMULADA
def tempera(n, si, vi, mat, t_max, t_min, fr):
    t = t_max
    atual = lib.cp.deepcopy(si)
    va = vi
    while t > t_min:
        novo, vn = sucessores1(n, atual, mat)
        de = vn - va
        if de < 0:
            atual = novo
            va = vn
        else:
            ale = lib.rd.uniform(0, 1)
            aux = lib.ma.exp(-de/t)
            if ale < aux:
                atual = novo
                va = vn
            t = t*fr
    return atual, va
