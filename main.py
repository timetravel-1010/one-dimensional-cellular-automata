import pygame as pg
import sys, os

n = 100 # matriz nxn
ANCHO = 1300
ALTO = ANCHO / 2#ANCHO
SIZE = ANCHO // n
ticks = 3
colors = {
    0: (0,0,0),
    1: (255,255,255), #blanco
}

def game(): 
    #configuración inicial de la pantalla
    def setup():
        global pantalla 
        pg.init()
        pantalla = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption('1D cellular automata')
        pantalla.fill((255,255,255)) 

    """ crear la cuadrícula """
    def grid():
        x = 0(255,255,255), #blanco
        y = 0
        limite_horizontal = ALTO
        limite_vertical = ANCHO
        for l in range(n):
            pg.draw.line(pantalla, (0,0,0), (x,0), (x, limite_horizontal))
            pg.draw.line(pantalla, (0,0,0), (0,y), (limite_vertical, y))
            x += SIZE
            y += SIZE


    
     # bucle infinito para mostrar en patalla todos los elementos gráficos.
    def mostrar_juego(): # resultado = [nodo5, nodo4, nodo3, nodo2, nodo1]
        
        while True:
            clock.tick(ticks) 

            for event in pg.event.get():
                if event.type == pg.QUIT: #para detener la ejecución al cerrar la ventana
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_p:
                        pass
            grid() #mostrar la cuadrícula
            pg.display.update()
            pg.display.flip() #actualizar el mundo para mostrar nuevos cambios.

    # Inicio
    setup() #pantalla
    clock = pg.time.Clock() #reloj para manipular la velocidad de la ejecución.
    #grid()
    mostrar_juego()
    pg.display.flip()

if '__main__' == __name__:
    game()