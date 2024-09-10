# Made in 2024 by CtrlAltWiz

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import random

# Initialize Pygame and OpenGL - Resolution grid scale can be changed here
pygame.init()
screen = pygame.display.set_mode((600, 600), DOUBLEBUF | OPENGL)
gluOrtho2D(0, 600, 0, 600)

# Number of blue dots
num_dots = 10
trail_length = 3000  # Shorter trail length for performance
trail_step = 5  # Only render every 5th point in the trail for better performance

# Initialize positions and velocities for the dots using NumPy
dots = np.zeros((num_dots, 4))  # Each dot has [x, y, vx, vy]
dots[:, 0] = np.random.randint(50, 550, size=num_dots)  # Random x positions
dots[:, 1] = np.random.randint(50, 550, size=num_dots)  # Random y positions
dots[:, 2] = np.random.uniform(-2, 2, size=num_dots)    # Random x velocities
dots[:, 3] = np.random.uniform(-2, 2, size=num_dots)    # Random y velocities

# Initialize trails as a 3D NumPy array: num_dots x trail_length x 2 (x, y coordinates)
trails = np.zeros((num_dots, trail_length, 2))

# Pulse timers to control green flash duration when bouncing
pulse_timers = np.zeros(num_dots)  # Will track how long the dot stays green

# Main loop
running = True
trail_index = 0
pulse_duration = 20  # Duration of the green pulse

while running:
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Update positions of the dots
    dots[:, 0] += dots[:, 2]  # Update x positions
    dots[:, 1] += dots[:, 3]  # Update y positions

    # Check for wall collisions and reflect velocities
    collided_x = (dots[:, 0] <= 0) | (dots[:, 0] >= 600)
    collided_y = (dots[:, 1] <= 0) | (dots[:, 1] >= 600)
    
    # Reflect and trigger pulse on collisions
    dots[:, 2] = np.where(collided_x, -dots[:, 2], dots[:, 2])
    dots[:, 3] = np.where(collided_y, -dots[:, 3], dots[:, 3])

    # Set pulse timers when reflecting off walls
    pulse_timers = np.where(collided_x | collided_y, pulse_duration, pulse_timers)

    # Decrease pulse timers
    pulse_timers = np.maximum(0, pulse_timers - 1)

    # Store current positions in trails
    trails[:, trail_index, 0] = dots[:, 0]
    trails[:, trail_index, 1] = dots[:, 1]
    trail_index = (trail_index + 1) % trail_length  # Cycle through the trail array

    # Draw the trailing green dots
    for i in range(num_dots):
        glColor3f(0, 1, 0)  # Green color for the trail
        glPointSize(1)

        glBegin(GL_POINTS)
        for j in range(0, trail_length, trail_step):  # Draw every 'trail_step' point
            glVertex2f(trails[i, j, 0], trails[i, j, 1])
        glEnd()

    # Draw the blue dots with pulsing green effect
    for i in range(num_dots):
        if pulse_timers[i] > 0:
            glColor3f(0, 1, 0)  # Green color during pulse
        else:
            glColor3f(0, 0, 1)  # Blue color otherwise
        glPointSize(10)
        glBegin(GL_POINTS)
        glVertex2f(dots[i, 0], dots[i, 1])
        glEnd()

    pygame.display.flip()
    pygame.time.wait(1)  # Control the speed of the simulation

pygame.quit()
