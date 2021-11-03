## Main

import os
def cargarDatos():
    matriz = []
    with open(os.path.dirname(__file__) + '/Data/distances100.txt', 'r') as file:
        lineas = file.readlines()
        for linea in lineas:
            matriz.append(list(map(int, (linea.replace('\n','').split('\t')))))
        return matriz

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



def dfs(matriz, inicio):
    ## Paso actual para verificar el desarrollo del ciclo. O reconstrucción de un orden topologico.
    pasoActual = 0
    pila = []
    respuesta = []
    ciclo = [inicio]

    ## Lista de pasoss en los que se visito el ciclo. Funciona tambien con lista de Trues para verificar si ya se paso por el mismo dos veces.
    visitados = [[] for i in range(0,len(matriz))]
    pila.append(inicio)
    visitados[inicio] = [pasoActual]

    while len(pila) > 0:
        siguiente = pila.pop()
        ## Se mete al orden unicamente si no se ha metido previamente.
        if len(visitados[siguiente]) < 2:
            respuesta.append(siguiente)

        for i in range(0,len(matriz)):
            ## Verificamos que exista camino y no se haya visitado dos veces previamente.
            if  0!= matriz[siguiente][i] != -1 and len(visitados[i]) < 2:
                pasoActual+=1 
                pila.append(i)
                ciclo.append(i)
                visitados[i].append(pasoActual)

                ## Si se visita dos veces y faltan vertices, significa que hay un ciclo. En el or verificamos que el ultimo nodo no complete un ciclo.
                if len(visitados[i]) == 2 and (pasoActual < len(matriz) or ciclo[0] == ciclo[len(ciclo) - 1]):
                    return 'Existe el siguiente ciclo:',ciclo
    return 'Hay un orden topologico:',respuesta

print(f"Bellman: {bellman(cargarDatos())}")
print(f"Warshall: {warshall(cargarDatos())}")
