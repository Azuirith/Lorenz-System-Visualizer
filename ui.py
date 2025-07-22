import pygame
from pygame import Vector2, Vector3
from projection import project_point
pygame.init()

AXIS_LENGTH = 5
AXIS_WIDTH = 3
AXIS_COLOR = (0, 0, 0)

TEXT_SIZE = 48

font = pygame.font.Font("assets/fonts/cmunti.ttf", size=TEXT_SIZE)

def draw_axes(screen):
    origin = project_point(Vector3(0, 0, 0))

    x_endpoint = project_point(Vector3(AXIS_LENGTH, 0, 0))
    y_endpoint = project_point(Vector3(0, AXIS_LENGTH, 0))
    z_endpoint = project_point(Vector3(0, 0, AXIS_LENGTH))

    # I hate magic numbers as much as the next guy, but this is literally the best way I can think
    # to adjust these right now
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