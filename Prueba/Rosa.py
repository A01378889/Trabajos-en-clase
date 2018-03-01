import pygame

def dibujarRosa(venatna, m, k):
    for alfa in range(80, 369, 1):
        alfaRad = radians(alfa)
        r = m * cos(k*alfaRad)
        x = int(r*cos(alfaRad))+ANCHO//2
        y = ALTO//2 -int(r*sin(alfaRad))
        colorAzar = (randint(0, 255), randint(0, 255), randint(0, 255))
        pygame.draw.circle(ventan, ROJO, (x,y), 1)


def dibujar():
    ventana.fill(BLANCO)+
    dibujarRosa(ventana, 300, 3)
    pygame.display.flip()
    reloj.tick(40)

    pygame.quit()
def main():
    k = int(input("Valor de k: "))
    while k!=0:
        dibujar(k)
        k = int(input("Valor de k: "))

main()