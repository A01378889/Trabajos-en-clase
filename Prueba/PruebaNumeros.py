#Autor: Felipe GPT
#Prueba numeros primos y perfectos

#Prueba si el numero es primo o no, dependiendo del numero de divisores.
def esPrimo(numero):
    cd = 0

    for pd in range(2,numero):                 #[2,numero-1]
        if numero%pd==0:
            cd += 1                            #cd = cd+1

    if cd==0:
        return True

    return False

#Prueba si un nuemro es perfecto o no.
def esPerfecto(numero):
    sumaDivisores = 0
    for pd in range(1,numero):
        if numero%pd == 0:
            sumaDivisores += pd
    if numero == sumaDivisores:
        return True
    return False

#Aporxima PI como la serie 1/1 - 1/3 + 1/5 ...1/n
def aproximaPi(n):
    suma=0   #sumatoria de las fracciones
    cf = 1
    for d in range (1,n+1,2):
        if cf%2==1:
            suma +=1/d
        else:
            suma-=1/d
        cf+=1
    return 4*suma
def main():
    '''for pp in range (1,21):
        print(pp,"Es primo?",esPrimo(pp))
    for pp in range (1,21):
        print(pp,"Es perfecto?",esPerfecto(pp) )'''
    '''for pp in range(1,21):
        if esPerfecto(pp):
            print(pp)'''
    print(aproximaPi(1000000))

main()