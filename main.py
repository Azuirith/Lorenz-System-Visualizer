import pygame
from pygame import Vector2, Vector3
from mesh import Mesh
from math import sin, cos
from triangle import Triangle

pygame.init()

TITLE = "Lorenz System Visualizer"

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
SCREEN_COLOR = (255, 255, 255)

THETA = 3.14159 / 4
PHI = 0.55536

screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

# Temporary testing with this cube that I designed a while back
cube = Mesh(size=250, color=(255, 0, 255))
cube.triangles = [Triangle(Vector3(0, 0, 0), Vector3(0, 1, 0), Vector3(1, 1, 0)), 
                  Triangle(Vector3(0, 0, 0), Vector3(1, 1, 0), Vector3(1, 0, 0)),
                  Triangle(Vector3(1, 0, 0), Vector3(1, 1, 0), Vector3(1, 1, 100)),
                  Triangle(Vector3(1, 0, 0), Vector3(1, 1, 100), Vector3(1, 0, 100)),
                  Triangle(Vector3(1, 0, 100), Vector3(1, 1, 100), Vector3(0, 1, 100)),
                  Triangle(Vector3(1, 0, 100), Vector3(0, 1, 100), Vector3(0, 0, 100)),
                  Triangle(Vector3(0, 0, 100), Vector3(0, 1, 100), Vector3(0, 1, 0)),
                  Triangle(Vector3(0, 0, 100), Vector3(0, 1, 0), Vector3(0, 0, 0)),
                  Triangle(Vector3(0, 1, 0), Vector3(0, 1, 100), Vector3(1, 1, 100)), 
                  Triangle(Vector3(0, 1, 0), Vector3(1, 1, 100), Vector3(1, 1, 0)),
                  Triangle(Vector3(0, 0, 100), Vector3(0, 0, 0), Vector3(1, 0, 0)),
                  Triangle(Vector3(0, 0, 100), Vector3(1, 0, 0), Vector3(1, 0, 100))]

pyramid = Mesh(size=200, color=(255, 0, 255))
pyramid.triangles = [Triangle(Vector3(2, 0, 0), Vector3(2.5, 1, 50), Vector3(3, 0, 0)), 
                     Triangle(Vector3(3, 0, 0), Vector3(2.5, 1, 50), Vector3(3, 0, 100)), 
                     Triangle(Vector3(3, 0, 100), Vector3(2.5, 1, 50), Vector3(2, 0, 100)), 
                     Triangle(Vector3(2, 0, 100), Vector3(2.5, 1, 50), Vector3(2, 0, 0)), 
                     Triangle(Vector3(2, 0, 0), Vector3(2, 0, 100), Vector3(3, 0, 100)), 
                     Triangle(Vector3(2, 0, 0), Vector3(3, 0, 100), Vector3(3, 0, 0))]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SCREEN_COLOR)

    for triangle in cube.triangles:
        projectedVertices = [Vector2(triangle.vertices[0].x, triangle.vertices[0].y),
                             Vector2(triangle.vertices[1].x, triangle.vertices[1].y),
                             Vector2(triangle.vertices[2].x, triangle.vertices[2].y)]
        
        for index, projectedVertex in enumerate(projectedVertices):
            if pygame.key.get_pressed()[pygame.K_w]: triangle.vertices[index].y -= 0.01
            if pygame.key.get_pressed()[pygame.K_s]: triangle.vertices[index].y += 0.01
            if pygame.key.get_pressed()[pygame.K_d]: triangle.vertices[index].x -= 0.01
            if pygame.key.get_pressed()[pygame.K_a]: triangle.vertices[index].x += 0.01
            if pygame.key.get_pressed()[pygame.K_LEFT]: triangle.vertices[index].z -= 1
            if pygame.key.get_pressed()[pygame.K_RIGHT]: triangle.vertices[index].z += 1

            projectedVertex.x *= 100
            projectedVertex.y *= 100

            projectedVertex.x *= cos(THETA)
            projectedVertex.x -= triangle.vertices[index].z * sin(THETA)
            projectedVertex.x += SCREEN_WIDTH / 2

            projectedVertex.y *= cos(PHI) 
            projectedVertex.y -= projectedVertex.x * sin(THETA) * sin(PHI)
            projectedVertex.y -= triangle.vertices[index].z * cos(THETA) * sin(PHI) 
            projectedVertex.y = SCREEN_HEIGHT / 2 - projectedVertex.y

        pygame.draw.line(screen, cube.color, projectedVertices[0], projectedVertices[1])
        pygame.draw.line(screen, cube.color, projectedVertices[1], projectedVertices[2])
        pygame.draw.line(screen, cube.color, projectedVertices[2], projectedVertices[0])

    for triangle in pyramid.triangles:
        projectedVertices = [Vector2(triangle.vertices[0].x, triangle.vertices[0].y),
                             Vector2(triangle.vertices[1].x, triangle.vertices[1].y),
                             Vector2(triangle.vertices[2].x, triangle.vertices[2].y)]
        
        for index, projectedVertex in enumerate(projectedVertices):
            if pygame.key.get_pressed()[pygame.K_w]: triangle.vertices[index].y -= 0.01
            if pygame.key.get_pressed()[pygame.K_s]: triangle.vertices[index].y += 0.01
            if pygame.key.get_pressed()[pygame.K_d]: triangle.vertices[index].x -= 0.01
            if pygame.key.get_pressed()[pygame.K_a]: triangle.vertices[index].x += 0.01
            if pygame.key.get_pressed()[pygame.K_LEFT]: triangle.vertices[index].z -= 1
            if pygame.key.get_pressed()[pygame.K_RIGHT]: triangle.vertices[index].z += 1

            projectedVertex.x *= 100
            projectedVertex.y *= 100

            projectedVertex.x *= cos(THETA)
            projectedVertex.x -= triangle.vertices[index].z * sin(THETA)
            projectedVertex.x += SCREEN_WIDTH / 2

            projectedVertex.y *= cos(PHI) 
            projectedVertex.y -= projectedVertex.x * sin(THETA) * sin(PHI)
            projectedVertex.y -= triangle.vertices[index].z * cos(THETA) * sin(PHI) 
            projectedVertex.y = SCREEN_HEIGHT / 2 - projectedVertex.y

        pygame.draw.line(screen, cube.color, projectedVertices[0], projectedVertices[1])
        pygame.draw.line(screen, cube.color, projectedVertices[1], projectedVertices[2])
        pygame.draw.line(screen, cube.color, projectedVertices[2], projectedVertices[0])

    pygame.display.flip()