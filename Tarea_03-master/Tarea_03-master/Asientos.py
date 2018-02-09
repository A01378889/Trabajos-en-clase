#Autor: Felipe Gomez Portugal
#Preguntar cuantos asientos quieren comprar de cada tipo diferente e imprimir el total a pagar.

def calcularPago(asientosA, asientosB, asientosC):
    total = (asientosA*870) + (asientosB*650) + (asientosC*235)
    print("El costo total es: $", total)

def main():
    numeroBoletosA = input("Número de boletos de clase A: ")
    numeroBoletosB = input("Número de boletos de clase B: ")
    numeroBoletosC = input("Número de boletos de clase C: ")

    calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)



main()