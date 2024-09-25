import pygame
import Config

# Placeholder for a cell
class Cell:
    def __init__(self, color):
        self.color = color

    def drawCell(self, screen, pos, cellSize):
        pygame.draw.rect(screen, self.color, pygame.Rect(pos[0], pos[1], cellSize, cellSize))