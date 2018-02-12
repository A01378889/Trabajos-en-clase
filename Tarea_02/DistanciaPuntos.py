#Autor: Felipe Gomez Portugal
#Calcular distancia entre dos puntos
#import math math.sqrt

from math import sqrt

def distanciaPuntos(x1, y1, x2, y2):
    d = sqrt((x1-x2)**2 +(y1-y2)**2)
    return d

def main():
    x1 = int(input("Teclea x1: "))
    y1 = int(input("Teclea y1: "))
    x2 = int(input("Teclea x2: "))
    y2 = int(input("Teclea y2: "))

    distancia = distanciaPuntos(x1, y1, x2, y2)
    print("Distancia: ", distancia)
main()