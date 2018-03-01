import turtle


def dibujarEspiral():
    turtle.speed(0)
    for longitud in range (5,801,5):
        turtle.forward(longitud)
        turtle.left(90)
        turtle.forward(longitud)
        turtle.left(90)



def main():
    dibujarEspiral()
    turtle.done()

main()