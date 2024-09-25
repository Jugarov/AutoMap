from Map import Map
from SideBar import SideBar
import Colors
import Config
import pygame

# Main layout class
class Game:
    def __init__(self):
        # Create the game window
        self.screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        pygame.display.set_caption("AutoMap")

        # Design the layout instancing the Map & SideBar placeholders
        self.map = Map()
        self.sidebar = SideBar()

        # Flags & memory accesses for dragging mechanisms
        self.dragging = False
        self.dragged_cell = None
        self.drag_pos = (0, 0)

    def run(self):
        running = True
        while running:
            # Draw the empty canvas, then fill in the map & sidebar
            self.screen.fill(Colors.WHITE)
            self.map.draw(self.screen)
            self.sidebar.draw(self.screen)

            # Draw a cell while holding it with the mouse
            if self.dragging and self.dragged_cell:
                # This formula draws the cell centered on the mouse's tip
                self.dragged_cell.drawCell(self.screen, (self.drag_pos[0] - Config.CELL_SIZE // 2, self.drag_pos[1] - Config.CELL_SIZE // 2), Config.CELL_SIZE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Catch a click-and-hold event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # On left click, on a cell from the sidebar is detected, store an instance of it until dropped on a valid place
                    if event.button == 1:
                        self.dragged_cell = self.sidebar.get_cell(event.pos)

                        # Update flags for dragging mechanism on holding a cell
                        if self.dragged_cell:
                            self.dragging = True
                            self.drag_pos = event.pos

                    # On right click, delete a Cell from the map
                    if event.button == 3:
                        mouse_x, mouse_y = event.pos
                        if mouse_x < Config.SIDEBAR_X_START:  # Clic dentro del tablero
                            col = mouse_x // Config.CELL_SIZE
                            row = mouse_y // Config.CELL_SIZE
                            self.map.remove_cell(row, col)

                # Catch a mouse-release event
                if event.type == pygame.MOUSEBUTTONUP:
                    # Update flags for releasing the mouse
                    if self.dragging:
                        self.dragging = False
                        mouse_x, mouse_y = event.pos

                        # Check if a cell is dropped on the map & store the cells already placed in memory
                        if mouse_x < Config.SIDEBAR_X_START:
                            col = mouse_x // Config.CELL_SIZE
                            row = mouse_y // Config.CELL_SIZE
                            self.map.place_cell(row, col, self.dragged_cell)

                # Catch the mouse movement when a cell is held & update the cell position between frames
                if event.type == pygame.MOUSEMOTION and self.dragging:
                    self.drag_pos = event.pos

            # Update the drawn frame on screen
            pygame.display.flip()

        pygame.quit()

# Run game on execution
if __name__ == "__main__":
    game = Game()
    game.run()