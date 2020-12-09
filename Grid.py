import pygame
from ComputerOpponent import ComputerOpponent

class Grid:
    def __init__(self, window, width, height, color):
        """ class constructor

        :param window: game window
        :param width: width of game window
        :param height: height of game window
        :param color: color of gridlines
        """
        self.window = window
        self.width = width
        self.height = height
        self.color = color

        # uses row, column format to check if a 
        # cell in the grid has been used. 1=cell taken; 0=not taken
        self.cells = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

        self.compOpp = ComputerOpponent(self.window, self, self.color)

    def drawGrid(self):
        """ draws the tic-tac-toe grid """
        # draws left vertical line
        pygame.draw.line(self.window, self.color, (self.width/4+20, 0), (self.width/4+20, self.height))

        # draws right vertical line
        pygame.draw.line(self.window, self.color, ((self.width-self.width/4)-20, 0), ((self.width-self.width/4)-20, self.height))

        # draws top horizontal line
        pygame.draw.line(self.window, self.color, (0, self.height/4+20), (self.width, self.height/4+20))

        # draws bottom horizontal line
        pygame.draw.line(self.window, self.color, (0, (self.height-self.height/4)-20), (self.width, (self.height-self.height/4)-20))

    def keySeven(self):
        """ draws an x in the upper left corner of the grid """
        #self.position_taken.append(1)
        if (self.cells[0][0] == 0):
            self.cells[0][0] = 1
            pygame.draw.line(self.window, self.color, (0, 0), (105, 105))
            pygame.draw.line(self.window, self.color, (0, 105), (105, 0))
        self.compOpp.generateSmartMove(self.cells)

    def keyEight(self):
        """ places x at row 0 column 1 of grid """
        if (self.cells[0][1] == 0):
            self.cells[0][1] = 1
            pygame.draw.line(self.window, self.color, (108, 0), (240, 105))
            pygame.draw.line(self.window, self.color, (108, 105), (240, 0))
        self.compOpp.generateSmartMove(self.cells)

    def keyNine(self):
        """ places x at row 0 column 2 of grid """
        if (self.cells[0][2] == 0):
            self.cells[0][2] = 1
            pygame.draw.line(self.window, self.color, (245, 0), (350, 105))
            pygame.draw.line(self.window, self.color, (245, 105), (350, 0))
        self.compOpp.generateSmartMove(self.cells)

    def keyFour(self):
        if (self.cells[1][0] == 0):
            self.cells[1][0] = 1
            pygame.draw.line(self.window, self.color, (0, 108), (105, 240))
            pygame.draw.line(self.window, self.color, (0, 240), (108, 105))
        self.compOpp.generateSmartMove(self.cells)

    def keyFive(self):
        if (self.cells[1][1] == 0):
            self.cells[1][1] = 1
            pygame.draw.line(self.window, self.color, (108, 108), (240, 240))
            pygame.draw.line(self.window, self.color, (108, 240), (240, 108))
        self.compOpp.generateSmartMove(self.cells)

    def keySix(self):
        if (self.cells[1][2] == 0):
            self.cells[1][2] = 1
            pygame.draw.line(self.window, self.color, (245, 108), (350, 240))
            pygame.draw.line(self.window, self.color, (245, 240), (350, 108))
        self.compOpp.generateSmartMove(self.cells)

    def keyOne(self):
        if (self.cells[2][0] == 0):
            self.cells[2][0] = 1
            pygame.draw.line(self.window, self.color, (0, 245), (105, 350))
            pygame.draw.line(self.window, self.color, (0, 350), (105, 245))
        self.compOpp.generateSmartMove(self.cells)

    def keyTwo(self):
        if (self.cells[2][1] == 0):
            self.cells[2][1] = 1
            pygame.draw.line(self.window, self.color, (108, 245), (240, 350))
            pygame.draw.line(self.window, self.color, (108, 350), (240, 245))
        self.compOpp.generateSmartMove(self.cells)

    def keyThree(self):
        if (self.cells[2][2] == 0):
            self.cells[2][2] = 1
            pygame.draw.line(self.window, self.color, (240, 245), (350, 350))
            pygame.draw.line(self.window, self.color, (240, 350), (350, 245))
        self.compOpp.generateSmartMove(self.cells)