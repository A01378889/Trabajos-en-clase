#Autor: Felipe Gomez Portugal T
#

def calcularEstado(temperatura):
    if temperatura>=100:
        estado="Vapor"
    elif temperatura>=50 and temperatura:
        estado="Muy Caliente"
    elif temperatura>=30:
        estado="Caliente"
    elif temperatura>20:
        estado="Tibia"
    elif temperatura>=0:
        estado="Fria"
    else:
        estado="Congelada"
    return estado


def main():
    temperatura = int(input("Temperatura del agua: "))

    estado = calcularEstado(temperatura)

    print(estado)

main()