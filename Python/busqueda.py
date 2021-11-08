def caminosMin(grafo:list,v:int):
    visitados=[]
    matrizRespuesta=[10000000]*len(grafo)
    residuo=[]
    total=len(grafo)
    visitados.append(v)
    matrizRespuesta[v]=0
    while len(visitados)>0:
        total=-1
        i=visitados[0]
        for j in range(len(grafo)):
            if grafo[i][j]!=-1 and grafo[i][j]!=0 :
                if j not in residuo:
                    visitados.append(j)
                if matrizRespuesta[j]>grafo[i][j]+matrizRespuesta[i] and grafo[i][j]!=0: 
                        matrizRespuesta[j]=grafo[i][j]+matrizRespuesta[i]
        residuo.append(visitados.pop(0))
        
    return matrizRespuesta
print(caminosMin([[0,90	,80	,-1	,-1],[15,0	,69	,48	,-1],[91,-1,0,	12,	39],[78,-1,	-1,	0,	36],[26,12,	39,	33,	0]],0))


    
