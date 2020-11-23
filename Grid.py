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
        self.zeroZero = False
        self.zeroOne = False
        self.zeroTwo = False

        self.oneZero = False
        self.oneOne = False
        self.oneTwo = False

        self.twoZero = False
        self.twoOne = False
        self.twoTwo = False 

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
        if (self.zeroZero == False):
            self.zeroZero = True
            pygame.draw.line(self.window, self.color, (0, 0), (105, 105))
            pygame.draw.line(self.window, self.color, (0, 105), (105, 0))

    def keyEight(self):
        """ places x at row 0 column 1 of grid """
        if (self.zeroOne == False):
            self.zeroOne = True
            pygame.draw.line(self.window, self.color, (108, 0), (240, 105))
            pygame.draw.line(self.window, self.color, (108, 105), (240, 0))

    def keyNine(self):
        """ places x at row 0 column 2 of grid """
        if (self.zeroTwo == False):
            self.zeroTwo = True
            pygame.draw.line(self.window, self.color, (245, 0), (350, 105))
            pygame.draw.line(self.window, self.color, (245, 105), (350, 0))

    def keyFour(self):
        if (self.oneZero == False):
            self.oneZero = True
            pygame.draw.line(self.window, self.color, (0, 108), (105, 240))
            pygame.draw.line(self.window, self.color, (0, 240), (108, 105))

    def keyFive(self):
        if (self.oneOne == False):
            self.oneOne = True
            pygame.draw.line(self.window, self.color, (108, 108), (240, 240))
            pygame.draw.line(self.window, self.color, (108, 240), (240, 108))

    def keySix(self):
        if (self.oneTwo == False):
            self.oneTwo = True
            pygame.draw.line(self.window, self.color, (245, 108), (350, 240))
            pygame.draw.line(self.window, self.color, (245, 240), (350, 108))

    def keyOne(self):
        if (self.twoZero == False):
            self.twoZero = True
            pygame.draw.line(self.window, self.color, (0, 245), (105, 350))
            pygame.draw.line(self.window, self.color, (0, 350), (105, 245))

    def keyTwo(self):
        if (self.twoOne == False):
            self.twoOne = True
            pygame.draw.line(self.window, self.color, (108, 245), (240, 350))
            pygame.draw.line(self.window, self.color, (108, 350), (240, 245))

    def keyThree(self):
        if (self.twoTwo == False):
            self.twoTwo = True
            pygame.draw.line(self.window, self.color, (240, 245), (350, 350))
            pygame.draw.line(self.window, self.color, (240, 350), (350, 245))