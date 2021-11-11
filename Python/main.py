## Main

import os
import CaminosMinimosP1 as minim
import RecorridosP23 as rec
import Fiesta as ft

def cargarDatos(archivo:str):
    matriz = []
    with open(os.path.dirname(__file__) + f'/Data/{archivo}.txt', 'r') as file:
        lineas = file.readlines()
        for linea in lineas:
            matriz.append(list(map(int, (linea.replace('\n','').split('\t')))))
        return matriz
    
def main():
    vis=True
    while vis==True: 
        f=int (input("Seleccione el archivo que desea cargar (1:distances5, 2:distances100, 3:distances1000, 4:distancesDisconnected, 5:distancesTopo, 6:Salir de la aplicacion)\n"))
        matriz=0
        if f==1:
            matriz=cargarDatos("distances5")
        elif f==2:
            matriz=cargarDatos("distances100")
        elif f==3:
            matriz=cargarDatos("distances1000_202110")
        elif f==4:
            matriz=cargarDatos("distancesDisconnected")
            print(f"Componentes Desconectados{rec.bfs(matriz)}")
        elif f==5:
            matriz=cargarDatos("distancesTopo")
            vertice=int(input("ingrese el vertice desde el que desea hacer la busqueda:\n"))
            print(f"Orden topologico en la matriz {rec.dfs(matriz,vertice)}")
        elif f==6:
            vis=False
        if f!=4 and f!=5 and f!=6:
            print("matriz cargada correctamente")
            print("Cargando algorimos de caminos minimo\nPuede tardar un poco")    
            print(f"Warshall: {minim.warshall(matriz)}")
            print(f"Bellman: {minim.bellman(matriz)}")


main()

print(ft.fiesta(cargarDatos()))
