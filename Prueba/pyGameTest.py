# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame


# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    # Dimensiones de la pantalla
    ANCHO = 640
    ALTO = 480
    # Colores
    BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
    VERDE_BANDERA = (0, 122, 0)
    ROJO = (255, 0, 0)

    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock()     # Para limitar los fps
    termina = False                 # Bandera para saber si termina la ejecución

    while not termina:              # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        c=1
        for y in range(30,ALTO+60,60):
            for x in range(30,ANCHO+60,60):
                if c%2==1:
                    pygame.draw.circle(ventana, ROJO, (x,y), 30)
                else:
                    pygame.draw.circle(ventana,ROJO,(x,y),30,2)
                c+=1
            c+=1

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    # Después del ciclo principal
    pygame.quit()   # termina pygame


def main():
    dibujar()


main()