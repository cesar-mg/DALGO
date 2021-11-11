import sys
import queue
def bellman(g:list):
    grafo=g
    visitados=[]
    sinVisitar=[]
    matrizRespuesta=[]
    sigVertices=[]
    sol=[]
    for x in range(len(g)):
        sinVisitar.append(x)
        matrizRespuesta.append([100000000]*3)
        matrizRespuesta[x][0]=x
        
    
    
    for origen in range(len(g)):
        sol.append(matrizRespuesta)
        i=origen
        j=0
        visitados=[]
        pesoActual=100000000
        if origen>0:
            matrizRespuesta=[]
            for x in range(len(g)):
                matrizRespuesta.append([100000000]*3)
                matrizRespuesta[x][0]=x
        while len(visitados)<=len(sinVisitar):
            visitados.append(sinVisitar[i])
            while j<len(g[i]):
                if i==origen:
                    matrizRespuesta[i][2]=0
                    matrizRespuesta[i][1]=i
                if grafo[i][j]!=-1:  
                    if matrizRespuesta[j][2]>grafo[i][j]+matrizRespuesta[i][2] and grafo[i][j]!=0: 
                        matrizRespuesta[j][2]=grafo[i][j]+matrizRespuesta[i][2]
                        matrizRespuesta[j][1]=i
                        sigVertices.append(j)
                j=j+1
            for w in sigVertices:
                if w not in visitados:
                    i=w
                    sigVertices.remove(i)
                    break
            j=0
    return(sol)

def warshall(grafo:list):
    i=0
    j=0
    k=0
    sol=[]
    for x in range(len(grafo)):
        sol.append([])
        for m in range(len(grafo[0])):
            sol[x].append(0)
    for k in range(len(grafo)):
        for i in range(len(grafo)):
            for j in range(len(grafo[i])):
                if grafo[i][j]==-1 and (grafo[i][k]!=-1 and grafo[k][j]!=-1) :
                    grafo[i][j]=grafo[i][k]+grafo[k][j]
                elif grafo[i][k]!=-1 and grafo[k][j]!=-1:    
                    grafo[i][j]=min(grafo[i][j],grafo[i][k]+grafo[k][j])
    return grafo

def dijkstra(grafo:list):
    solucion = []
    ## Realizamos dijkstra teniendo todos los vertices de origen.
    for i in range(len(grafo)):
        costo = [sys.maxsize for i in range(len(grafo))]
        visitados = [False for i in range(len(grafo))]
        costo[i] = 0

        ## Realizamos dijkstra.
        paso = 0
        while paso < len(grafo):

            ## Buscamos el indice con el costo menor NO visitado.
            indice_menor = 0
            minimo = sys.maxsize
            for vertice in range(len(grafo)):

                ## Verificamos que no este visitado y su costo sea menor al menor actual.
                if visitados[vertice] == False and costo[vertice] < minimo:
                    minimo = costo[vertice]
                    indice_menor = vertice

            
            ## Visitamos el vertice, es decir que continuamos el algoritmo en este.
            visitados[indice_menor] = True

            ## Validamos que los arcos del vertice actual acorten algun camino.
            indice_actual = 0
            while indice_actual < len(grafo):
                ## Validamos el arco. Si existe camino y no ha sido visitado.
                if visitados[indice_actual] == False and grafo[indice_menor][indice_actual] > 0:

                    ## Obtenemos el costo del camino nuevo.
                    camino_nuevo = costo[indice_menor] + grafo[indice_menor][indice_actual]

                    ## Verificamos si ahorra costo de un camino y acortamos en cuyo caso.
                    if  camino_nuevo < costo[indice_actual]:
                        costo[indice_actual] = camino_nuevo
                indice_actual += 1
            paso+=1

        ## Agregamos los costos minimos del vertice actual.
        solucion.append(costo)
    return solucion