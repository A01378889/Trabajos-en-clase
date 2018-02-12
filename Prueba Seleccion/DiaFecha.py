#Autor: Felipe Gomez Portugal T
#Un programa que imprimer el dia de la semana de cualquier fecha(calendaria gregoriano)

def calcularDia(dia,mes,anno):
    y0=anno- ((14-mes)//12)
    x=y0+(y0//4)-(y0//100)+(y0//400)
    m0=mes+12*((14-mes)//12)-2
    d0=(dia+x+((31*m0)//12))%7
    return d0

def calcularNombre(d0):
    if d0==0:
        nombreDia= "Domingo"
    elif d0==1:
        nombreDia= "Lunes"
    elif d0==2:
        nombreDia= "Martes"
    elif d0==3:
        nombreDia= "Miercoles"
    elif d0==4:
        nombreDia= "Jueves"
    elif d0==5:
        nombreDia= "Viernes"
    elif d0==6:
        nombreDia= "Sabado"
    return nombreDia


def main():
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    anno= int(input("Año: "))

    d0 = calcularDia(dia,mes,anno)
    diaSemana = calcularNombre(d0)

    print("El dia es: ",diaSemana)
main()