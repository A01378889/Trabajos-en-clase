import math
def calcularRaiz(a):
    x=a/2
    while math.fabs (x*x - a) >0.00001:
        print (x)
        x=(x+a/x)/2
    return x


def main():
    a = int(input("teclea a: "))
    raiz = calcularRaiz(a)
    print(raiz)
main()