import pygame as pg
import sys, os
import numpy as np
import random

from automata import *

rules = {
    0: 0, #'000': None,
    1: 0, #'001': None,
    2: 0, #'010': None,
    3: 0, #'011': None,
    4: 0, #'100': None,
    5: 0, #'101': None,
    6: 0, #'110': None,
    7: 0, #'111': None,
}


class Window():

    def __init__(self, n, size, ticks):
        self.n = n # matriz nxn
        self.EXTRA_HEIGHT = 50
        self.HEIGHT = size[1]
        self.TOTAL_HEIGHT = size[1] + self.EXTRA_HEIGHT#1300
        self.WIDTH = size[0]
        self.CELL_SIZE = self.WIDTH // n
        self.cell_size = self.WIDTH // n, self.HEIGHT // n 
        self.ticks = ticks
        self.colors = {
            0: (0,0,0),
            1: (255,255,255), #blanco
            2: (125,125,125), #gris
        }
        #self.pantalla = None
        self.setup()
        self.cells = []
        self.static_cells = []
        self.out = []


    def setup(self):
        pg.init()
        self.pantalla = pg.display.set_mode((self.WIDTH, self.TOTAL_HEIGHT))
        pg.display.set_caption('1D cellular automata')
        self.pantalla.fill((255,255,255)) 
        self.clock = pg.time.Clock() #reloj para manipular la velocidad de la ejecución.

    def showCells(self):
        s = self.CELL_SIZE
        cs = self.cell_size
        x = 0
        #y = 0
        y = self.EXTRA_HEIGHT
        val = False
        
        #celdas primera fila
        """ self.cells.append(Automata(0, 0, 1))
        self.cells.append(Automata(1, 1, 0))
        self.cells.append(Automata(0, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 0, 1))
        self.cells.append(Automata(1, 0, 0))
        
        self.cells.append(Automata(0, 0, 1))
        self.cells.append(Automata(1, 1, 0))
        self.cells.append(Automata(0, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 0, 1))
        self.cells.append(Automata(1, 0, 0))
        self.cells.append(Automata(0, 0, 1))
        self.cells.append(Automata(1, 1, 0))
        self.cells.append(Automata(0, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 0, 1))
        self.cells.append(Automata(1, 0, 0))
        self.cells.append(Automata(0, 0, 1))
        self.cells.append(Automata(1, 1, 0))
        self.cells.append(Automata(0, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 0, 1))
        self.cells.append(Automata(1, 0, 0))
        self.cells.append(Automata(0, 0, 1))
        self.cells.append(Automata(1, 1, 0))
        self.cells.append(Automata(0, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 0, 1))
        self.cells.append(Automata(1, 0, 0))
        self.cells.append(Automata(0, 0, 1))
        self.cells.append(Automata(1, 1, 0))
        self.cells.append(Automata(0, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 0, 1))
        self.cells.append(Automata(1, 0, 0))
        self.cells.append(Automata(0, 0, 1))
        self.cells.append(Automata(1, 1, 0))
        self.cells.append(Automata(0, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 0, 1))
        self.cells.append(Automata(1, 0, 0))
        self.cells.append(Automata(0, 0, 1))
        self.cells.append(Automata(1, 1, 0))
        self.cells.append(Automata(0, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 0, 1))
        self.cells.append(Automata(1, 0, 0))
        self.cells.append(Automata(0, 0, 1))
        self.cells.append(Automata(1, 1, 0))
        self.cells.append(Automata(0, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 0, 1))
        self.cells.append(Automata(1, 0, 0))
        self.cells.append(Automata(0, 0, 1))
        self.cells.append(Automata(1, 1, 0))
        self.cells.append(Automata(0, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 1, 1))
        self.cells.append(Automata(1, 0, 1))
        self.cells.append(Automata(1, 0, 0)) """
 
        for i in range(self.n):
            if i != 0:
                cell = Automata(self.cells[i-1].getState(), 0, random.randint(0, 1))
                self.cells.append(cell)
                self.cells[i-1].set_rhn(cell.getState())
            else:
                cell = Automata(0, 0, random.randint(0, 1)) # primera celda
                self.cells.append(cell)

            pg.draw.rect(
                self.pantalla, 
                self.colors.get(self.cells[i].getState()),
                pg.rect.Rect(x, y, s, s)#, cs[0], cs[1])
            )
            x += s
        x = 0
        y += s
        #recorrer todas las filas
        """ for j in range(self.n-1):
            for i in range(self.n):
                self.cells[i].setState(rules)
                pg.draw.rect(
                    self.pantalla, 
                    self.colors.get(self.cells[i].getState()),
                    pg.rect.Rect(x, y, s, s)#, cs[0], cs[1])
                )
                if i >= 2:
                    self.cells[i-1].set_lhn(self.cells[i-2].getState())
                    self.cells[i-1].set_rhn(self.cells[i].getState())
                elif i == 1:
                    self.cells[i-1].set_rhn(self.cells[i].getState())
                x += s
            x = 0
            y += s """

    def showRules(self):

        s = self.CELL_SIZE
        x = 0
        #y = 0
        y = s
        val = False

        sc = []
        sc.extend([2]*24)
        sc.extend([0, 0, 0])
        sc.extend([2]*4)
        sc.extend([0, 0, 1])
        sc.extend([2]*4)
        sc.extend([0, 1, 0])
        sc.extend([2]*4)
        sc.extend([0, 1, 1])
        sc.extend([2]*4)
        sc.extend([1, 0, 0])
        sc.extend([2]*4)
        sc.extend([1, 0, 1])
        sc.extend([2]*4)
        sc.extend([1, 1, 0])
        sc.extend([2]*4)
        sc.extend([1, 1, 1])
        sc.extend([2]*24)

        self.out.extend([2]*25)
        self.out.append(rules[0])
        self.out.extend([2]*6)
        self.out.append(rules[1])
        self.out.extend([2]*6)
        self.out.append(rules[2])
        self.out.extend([2]*6)
        self.out.append(rules[3])
        self.out.extend([2]*6)
        self.out.append(rules[4])
        self.out.extend([2]*6)
        self.out.append(rules[5])
        self.out.extend([2]*6)
        self.out.append(rules[6])
        self.out.extend([2]*6)
        self.out.append(rules[7])
        self.out.extend([2]*25)

        for i in range(self.n):
            pg.draw.rect(
                self.pantalla, 
                self.colors.get(2),
                pg.rect.Rect(x, 0, s, s)#, cs[0], cs[1])
            )
            pg.draw.rect(
                self.pantalla, 
                self.colors.get(sc[i]),
                pg.rect.Rect(x, s, s, s)#, cs[0], cs[1])
            )
            pg.draw.rect(
                self.pantalla, 
                self.colors.get(self.out[i]),
                pg.rect.Rect(x, 2*s, s, s)#, cs[0], cs[1])
            )
            pg.draw.rect(
                self.pantalla, 
                self.colors.get(2),
                pg.rect.Rect(x, 3*s, s, s)#, cs[0], cs[1])
            )
            x += s


    """ crear la cuadrícula """
    def grid(self):
        x = 0
        y = 0
        #y = self.EXTRA_HEIGHT
        limite_horizontal = self.WIDTH 
        limite_vertical = self.WIDTH

        for l in range(self.n):
            pg.draw.line(self.pantalla, (128,128,128), (x,0), (x, limite_horizontal)) #lineas verticales
            pg.draw.line(self.pantalla, (128,128,128), (0,y), (limite_vertical, y)) #lineas horizontales
            
            #pg.draw.line(self.pantalla, (128,128,128), (x,self.EXTRA_HEIGHT), (x, limite_horizontal)) 
            #pg.draw.line(self.pantalla, (128,128,128), (0,y), (limite_vertical, y)) 
            x += self.CELL_SIZE
            y += self.CELL_SIZE


    def run(self):     
        i = 0
        while True:
            self.clock.tick(self.ticks) 

            for event in pg.event.get():
                if event.type == pg.QUIT: #para detener la ejecución al cerrar la ventana
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_p:
                        pass
                if event.type == pg.MOUSEBUTTONDOWN:
                    position = pg.mouse.get_pos()
                    self.handleClick(position)
            
            self.showRules()
            #if i <= 2:
            self.showCells()
            i += 1
            self.grid() #mostrar la cuadrícula

            pg.display.update()
            pg.display.flip() #actualizar el mundo para mostrar nuevos cambios.

    def handleClick(self, position):
        index = position[1] // self.CELL_SIZE, position[0] // self.CELL_SIZE
        print("index:", index)

        if index[0] == 2:
            if self.out[index[1]] in [0, 1]:
                val = int(not self.out[index[1]])
                self.out[index[1]] = val
                i = (index[1]-25) / 7
                rules[i] = val
                print("rules: ", rules)
        elif index[0] == 4:
            print("entra")
            self.cells[index[1]].setInitState(int(not self.cells[index[1]].getState()))
        else:
            print("No puede seleccionar esa celda.")
        

class Rules():
    def __init__(self):
        pass



if '__main__' == __name__:
    #w = Window(10, (650, 650), 3)
    w = Window(100, (1200, 1200 // 2), 3)
    w.run()