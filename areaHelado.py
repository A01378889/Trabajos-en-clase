#Autor:Felipe Gomez
#Calcular el área de un triangulo mas la mitad de un circulo.

radio = int(input("¿Cual es el radio?: "))
altura = int(input("¿Cual es la altura?: "))

area = (3.141592*radio**2) / 2 +radio*altura

print ("El area es: ", area)