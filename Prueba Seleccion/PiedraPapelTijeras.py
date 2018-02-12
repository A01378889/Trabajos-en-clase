#Autor: Felipe Gomez Portugal T
#Juego de piedra, papel o tijeras

from random import randint

def imprimir(juego):
    if juego==1: print("Piedra")
    elif juego==2:
        print("Papel")
    else:
        print("Tijeras")

def jugar(jugada):
    compu=randint(1,3)#numero aleatorio entre 1,3
    imprimir (compu)
    #ganar
    if jugada==1 and compu==3 or jugada== 2 and compu==1 or jugada==3 and compu==2:
        return "Ganas"
    #Empate
    elif jugada == compu:
        return "Empate"

    #Pierdes
    return "Pierdes"


def main():
    print("1-Piedra, 2-Papel, 3-Tijeras")
    jugador = int(input("Que quieres jugar: "))
    resultado = jugar(jugador)

    print("Resultado: ", resultado)

main()