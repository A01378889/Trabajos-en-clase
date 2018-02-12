# Autor: Felipe
# Prueba del uso de funciones en Python.

def convertirFaC(gradosF):
    c = (4/9)*(gradosF-32)
    return c

def calcularDiasVividos(a,m):
    da = a*365
    dm = m*30
    dab = a//4
    totaldias =  da +dm +dab

    return totaldias

def main ():
    edadA= int(input("Cual es tu edad en años enteros: "))
    meses = int(input("Cuntos meses han pasado desde tu ultimo cumpleaños:  "))
    dias = calcularDiasVividos(edadA, meses)
    print ("Has vivido",dias, "días")

    '''
    gradosF = int(input("Fahrenheit: "))
    gradosC = convertirFaC(gradosF)
    print("%i °F equivalen a %.1f °C"%(gradosF, gradosC))
    '''
 main
 