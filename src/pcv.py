# problema do cacheiro viajante
# implementação dos algoritmos de busca local com info
import busca_local_com_info as busca

# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    N = 8    # Total de pontos do grafo
    MIN = 5   # Limites mínimos da rotina RANDINT
    MAX = 25  # Limites máximos da rotina RANDINT

    # CONFIGURAÇÃO DO AMBIENTE
    m = busca.gerar_ambiente(N, MIN, MAX)
    #print("\n**** Matriz Custo *****\n",m)

    # BUSCA LOCAL
    si = busca.solucao_inicial(N)
    #print("\nSolução Inicial: ",si)
    vi = busca.avalia(N, si, m)
    print("Custo da solução inicial: ", vi)

    sf, vf = busca.encosta(N, si, vi, m)
    #print("\nSubida de Encosta: ",sf)
    print("Custo da solução - subida de encosta: ", vf)

    nt = int(N*0.1)
    sf, vf = busca.encosta_alt(N, si, vi, m, nt)
    #print("\nSubida de Encosta com Tentativas: ",sf)
    print("Custo da solução - subida de encosta com ", nt, " tentativa (5): ", vf)
    print("Ganho: ", (vi-vf)*100/vi)

    nt = int(N/2)
    sf, vf = busca.encosta_alt(N, si, vi, m, nt)
    #print("\nSubida de Encosta com Tentativas: ",sf)
    print("Custo da solução - subida de encosta com ", nt, " tentativa (5): ", vf)
    print("Ganho: ", (vi-vf)*100/vi)

    nt = N
    sf, vf = busca.encosta_alt(N, si, vi, m, nt)
    #print("\nSubida de Encosta com Tentativas: ",sf)
    print("Custo da solução - subida de encosta com ", nt, " tentativa (5): ", vf)
    print("Ganho: ", (vi-vf)*100/vi)

    sf, vf = busca.tempera(N, si, vi, m, 400, 0.1, 0.8)
    #print("\nTêmpera Simulada: ",sf)
    print("Custo da solução - têmpera: ", vf)
    print("Ganho: ", (vi-vf)*100/vi)

    sf, vf = busca.tempera(N, si, vi, m, 400, 0.01, 0.8)
    #print("\nTêmpera Simulada: ",sf)
    print("Custo da solução - têmpera: ", vf)
    print("Ganho: ", (vi-vf)*100/vi)

    sf, vf = busca.tempera(N, si, vi, m, 400, 0.01, 0.9)
    #print("\nTêmpera Simulada: ",sf)
    print("Custo da solução - têmpera: ", vf)
    print("Ganho: ", (vi-vf)*100/vi)
