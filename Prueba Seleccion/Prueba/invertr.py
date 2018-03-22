def invertir(lista):
    alReves = []
    for k in range(len(lista)-1,-1,-1):
        alReves.append(lista[k])
    return alReves

def main():
    lista = []
    dato = int(input("teclea el valor [-1 termina]"))
    while dato !=-1:
        lista.append(dato)
        dato=int(input("Teclea el valor [-1 termina]"))

        print (lista, dato)