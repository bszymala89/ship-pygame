# place for enums and settings

from enum import Enum, auto
from dataclasses import dataclass

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

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