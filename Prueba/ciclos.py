import pygame


# Dimensiones de la pantalla
ANCHO = 640
ALTO = 480
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)

def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock()     # Para limitar los fps
    termina = False                 # Bandera para saber si termina la ejecución

    #cargar imagen
    imgTortuga = pygame.image.load("tortuga.png")
    xTortuga = 0
    imgFondo=pygame.image.load("fondo.jpg")
    imgBunny = pygame.image.load("bunny.png")
    while not termina:              # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        ventana.blit(imgFondo, (0, 0))
        ventana.blit(imgTortuga,(xTortuga,ALTO//2))
        if xTortuga<ANCHO-64:
            xTortuga+=1

        ventana.blit(imgBunny,(0, ALTO // 4))

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    # Después del ciclo principal
    pygame.quit()   # termina pygame



def main():
    dibujar()

main()