import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Box")

# Define box dimensions
box_width = 200
box_height = 200
box_depth = 200

# Define box position
box_x = width // 2
box_y = height // 2

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define vertices of the box
vertices = [
    (box_x - box_width // 2, box_y - box_height // 2, -box_depth // 2),
    (box_x + box_width // 2, box_y - box_height // 2, -box_depth // 2),
    (box_x + box_width // 2, box_y + box_height // 2, -box_depth // 2),
    (box_x - box_width // 2, box_y + box_height // 2, -box_depth // 2),
    (box_x - box_width // 2, box_y - box_height // 2, box_depth // 2),
    (box_x + box_width // 2, box_y - box_height // 2, box_depth // 2),
    (box_x + box_width // 2, box_y + box_height // 2, box_depth // 2),
    (box_x - box_width // 2, box_y + box_height // 2, box_depth // 2)
]

# Define edges of the box
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Define main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Set the camera position
    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)

    # Draw the edges
    for edge in edges:
        glBegin(GL_LINES)
        glColor3f(WHITE)
        glVertex3f(vertices[edge[0]][0], vertices[edge[0]][1], vertices[edge[0]][2])
        glVertex3f(vertices[edge[1]][0], vertices[edge[1]][1], vertices[edge[1]][2])
        glEnd()

    # Update the display
    pygame.display.flip()

# Quit the program
pygame.quit()

