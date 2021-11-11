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
        f=int (input("Seleccione el archivo que desea cargar (1:distances5, 2:distances100, 3:distances:1000, 4:Salir de la aplicacion)\n"))
        matriz=0
        if f==1:
            matriz=cargarDatos("distances5")
        elif f==2:
            matriz=cargarDatos("distances100")
        elif f==3:
            matriz=cargarDatos("distances1000")
        elif f==4:
            vis=False
        if f!=4:
            print("matriz cargada correctamente")
            print("Cargando algorimos de caminos minimo\nPuede tardar un poco")    
            print(f"Warshall: {minim.warshall(matriz)}")
            print(f"Bellman: {minim.bellman(matriz)}")
    


main()

print(ft.fiesta(cargarDatos()))
