from pygame import Vector2, Vector3
from math import sin, cos

# Redefined here to prevent a circular import, hopefully I don't forget to change it here
# if I change it in main
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

THETA = 3.14159 / 4
PHI = 0.55536

SCALE_FACTOR = 100
VERTICAL_OFFSET = 100 # Shifts every screen point down

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