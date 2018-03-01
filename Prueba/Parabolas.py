#
#
import pygame
from random import randint

                                            # Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
                                            # Colores
BLANCO = (255, 255, 255)                    # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
AZUL = (28, 79, 114)


                                            #Estructura básica de un programa que usa pygame para dibujar
def dibujarArco(ventana):
    for x in range(ANCHO/2, ANCHO+1,10):
        y = x - ANCHO/2 + 10
        colorAzar = (randint(0,255),randint(0,255) ,randint(0,255))
        pygame.draw.line(ventana, colorAzar, (x-ANCHO//2, ALTO//2),(ANCHO//2,y+ALTO//2))
def dibujar():

                                            # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock()             # Para limitar los fps
    termina = False                         # Bandera para saber si termina la ejecución

    while not termina:                      # Ciclo principal
                                            # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

                                            # Borrar pantalla
        ventana.fill(BLANCO)

                                            # Dibujar, aquí haces todos los trazos que requieras


        pygame.display.flip()               # Actualiza trazos
        reloj.tick(40)                      # 40 fps

                                            # Después del ciclo principal
    pygame.quit()                           # termina pygame

def main():


main()