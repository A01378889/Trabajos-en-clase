#Autores: Jossian Abimelec García Quijano, Felipe Gomez Portugal
#Calcula el area y precio de un terreno, dado su altura y bases, al igual que el precio por metro cuadrado.

a = int(input("Cual es la base de abajo: "))
b = int(input("Cual es la altura: "))
c = int(input("Cual es la base de arriba: "))

formula = int((a + (a+2*c))*b)/2

print ("Esta es el area: ",formula)

print ("El precio es:$",formula*3450)