import pygame
from pygame import Vector2, Vector3
from math import sin, cos

pygame.init()

TITLE = "Lorenz System Visualizer"

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
AXIS_WIDTH = 3
AXIS_LENGTH = 5

SCALE_FACTOR = 100
VERTICAL_OFFSET = 100 # Shifts every screen point down
TEXT_SIZE = 48

SCREEN_COLOR = (255, 255, 255)
AXIS_COLOR = (0, 0, 0)
LINE_COLOR = (255, 0, 255)

THETA = 3.14159 / 4
PHI = 0.55536

screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

font = pygame.font.Font("assets/fonts/cmunti.ttf", size=TEXT_SIZE)

def draw_axes(screen):
    origin = project_point(Vector3(0, 0, 0))

    x_endpoint = project_point(Vector3(AXIS_LENGTH, 0, 0))
    y_endpoint = project_point(Vector3(0, AXIS_LENGTH, 0))
    z_endpoint = project_point(Vector3(0, 0, AXIS_LENGTH))

    pygame.draw.line(screen, AXIS_COLOR, origin, x_endpoint, width=AXIS_WIDTH)
    x_label = font.render("x", True, AXIS_COLOR)
    x_label_position = Vector2(x_endpoint.x + TEXT_SIZE / 5, x_endpoint.y - TEXT_SIZE / 2)
    screen.blit(x_label, x_label_position)

    pygame.draw.line(screen, AXIS_COLOR, origin, y_endpoint, width=AXIS_WIDTH)
    y_label = font.render("y", True, AXIS_COLOR)
    y_label_position = Vector2(y_endpoint.x - TEXT_SIZE / 4, y_endpoint.y - TEXT_SIZE * 1.5)
    screen.blit(y_label, y_label_position)
    
    pygame.draw.line(screen, AXIS_COLOR, origin, z_endpoint, width=AXIS_WIDTH)
    z_label = font.render("z", True, AXIS_COLOR)
    z_label_position = Vector2(z_endpoint.x - TEXT_SIZE / 1.4, z_endpoint.y - TEXT_SIZE / 2.25)
    screen.blit(z_label, z_label_position)

def project_point(point: Vector3):
    point *= SCALE_FACTOR

    # Unmodified coordinates are needed to correctly calculate projections
    x = point.x
    y = point.y
    z = point.z
    
    point.x = x * cos(THETA) - z * sin(THETA)
    point.x += SCREEN_WIDTH / 2

    point.y = y * cos(PHI) - x * sin(THETA) * sin(PHI) - z * cos(THETA) * sin(PHI)
    point.y = SCREEN_HEIGHT / 2 + VERTICAL_OFFSET - point.y

    point = Vector2(point.x, point.y) # Flattens to 2D
    return point

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SCREEN_COLOR)

    draw_axes(screen)

    pygame.display.flip()