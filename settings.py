# place for enums and settings

from enum import Enum, auto
from dataclasses import dataclass

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

GRID_SIZE = 10
CELL_SIZE = 50
GRID_SPACING = 5

INITIAL_X_SPACING = (SCREEN_WIDTH // 2) - (GRID_SIZE * (CELL_SIZE + GRID_SPACING))
INITIAL_Y_SPACING = (SCREEN_HEIGHT // 2) - (GRID_SIZE * (CELL_SIZE + GRID_SPACING))

COLOR_CELL = (0, 123, 255)
COLOR_SHOT = (0, 85, 176)
COLOR_DEAD_SHIP = (222, 24, 24)
COLOR_SHIP = (50, 50, 50)
COLOR_BACKROUND = (255, 255, 255)
COLOR_BUTTON = (200, 200, 200)

class PlayMode(Enum):
    PLAYER_VS_MACHINE = auto()
    PLAYER_VS_PLAYER = auto()

class ShipPlacemenMode(Enum):
    MANUAL = auto()
    AUTO = auto()

@dataclass
class Settings:
    play_mode: PlayMode = PlayMode.PLAYER_VS_MACHINE
    ship_placement_mode: ShipPlacemenMode = ShipPlacemenMode.MANUAL