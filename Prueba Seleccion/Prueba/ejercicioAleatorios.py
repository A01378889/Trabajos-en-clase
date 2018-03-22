from random import randint

def generarLista(n):
    lista = []

    for k in range (n):
        azar = randint(0,255)
        lista.append(azar)
    return lista


def contarPares(lista):
    numPares = 0

    for numero in lista:
        if numero%2==0:
            numPares += 1 #numPares = numPares + 1

    return numPares

def menu():
    print("1. Generar lista aleatoria.")
    print("2. Contar pares.")
    print("3. Salir.")
    opcion = int(input("Opcion: "))


def main():
    lista = []

    opcion = menu() #fix me

    while opcion !=3: #no quiere salir
        if opcion ==1:
            n = int(input("Cuantos valores quieres generar? "))
            lista = generarLista(n)
            print(lista)
        elif opcion == 2:
            nPares = contarPares(lista)
            print(lista)
            print("Hay", nPares,"pares en la lista")
        else:
            print("Error, selecciona una opcion correcta")

        opcion = menu() #fix me
main()