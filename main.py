import pygame
from ui import draw_axes
pygame.init()

TITLE = "Lorenz System Visualizer"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_COLOR = (255, 255, 255)

screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SCREEN_COLOR)

    # Hello!

    draw_axes(screen)

    pygame.display.flip()
