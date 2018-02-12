#Autor: Felipe Gomez Portugal
#Un programa que pida el numero de dia (0-6) e imprime el nombre del dia de la semana, 0-Domingo...6-Sabado

def main():
    numero = int(input("Telea el numero de dia:"))
    if numero ==0:
        print("Domingo")
    elif numero == 1:
        print("Lunes")
    elif numero == 2:
        print("Martes")
    elif numero == 3:
        print("Miercoles")
    elif numero == 4:
        print("Jueves")
    elif numero == 5:
        print("Viernes")
    elif numero == 6:
        print("Sabado")
    else:
        print("Error, el dia no existe")
main()
