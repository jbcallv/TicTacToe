import pygame

from Grid import Grid

pygame.init()

# dimensions of game window
WIDTH = 350
HEIGHT = 350
size = (WIDTH, HEIGHT)

# initialize window
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic-Tac-Toe")

# create game window
pygame.display.flip()

# grid class instantiation
white = (255, 255, 255)
game_grid = Grid(screen, WIDTH, HEIGHT, white)

# game loop
running = True
while (running):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False

    game_grid.drawGrid()
    pygame.display.update()