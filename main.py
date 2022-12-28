import pygame as pg
import sys, os
import numpy as np
from automata import *

rules = {
    0: 1, #'000': None,
    1: 1, #'001': None,
    2: 0, #'010': None,
    3: 0, #'011': None,
    4: 0, #'100': None,
    5: 0, #'101': None,
    6: 1, #'110': None,
    7: 1, #'111': None,
}

class Window():

    def __init__(self, n, size, ticks):
        self.n = n # matriz nxn
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
        cells = []
        x = 0
        y = 0
        limite_horizontal = self.HEIGHT
        limite_vertical = self.WIDTH
        s = self.CELL_SIZE
        val = False
        
        #celdas primera fila
        cells.append(Automata(0, 0, 1))
        cells.append(Automata(1, 1, 0))
        cells.append(Automata(0, 1, 1))
        cells.append(Automata(1, 1, 1))
        cells.append(Automata(1, 1, 1))
        cells.append(Automata(1, 1, 1))
        cells.append(Automata(1, 1, 1))
        cells.append(Automata(1, 1, 1))
        cells.append(Automata(1, 0, 1))
        cells.append(Automata(1, 0, 0))

        for i in range(self.n):
            """ if i != 0:
                cell = Automata(cells[i-1].get_state(), None, 1 if  val else 0)
                cells.append(cell)
                cells[i-1].set_rhn(cell.get_state())
                val = not val
            else:
                cell = Automata(0, None, 1) # primera celda
                cells.append(cell) """

            pg.draw.rect(
                self.pantalla, 
                self.colors.get(cells[i].get_state()),
                pg.rect.Rect(x, y, s, s)
            )
            x += s
        x = 0
        y = s
        #recorrer todas las filas
        for j in range(self.n-1):
            for i in range(self.n):
                cells[i].set_state(rules)
                pg.draw.rect(
                    self.pantalla, 
                    self.colors.get(cells[i].get_state()),
                    pg.rect.Rect(x, y, s, s)
                )
                if i >= 2:
                    cells[i-1].set_lhn(cells[i-2].get_state())
                    cells[i-1].set_rhn(cells[i].get_state())
                elif i == 1:
                    cells[i-1].set_rhn(cells[i].get_state())
                """ elif i == (self.n - 1):
                    cells[i].set_rhn(cells[0].get_state())
                    cells[0].set_lhn(cells[i].get_state()) """
                x += s
            x = 0
            y += s

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
    w = Window(10, (650, 650), 3)
    #w = Window(100, (1300, 1300 // 2), 3)
    w.run()