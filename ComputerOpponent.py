import pygame
import random

class ComputerOpponent:
    def __init__(self, window, grid, color):
        self.window = window
        self.grid = grid
        self.color = color
        #self.generateSmartMove()

    def generateSmartMove(self, taken_cells):
        ind1 = random.randint(0, 2)
        ind2 = random.randint(0, 2)
        print(taken_cells)

        while (taken_cells[ind1][ind2] != 0):
            print(taken_cells[ind1][ind2])
            ind1 = random.randint(0, 2)
            ind2 = random.randint(0, 2)

        # continue generating new position
        if (ind1 == 0 and ind2 == 0):
            self.keySeven()
        if (ind1 == 0 and ind2 == 1):
            self.keyEight()
        if (ind1 == 0 and ind2 == 2):
            self.keyNine()
        if (ind1 == 1 and ind2 == 0):
            self.keyFour()
        if (ind1 == 1 and ind2 == 1):
            self.keyFive()
        if (ind1 == 1 and ind2 == 2):
            self.keySix()
        if (ind1 == 2 and ind2 == 0):
            self.keyOne()
        if (ind1 == 2 and ind2 == 1):
            self.keyTwo()
        if (ind1 == 2 and ind2 == 2):
            self.keyThree()


    def keySeven(self):
        """ draws an x in the upper left corner of the grid """
        #self.position_taken.append(1)
        if (self.grid.cells[0][0] == 0):
            self.grid.cells[0][0] = 2
            pygame.draw.line(self.window, self.color, (0, 0), (105, 105))
            #pygame.draw.line(self.window, self.color, (0, 105), (105, 0))

    def keyEight(self):
        """ places x at row 0 column 1 of grid """
        if (self.grid.cells[0][1] == 0):
            self.grid.cells[0][1] = 2
            pygame.draw.line(self.window, self.color, (108, 0), (240, 105))
            #pygame.draw.line(self.window, self.color, (108, 105), (240, 0))
        #self.compOpp.generateSmartMove(self.cells)

    def keyNine(self):
        """ places x at row 0 column 2 of grid """
        if (self.grid.cells[0][2] == 0):
            self.grid.cells[0][2] = 2
            pygame.draw.line(self.window, self.color, (245, 0), (350, 105))
            #pygame.draw.line(self.window, self.color, (245, 105), (350, 0))
        #self.compOpp.generateSmartMove(self.cells)

    def keyFour(self):
        if (self.grid.cells[1][0] == 0):
            self.grid.cells[1][0] = 2
            pygame.draw.line(self.window, self.color, (0, 108), (105, 240))
            #pygame.draw.line(self.window, self.color, (0, 240), (108, 105))
        #self.compOpp.generateSmartMove(self.cells)

    def keyFive(self):
        if (self.grid.cells[1][1] == 0):
            self.grid.cells[1][1] = 2
            pygame.draw.line(self.window, self.color, (108, 108), (240, 240))
            #pygame.draw.line(self.window, self.color, (108, 240), (240, 108))
        #self.compOpp.generateSmartMove(self.cells)

    def keySix(self):
        if (self.grid.cells[1][2] == 0):
            self.grid.cells[1][2] = 2
            pygame.draw.line(self.window, self.color, (245, 108), (350, 240))
            #pygame.draw.line(self.window, self.color, (245, 240), (350, 108))
        #self.compOpp.generateSmartMove(self.cells)

    def keyOne(self):
        if (self.grid.cells[2][0] == 0):
            self.grid.cells[2][0] = 2
            pygame.draw.line(self.window, self.color, (0, 245), (105, 350))
            #pygame.draw.line(self.window, self.color, (0, 350), (105, 245))
        #self.compOpp.generateSmartMove(self.cells)

    def keyTwo(self):
        if (self.grid.cells[2][1] == 0):
            self.grid.cells[2][1] = 1
            pygame.draw.line(self.window, self.color, (108, 245), (240, 350))
            #pygame.draw.line(self.window, self.color, (108, 350), (240, 245))
        #self.compOpp.generateSmartMove(self.cells)

    def keyThree(self):
        if (self.grid.cells[2][2] == 0):
            self.grid.cells[2][2] = 2
            pygame.draw.line(self.window, self.color, (240, 245), (350, 350))
            #pygame.draw.line(self.window, self.color, (240, 350), (350, 245))
        #self.compOpp.generateSmartMove(self.cells)