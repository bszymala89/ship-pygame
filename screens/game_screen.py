from settings import GRID_SIZE, CELL_SIZE, GRID_SPACING, COLOR_CELL, COLOR_DEAD_SHIP, COLOR_SHOT,  COLOR_SHIP, CENTER_X_SPACING, CENTER_Y_SPACING, SHIP_NUMBER, GameStage, ShipPlacementMode
import pygame
import random

class game_Screen:
    def __init__(self, screen):
        self.screen = screen
        self.selected_cells = set()
        self.ship_cells = set()
        self.stage = GameStage.PLANNING

    def handle_events(self, events, placement_mode):
        step = CELL_SIZE + GRID_SPACING
        for event in events:
            if event.type != pygame.MOUSEBUTTONDOWN or event.button != 1:
                continue

            x, y = event.pos
            horizontal_offset = x - CENTER_Y_SPACING
            vertical_offset = y - CENTER_X_SPACING
            horizontal_cell = horizontal_offset // step
            vertical_cell = vertical_offset // step

            print(placement_mode)
            print(id(placement_mode))

            if placement_mode == ShipPlacementMode.AUTO.value and self.stage != GameStage.PLAYING:
                for i in range(SHIP_NUMBER):
                    
                    print("auto")
                    self.ship_cells.add((random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE)))
                    self.stage = GameStage.PLAYING
            elif placement_mode == ShipPlacementMode.MANUAL.value and self.stage != GameStage.PLAYING:
                if len(self.ship_cells) == SHIP_NUMBER:
                    self.stage = GameStage.PLAYING
    
                if self.stage == GameStage.PLANNING:
                    if (
                        0 <= horizontal_cell < GRID_SIZE
                        and 0 <= vertical_cell < GRID_SIZE
                        and horizontal_offset % step < CELL_SIZE
                        and vertical_offset % step < CELL_SIZE
                    ):
                        self.ship_cells.add((horizontal_cell, vertical_cell))

            if self.stage == GameStage.PLAYING:
                if (
                    0 <= horizontal_cell < GRID_SIZE
                    and 0 <= vertical_cell < GRID_SIZE
                    and horizontal_offset % step < CELL_SIZE
                    and vertical_offset % step < CELL_SIZE
                ):
                    self.selected_cells.add((horizontal_cell, vertical_cell))  

                    
    def draw(self):
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                color = COLOR_CELL
                if (y, x) in self.selected_cells and (y, x) in self.ship_cells:
                    color = COLOR_DEAD_SHIP
                elif (y, x) in self.ship_cells:
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