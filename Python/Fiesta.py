## Se intenta organizar dos reuniones dado un grafo de amistades donde
## 1 representa amigos. -1 Peleados. y 0 Misma persona.

def fiesta(grafo):
    viernes = [0]
    sabado = []
    excluidos_a_la_85 = []
    act = 1
    while act < len(grafo):
        agregado = False
        segundo_grupo = False

        ## Verifica si hay peleas entre miembros del primer grupo.
        for i in viernes:
            ## Se valida y notifica la pelea.
            if grafo[act][i] == -1:
                segundo_grupo = True
        ## En cuyo caso no hayan peleas se agrega.
        if segundo_grupo == False:
            agregado = True
            viernes.append(act)

        ## Si hay peleas se valida en el segundo grupo.
        elif segundo_grupo == True:
            for j in sabado:
                ## Si hay peleas en este caso tambien, se agrega a un grupo de excluidos de las fiestas.
                if grafo[act][j] == -1:
                    agregado = True
                    excluidos_a_la_85.append(act)

        ## Si no se agrego al grupo de excluidos es por que se puede agregar al grupo de la segunda fiesta.    
        if agregado == False:
            sabado.append(act)
        act+=1
    return viernes, sabado, excluidos_a_la_85
