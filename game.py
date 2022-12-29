import pygame as pg
import sys, os
import numpy as np
import random
from copy import copy as cp

from automata import *
from rules import Rules


""" 
Game: clase encargada de toda la parte gráfica utilizando la biblioteca pygame
"""
class Game():

    """ 
    Constructor encargado de inicializar los atributos del objeto.
    """
    def __init__(self, n, size, ticks):
        self.n = n # matriz nxn
        self.EXTRA_HEIGHT = 50
        self.HEIGHT = size[1]
        self.TOTAL_HEIGHT = size[1] + self.EXTRA_HEIGHT#1300
        self.WIDTH = size[0]
        self.CELL_SIZE = self.WIDTH // n
        self.pantalla = pg.display.set_mode((self.WIDTH, self.TOTAL_HEIGHT))
        self.clock = pg.time.Clock() #reloj para manipular la velocidad de la ejecución.
        self.colors = {
            0: (0,0,0),
            1: (255,255,255), #blanco
            2: (125,125,125), #gris
        }

        self.static_cells = self.createInitCells()
        self.cells = []
        self.out = []
        self.rules = Rules()
        self.t = 1

        self.setup(ticks)


    """ 
    Realiza las configuraciones iniciales de la ventana y el reloj
    """
    def setup(self, ticks):
        pg.init()
        pg.display.set_caption('1D cellular automata')
        self.pantalla.fill((255,255,255)) 
        self.clock.tick(ticks) 


    """
    Muestra en una sección de la pantalla los posibles estados de las celdas y la salida para su posterior modificación (reglas de transición)
    """
    def showRules(self):
        s = self.CELL_SIZE
        x = 0
        y = 0

        posibilidades = [] #para mostrar los posibles estados de una celda
        posibilidades.extend([2]*24) #celdas vacías
        posibilidades.extend([0, 0, 0]) #un estado
        posibilidades.extend([2]*4)
        posibilidades.extend([0, 0, 1])
        posibilidades.extend([2]*4)
        posibilidades.extend([0, 1, 0])
        posibilidades.extend([2]*4)
        posibilidades.extend([0, 1, 1])
        posibilidades.extend([2]*4)
        posibilidades.extend([1, 0, 0])
        posibilidades.extend([2]*4)
        posibilidades.extend([1, 0, 1])
        posibilidades.extend([2]*4)
        posibilidades.extend([1, 1, 0])
        posibilidades.extend([2]*4)
        posibilidades.extend([1, 1, 1])
        posibilidades.extend([2]*24)

        rules = self.rules.getRules()
        self.out.extend([2]*25) #celdas vacías
        self.out.append(rules[0]) #celda que muestra la salida del estado de la fila anterior
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
            pg.draw.rect( #primera fila vacía
                self.pantalla, 
                self.colors.get(2),
                pg.rect.Rect(x, 0, s, s)#, cs[0], cs[1])
            )
            pg.draw.rect( #segunda fila que muestra las 8 posibilidades
                self.pantalla, 
                self.colors.get(posibilidades[i]),
                pg.rect.Rect(x, s, s, s)#, cs[0], cs[1])
            )
            pg.draw.rect( #tercera fila que muestra la salida de cada posibilidad, se usa para establecer las reglas de transición
                self.pantalla, 
                self.colors.get(self.out[i]),
                pg.rect.Rect(x, 2*s, s, s)#, cs[0], cs[1])
            )
            pg.draw.rect( #cuarta fila vacía
                self.pantalla, 
                self.colors.get(2),
                pg.rect.Rect(x, 3*s, s, s)#, cs[0], cs[1])
            )
            x += s

    """ 
    Inicializa la primer fila con el estado de las celdas generado de forma pseudo-aleatoria
    """
    def createInitCells(self):
        aux_cells = np.array([])
        for i in range(self.n):
            if i != 0:
                # se crean las nuevas celdas
                # la celda de la extrema derecha toma el vecino de la derecha como muerto (0)
                cell = Automata(aux_cells[i-1].getState(), 0, random.randint(0, 1))
                aux_cells = np.append(aux_cells, cell)
                aux_cells[i-1].set_rhn(cell.getState())
            else:
                cell = Automata(0, 0, random.randint(0, 1)) # primera celda, el vecino de la izquierda se toma como muerto (0)
                aux_cells = np.append(aux_cells, cell)
        return aux_cells

    """ 
    Se encarga de mostrar en pantalla la primera fila de celdas "estáticas"
    """
    def showInitCells(self):
        s = self.CELL_SIZE
        x = 0
        y = self.EXTRA_HEIGHT - 1
        
        for i in range(self.n):
            pg.draw.rect(
                self.pantalla, 
                self.colors.get(self.static_cells[i].getState()),
                pg.rect.Rect(x, y, s, s)
            )
            x += s
        
    """ 
    Muestra en pantalla la nueva generación en la fila inmediatamente siguiente a la última generada.
    """
    def newGen(self):
        s = self.CELL_SIZE
        x = 0
        y = self.EXTRA_HEIGHT + s*(self.t) - 1
        rules = self.rules.getRules()
        
        if self.t == 1:
            self.cells = [cp(self.static_cells[i]) for i in range(self.static_cells.size)]
        
        for i in range(self.n):
            # se actualiza el estado de cada celda usando las reglas de transición
            self.cells[i].setState(rules)
            pg.draw.rect(
                self.pantalla, 
                self.colors.get(self.cells[i].getState()),
                pg.rect.Rect(x, y, s, s)
            )
            # se actualiza el estado de los vecinos de las celdas actual (lhn) y anterior (rhn)
            self.cells[i].set_lhn(self.cells[i-1].getState())
            self.cells[i-1].set_rhn(self.cells[i].getState())
            x += s
        self.t += 1

    """ 
    Muestra en pantalla una cuadrícula
    """
    def grid(self):
        x = 0
        y = 0
        limite_horizontal = self.WIDTH 
        limite_vertical = self.TOTAL_HEIGHT

        for i in range(self.n):
            pg.draw.line(self.pantalla, (128,128,128), (x,0), (x, limite_vertical)) #lineas verticales
            pg.draw.line(self.pantalla, (128,128,128), (0,y), (limite_horizontal, y)) #lineas horizontales
            x += self.CELL_SIZE
            y += self.CELL_SIZE

    """ 
    Ejecuta el juego de forma indefinida hasta que se cierra la ventana.
    """
    def run(self):     
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT: #para detener la ejecución al cerrar la ventana
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN: #para una nueva generación
                    if event.key == pg.K_p:
                        print("P!!!")
                        self.newGen()
                if event.type == pg.MOUSEBUTTONDOWN: #para captular los eventos de click
                    position = pg.mouse.get_pos()
                    self.handleClick(position)

            self.showRules()
            self.showInitCells()
            self.grid()

            pg.display.update()
            pg.display.flip() #actualizar el mundo para mostrar nuevos cambios.

    """ 
    Maneja los eventos de click realizados por el usuario.
    """
    def handleClick(self, position):
        index = position[1] // self.CELL_SIZE, position[0] // self.CELL_SIZE
        print("index:", index)

        if index[0] == 2: #se modifica la salida de una de las reglas de transición
            if self.out[index[1]] in [0, 1]:
                val = int(not self.out[index[1]])
                self.out[index[1]] = val
                i = (index[1]-25) / 7 #se obtiene el número de la regla modificada
                self.rules.setRule(i, val)
        elif index[0] == 4: #se modifica el estado de una celda de la fila inicial
            self.static_cells[index[1]].setInitState(int(not self.static_cells[index[1]].getState()))
        else:
            print("No puede seleccionar esa celda.")
        