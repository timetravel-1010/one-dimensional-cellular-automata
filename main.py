import pygame as pg
import sys, os
import numpy as np
from automata import *


class Window():

    def __init__(self, n, size, ticks):
        self.n = 100 # matriz nxn
        self.WIDTH = size[0] #1300
        self.HEIGHT = size[1] #WIDTH / 2#WIDTH
        self.CELL_SIZE = self.WIDTH // n
        self.ticks = ticks
        self.colors = {
            0: (0,0,0),
            1: (255,255,255), #blanco
        }
        #self.pantalla = None
        self.setup()
        wordd = [[]]

    def setup(self):
        pg.init()
        self.pantalla = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption('1D cellular automata')
        self.pantalla.fill((255,255,255)) 
        self.clock = pg.time.Clock() #reloj para manipular la velocidad de la ejecución.


    """ crear la cuadrícula """
    def grid(self):
        world = []
        x = 0
        y = 0
        limite_horizontal = self.HEIGHT
        limite_vertical = self.WIDTH
        s = self.CELL_SIZE

        cell = Automata(None, None, 0) # primera celda
        world.append(cell)
        
        for i in range(self.n):
            r = pg.rect.Rect(x, y, s, s)
            pg.draw.rect(
                self.pantalla, 
                self.colors.get(world[i].get_state()),
                r
            )
            x += s
            cell = Automata(world[i].get_state(), None, 0)
            cell.set_state()
            world.append(cell)

        x = 0
        y = 0

        for l in range(self.n):
            pg.draw.line(self.pantalla, (128,128,128), (x,0), (x, limite_horizontal))
            pg.draw.line(self.pantalla, (128,128,128), (0,y), (limite_vertical, y))
            x += self.CELL_SIZE
            y += self.CELL_SIZE


    def run(self):     
        while True:
            self.clock.tick(self.ticks) 

            for event in pg.event.get():
                if event.type == pg.QUIT: #para detener la ejecución al cerrar la ventana
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_p:
                        pass
            self.grid() #mostrar la cuadrícula
            pg.display.update()
            pg.display.flip() #actualizar el mundo para mostrar nuevos cambios.


if '__main__' == __name__:
    w = Window(100, (1300, 1300 // 2), 3)
    w.run()