import pygame

class ComputerOpponent:
    def __init__(self, window, grid, color):
        self.window = window
        self.grid = grid
        self.color = color
        self.generateSmartMove()

    def generateSmartMove(self):
        pass