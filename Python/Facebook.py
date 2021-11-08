
def facebook(grafo:list):
    #decimos que el grafo es una matriz que marca con 1 si hay una relacion de amistad entre 2 personas, -1 si no lo hay, y 0 si se encuentran con ellos mismos
    i=0
    j=0
    k=0
    sol=[]
    for k in range(len(grafo)):
        for i in range(len(grafo)):
            for j in range(len(grafo[i])):
                #se aplica un algoritmo similar a Floyd-warshall
                if grafo[i][j]==-1 and (grafo[i][k]!=-1 and grafo[k][j]!=-1): #El nodo i no tiene una conexion directa con el nodo j, pero si hay una conexion con el nodo intermedio k
                    #El camino entre j e i se vuelve la cantidad de nodos, incluyendo el destino, que son cruzados
                    grafo[i][j]=grafo[i][k]+grafo[k][j]
                elif grafo[i][k]!=-1 and grafo[k][j]!=-1:
                    #se decide el camino con menos nodos intermedios entre el camino que ya se encontro, y el camino usando el vertice intermedio k    
                    grafo[i][j]=min(grafo[i][j],grafo[i][k]+grafo[k][j])
    for x in range(len(grafo)):
        for m in range(len(grafo[x])):
            #verificamos que los caminos entre cada par de vertices del grafo sea menor a 7
            if grafo[x][m]>6:
                #si se encuentra que un camino es igual o mayor a 7, se retorna false, pues se incumpliria la ley de los 6 grados de separacion
                return False
    return True
sol=[[0	,1	,-1	,1	,-1,1,-1],[1	,0	,1	,-1,	-1,-1,-1],[-1	,1	,0	,1	,1,1,-1],[1,	-1,	1,	0	,-1,-1,1],[-1,	-1,	1,	-1,	0,1,-1],[1,	-1,	1,	-1,	1,0,-1],[-1,	-1,	-1,	1,	-1,-1,0]]
print(facebook(sol))