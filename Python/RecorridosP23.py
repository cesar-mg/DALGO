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