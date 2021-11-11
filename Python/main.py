## Main

import os
import CaminosMinimosP1 as minim
import RecorridosP23 as rec

def cargarDatos():
    matriz = []
    with open(os.path.dirname(__file__) + '/Data/distances5.txt', 'r') as file:
        lineas = file.readlines()
        for linea in lineas:
            matriz.append(list(map(int, (linea.replace('\n','').split('\t')))))
        return matriz


print(minim.dijkstra(cargarDatos()))
print(minim.bellman(cargarDatos()))
print(minim.warshall(cargarDatos()))
