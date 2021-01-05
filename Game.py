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

        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_KP7):
                game_grid.keySeven()
            if (event.key == pygame.K_KP8):
                game_grid.keyEight()
            if (event.key == pygame.K_KP9):
                game_grid.keyNine()
            if (event.key == pygame.K_KP4):
                game_grid.keyFour()
            if (event.key == pygame.K_KP5):
                game_grid.keyFive()
            if (event.key == pygame.K_KP6):
                game_grid.keySix()
            if (event.key == pygame.K_KP1):
                game_grid.keyOne()
            if (event.key == pygame.K_KP2):
                game_grid.keyTwo()
            if (event.key == pygame.K_KP3):
                game_grid.keyThree()

    print(game_grid.checkWin())

    game_grid.drawGrid()
    pygame.display.update()