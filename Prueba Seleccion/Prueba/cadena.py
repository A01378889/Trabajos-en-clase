
def invertir(lista):
    resultado = []
    for indice in range(-1,-len(lista)-1,-1):
        resultado.append(lista[indice])
    return resultado

def quitarEspacios(lista):
    sinEspacios = []

    for dato in lista:
        if dato!=' ':
            sinEspacios.append(dato)
    return sinEspacios

def main():
    cadena = input("Teclea una cadena: ")
    cadena = cadena.upper()
    listaOriginal = list(cadena)
    print(listaOriginal)

    sinEspacios =  quitarEspacios(listaOriginal)
    print(sinEspacios)

    alReves = invertir(sinEspacios)
    print(alReves)

    if sinEspacios==alReves:
        print("Si es palindromo")
    else:
        print("No es palindromo")

main()