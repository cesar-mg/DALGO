import sys
import queue
import CaminosMinimosP1 as minim
import RecorridosP23 as recorridos


def CaminosCiudadKrustal(grafo):
    caminos = []
    ejes_agregados = 0
    ##Matriz para validar los ciclos posibles a generar.
    matriz_de_agregados = [[0]*len(grafo) for i in range(len(grafo))]
    ##Validamos que se agregen N arcos, para crear el MST
    while ejes_agregados < len(grafo):
        arco_minimo = sys.maxsize
        vertice1 = -1
        vertice2 = -1
        for i in range(len(grafo)):
            for j in range(len(grafo)):
                ##Buscamos el menor arco que no genere un ciclo.
                if not generanCiclo(i,j,matriz_de_agregados) and grafo[i][j] < arco_minimo:
                    arco_minimo = grafo[i][j]
                    vertice1 = i
                    vertice2 = j

        ## Agregamos el arco a la matriz de agregados.
        matriz_de_agregados[vertice1][vertice2] = 1
        matriz_de_agregados[vertice2][vertice1] = 1
        
        ## Agregamos la dupla o arco a nuestra lista de caminos minimos.
        caminos.append((vertice1, vertice2))
        ejes_agregados += 1
    return caminos
## Usamos el metodo dfs creado que nos manifiesta si exsite un ciclo.
def generanCiclo(i,j,matriz):
    grafo = matriz.copy()
    ## Suponemos que se crea el arco
    grafo[i][j] = 1
    grafo[j][i] = 1
    ciclo = recorridos.dfs(grafo, i)
    if "ciclo" in ciclo:
        for k in range(len(ciclo)):
            ## Recortamos el ciclo, tal que solo aparezcan los vertices que lo crean.
            if ciclo[k] == ciclo[len(ciclo -1)]:
                ciclo_recortado = ciclo[k:len(ciclo) -1]
                ## Retorna true si hay un ciclo con i y j dentro.
                return i in ciclo_recortado and j in ciclo_recortado
    return False
