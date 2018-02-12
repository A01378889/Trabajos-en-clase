#Autor: Felipe Gomez Portugal
#Calcular distancias y tiempos

def calcularDistancia(velocidad, tiempo):
    return velocidad * tiempo


def calcularTiempo(velocidad, distancia):
    return distancia/velocidad


def main():
    velocidad = int(input("Velocidad: "))
    d7 = calcularDistancia(velocidad, 7)
    d45 = calcularDistancia()
    t = calcularTiempo(velocidad, 437)

    print(d7)
    print(d45)
    print(t)

    main()