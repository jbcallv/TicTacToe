import pygame

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

# game loop
running = True
while (running):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False

    pygame.display.update()