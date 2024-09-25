import pygame
from Cell import Cell
import Colors
import Config

# Placeholder for the Sidebar element
class SideBar:
    def __init__(self):
        # Cell types available to select
        self.cells = [Cell(Colors.RED), Cell(Colors.GREEN), Cell(Colors.BLACK)]

    def draw(self, screen):
        # Draw the sidebar
        pygame.draw.rect(screen, Colors.BLUE, pygame.Rect(Config.SIDEBAR_X_START, 0, Config.SIDEBAR_WIDTH, Config.HEIGHT))
        
        # Draw available cells
        for i, cell in enumerate(self.cells):
            cell.drawCell(screen, (Config.CATALOGUE_X_START, 
                               Config.CELL_CATALOGUE_PADDING_Y + i * (Config.CELL_CATALOGUE_SIZE + Config.CELL_CATALOGUE_INTERLINE_PADDING)),
                               Config.CELL_CATALOGUE_SIZE)

    def get_cell(self, pos):
        # Catch a click on a cell from the sidebar
        x, y = pos
        if x >= Config.CATALOGUE_X_START and x <= Config.CATALOGUE_X_END:
            # Select the corresponding cell based on the position clicked
            index = (y - Config.CELL_CATALOGUE_PADDING_Y) // (Config.CELL_CATALOGUE_SIZE + Config.CELL_CATALOGUE_INTERLINE_PADDING)
            if 0 <= index < len(self.cells):
                return self.cells[index]
        return None