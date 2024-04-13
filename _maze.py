# pip install pygame

import pygame
import random

# Constants
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 20
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Maze Generator")

# Create the maze grid
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

def generate_maze(row, col):
    grid[row][col] = 1

    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    random.shuffle(directions)

    for dx, dy in directions:
        new_row, new_col = row + dy, col + dx
        if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] == 0:
            if dx == 0:
                grid[row][min(col, new_col) + 1] = 1
            else:
                grid[min(row, new_row) + 1][col] = 1
            generate_maze(new_row, new_col)

# Generate the maze
generate_maze(0, 0)

# Set the start and end positions
start_pos = (0, 0)
end_pos = (ROWS - 1, COLS - 1)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Draw the maze
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw the start and end positions
    pygame.draw.rect(screen, GREEN, (start_pos[1] * CELL_SIZE, start_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (end_pos[1] * CELL_SIZE, end_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

pygame.quit()
