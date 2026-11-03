from settings import GRID_SIZE, CELL_SIZE, GRID_SPACING, COLOR_CELL, COLOR_DEAD_SHIP, COLOR_SHOT,  COLOR_SHIP, CENTER_X_SPACING, CENTER_Y_SPACING
import pygame

class game_Screen:
    def __init__(self, screen):
        self.screen = screen
        self.selected_cells = set()

    def handle_events(self, events):
        step = CELL_SIZE + GRID_SPACING
        for event in events:
            if event.type != pygame.MOUSEBUTTONDOWN or event.button != 1:
                continue

            x, y = event.pos
            horizontal_offset = x - CENTER_Y_SPACING
            vertical_offset = y - CENTER_X_SPACING
            horizontal_cell = horizontal_offset // step
            vertical_cell = vertical_offset // step

            if (
                0 <= horizontal_cell < GRID_SIZE
                and 0 <= vertical_cell < GRID_SIZE
                and horizontal_offset % step < CELL_SIZE
                and vertical_offset % step < CELL_SIZE
            ):
                self.selected_cells.add((horizontal_cell, vertical_cell))
    
    def draw(self, shot_list, ship_list):
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                color = COLOR_CELL
                if (y, x) in shot_list and (y, x) in ship_list:
                    color = COLOR_DEAD_SHIP
                elif (y, x) in ship_list:
                    color = COLOR_SHIP
                elif (y, x) in self.selected_cells:
                    color = COLOR_SHOT
                

                # print(INITIAL_X_SPACING, INITIAL_Y_SPACING)
    
                pygame.draw.rect(
                    self.screen,
                    color,
                    pygame.Rect(
                        ((CELL_SIZE + GRID_SPACING) * y) + CENTER_Y_SPACING,
                        ((CELL_SIZE + GRID_SPACING) * x) + CENTER_X_SPACING,
                        CELL_SIZE,
                        CELL_SIZE))