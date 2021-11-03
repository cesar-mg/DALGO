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