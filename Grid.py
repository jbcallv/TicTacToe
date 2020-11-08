import pygame

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