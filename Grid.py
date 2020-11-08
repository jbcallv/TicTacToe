import pygame

class Grid:
    def __init__(self, window, width, height, color, thickness):
        """ class constructor

        :param window: game window
        :param width: width of game window
        :param height: height of game window
        :param color: color of gridlines
        :param thickness: width of gridlines
        """
        self.window = window
        self.width = width
        self.height = height
        self.color = color
        self.thickness = thickness

    def drawGrid(self):
        """ draws the tic-tac-toe grid """
        pass