import pygame
import Colors
import Config

# Placeholder for the map
class Map:
    def __init__(self):
        # Hold empty positions on the grid
        self.grid = [[None for _ in range(Config.BOARD_SIZE)] for _ in range(Config.BOARD_SIZE)]

    def draw(self, screen):
        # Draw the cells on the map
        for row in range(Config.BOARD_SIZE):
            for col in range(Config.BOARD_SIZE):
                # If the value of the cell is not None, draw the Cell stored on memory & leave it blank otherwise
                if self.grid[row][col] is not None:
                    self.grid[row][col].drawCell(screen, (col * Config.CELL_SIZE, row * Config.CELL_SIZE), Config.CELL_SIZE)
                # Draw cell contours
                pygame.draw.rect(screen, Colors.GRAY, pygame.Rect(col * Config.CELL_SIZE, row * Config.CELL_SIZE, Config.CELL_SIZE, Config.CELL_SIZE), 1)

    def place_cell(self, row, col, cell):
        # Place a Cell instance where the mouse dropped a figure
        if 0 <= row < Config.BOARD_SIZE and 0 <= col < Config.BOARD_SIZE:
            self.grid[row][col] = cell

    def remove_cell(self, row, col):
        # Remove a Cell instance on the map
        if 0 <= row < Config.BOARD_SIZE and 0 <= col < Config.BOARD_SIZE:
            self.grid[row][col] = None

