#Autor: Felipe Gomez Portugal
#Calcular el total de una compra con impuestos

def calcularIF(cantidad):
    impuesto = cantidad * 0.16
    return impuesto

def calcularIE(cantidad):
    impuesto = cantidad * 0.03
    return impuesto

def calcularTotal(totalImpuestos, subtotal):
    return totalImpuestos + subtotal


def main():
    subtotal = int(input("Cual es el subtotal: "))
    impuestoFederal = calcularIF(subtotal)
    impuestoEstatal = calcularIE(subtotal)
    totalImpuestos = impuestoEstatal + impuestoFederal
    totalCompra = calcularTotal(totalImpuestos, subtotal)

    print("Subtotal: %.2f" % subtotal)
    print ("Impuesto federal: %.2f" % impuestoFederal)
    print("Impuesto estatal: %.2f" % impuestoEstatal)
    print("Impuestos: %.2f" %totalImpuestos)
    print("Total de la compra: %.2f" %totalCompra)


main()