from settings import GRID_SIZE, CELL_SIZE, GRID_SPACING, COLOR_CELL, COLOR_DEAD_SHIP, COLOR_SHOT,  COLOR_SHIP, COLOR_BACKROUND, CENTER_X_SPACING, CENTER_Y_SPACING, SHIP_NUMBER, SCREEN_HEIGHT, SCREEN_WIDTH, ShipPlacementMode
from enum import Enum, auto
import pygame
import random

class GameStage(Enum):
    PLANNING = auto()
    READY = auto()
    PLAYING = auto()

class game_Screen:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        self.stage = GameStage.PLANNING

        self.start_button = None
        self.main_menu_button = None
        
        self.start()

    def start(self):
        self.selected_cells = set()
        self.ship_cells = set()

        if self.settings.ship_placement_mode == ShipPlacementMode.AUTO:
            self.auto_planning()
            self.stage = GameStage.PLAYING

    def auto_planning(self):
        while True:
            if len(self.ship_cells) == SHIP_NUMBER:
                break

            rand1 = random.randint(0, GRID_SIZE - 1)
            rand2 = random.randint(0, GRID_SIZE - 1)

            if (rand1, rand2) in self.ship_cells:
                continue

            self.ship_cells.add((rand1, rand2))

    def manual_planning(self, horizontal_offset, horizontal_cell, vertical_offset, vertical_cell, step):
        if (
            0 <= horizontal_cell < GRID_SIZE
            and 0 <= vertical_cell < GRID_SIZE
            and horizontal_offset % step < CELL_SIZE
            and vertical_offset % step < CELL_SIZE
        ):
            self.ship_cells.add((horizontal_cell, vertical_cell))

        if len(self.ship_cells) == SHIP_NUMBER:
            self.stage = GameStage.READY

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

            if self.start_button != None and self.stage == GameStage.READY:
                if self.start_button.collidepoint((x, y)):
                    self.stage = GameStage.PLAYING

            if self.main_menu_button != None:
                if self.main_menu_button.collidepoint((x, y)):
                    return "main_menu"
                    

            if len(self.ship_cells) != SHIP_NUMBER:
                if self.settings.ship_placement_mode == ShipPlacementMode.AUTO:
                    self.auto_planning()
                    self.stage = GameStage.PLAYING
                    
                elif self.settings.ship_placement_mode == ShipPlacementMode.MANUAL:
                    self.manual_planning(horizontal_offset, horizontal_cell, vertical_offset, vertical_cell, step)
                    return

            if self.stage == GameStage.PLAYING:
                if (
                    0 <= horizontal_cell < GRID_SIZE
                    and 0 <= vertical_cell < GRID_SIZE
                    and horizontal_offset % step < CELL_SIZE
                    and vertical_offset % step < CELL_SIZE
                ):
                    self.selected_cells.add((horizontal_cell, vertical_cell))

                    
    def draw(self, font):
        text = font.render(f"current stage {self.stage}", False, (0,0,0))
        self.screen.blit(text, (0,0))

        placement_text = font.render(f"current placement mode {self.settings.ship_placement_mode}", False, (0,0,0))
        self.screen.blit(placement_text, (0, 50))

        main_menu_text = font.render("Main Menu", False, (0,0,0))

        self.main_menu_button = pygame.draw.rect(
            self.screen,
            COLOR_BACKROUND,
            pygame.Rect(
                SCREEN_WIDTH * 0.005,
                SCREEN_HEIGHT * 0.95,
                main_menu_text.get_size()[0],
                main_menu_text.get_size()[1]
            )
        )

        self.screen.blit(main_menu_text, (SCREEN_WIDTH * 0.005, SCREEN_HEIGHT * 0.95))

        if self.stage != GameStage.PLAYING:
            start_text_size = font.render("Start Game", False, COLOR_BACKROUND).get_size()

            self.start_button = pygame.draw.rect(
                self.screen,
                COLOR_BACKROUND,
                pygame.Rect(
                    (SCREEN_WIDTH // 2) - (start_text_size[0] // 2),
                    SCREEN_HEIGHT - (SCREEN_HEIGHT * 0.10),
                    start_text_size[0],
                    start_text_size[1]
                )
            )

            if self.stage == GameStage.PLANNING:
                ready_text = font.render("Start Game", False, (150,150,150))
                self.screen.blit(ready_text, ((SCREEN_WIDTH // 2) - (ready_text.get_size()[0] // 2), SCREEN_HEIGHT - (SCREEN_HEIGHT * 0.10)))
            elif self.stage == GameStage.READY:
                ready_text = font.render("Start Game", False, (0,0,0))
                self.screen.blit(ready_text, ((SCREEN_WIDTH // 2) - (ready_text.get_size()[0] // 2), SCREEN_HEIGHT - (SCREEN_HEIGHT * 0.10)))
        
        # make invisible rect to act as button or make a decorative rect with border radius and backround color

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