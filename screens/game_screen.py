from settings import GRID_SIZE, CELL_SIZE, GRID_SPACING, COLOR_CELL, COLOR_DEAD_SHIP, COLOR_SHOT,  COLOR_SHIP, INITIAL_X_SPACING, INITIAL_Y_SPACING
import pygame

class game_Screen:
    def __init__(self, screen):
        self.screen = screen
        pass

    def handle_events(self, events):
        self.menu.update(events)
    
    def draw(self, shot_list, ship_list):
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                color = COLOR_CELL
                if (y, x) in shot_list and (y, x) in ship_list:
                    color = COLOR_DEAD_SHIP
                elif (y, x) in shot_list:
                    color = COLOR_SHOT
                elif (y, x) in ship_list:
                    color = COLOR_SHIP

                print(INITIAL_X_SPACING, INITIAL_Y_SPACING)
    
                pygame.draw.rect(
                    self.screen,
                    color,
                    pygame.Rect(
                        (CELL_SIZE + GRID_SPACING) * y,
                        (CELL_SIZE + GRID_SPACING) * x,
                        CELL_SIZE,
                        CELL_SIZE))