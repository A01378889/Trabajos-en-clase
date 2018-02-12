#Felipe Gomz Portugal
#Prueba de funciones en python
import turtle
def dibujarCuadro(longitud):
    turtle.forward(longitud)
    turtle.left(90)
    turtle.forward(longitud)
    turtle.left(90)
    turtle.forward(longitud)
    turtle.left(90)
    turtle.forward(longitud)
    turtle.left(90)

def dibujar5cuadros(longitud):
    turtle.fd(longitud)
    turtle.lt(90)
    turtle.fd(longitud*3)
    turtle.lt(90)
    turtle.fd(longitud)
    turtle.lt(90)
    turtle.fd(longitud)
    turtle.lt(90)
    turtle.fd(longitud * 3)
    turtle.lt(90)
    turtle.fd(longitud)
    turtle.lt(90)
    turtle.fd(longitud)
    turtle.lt(90)
    turtle.fd(longitud*3)
    turtle.lt(90)
    turtle.fd(longitud)
    turtle.lt(90)
    turtle.fd(longitud)
    turtle.lt(90)
    turtle.fd(longitud*3)
    turtle.lt(90)
    turtle.fd(longitud)
    turtle.lt(90)


def main():
    dibujar5cuadros(100)
    turtle.lt(45)
    dibujar5cuadros(100)

    turtle.done()

main() #Llamar a la función.