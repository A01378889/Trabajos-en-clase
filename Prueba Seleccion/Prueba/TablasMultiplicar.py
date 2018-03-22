def imprimirTabla(tabla):
    print("Tabla del", tabla)
    for factor in range(1,11):
        resultado = tabla*factor
        print("%d x %2d = %d"%(tabla, factor, resultado))

def main():
    for tabla in range(1,11):
       imprimirTabla(tabla)
main()