from settings import SCREEN_HEIGHT, SCREEN_WIDTH, PlayMode, ShipPlacemenMode , Settings
import pygame_menu

class Settings_menu:
    def __init__(self, theme, settings: Settings):
        self.settings = settings

        self.menu = pygame_menu.Menu(
            height=SCREEN_HEIGHT,
            width=SCREEN_WIDTH,
            title="Settings",
            theme=theme
        )

        self.menu.add.selector(
            "Game mode ",
            [
                ("Player vs Machine", PlayMode.PLAYER_VS_MACHINE),
                ("Player vs Player", PlayMode.PLAYER_VS_PLAYER)
            ],
            default=self.read_play_mode(),
            onchange=self.change_play_mode
        )

        self.menu.add.selector(
            "Ship placement mode",
            [
                ("Manual", ShipPlacemenMode.MANUAL),
                ("Auto", ShipPlacemenMode.AUTO)
            ],
            default=self.read_ship_placement_mode(),
            onchange=self.change_ship_placement_mode
        )

    def read_play_mode(self):
        if self.settings.play_mode == PlayMode.PLAYER_VS_PLAYER:
            return 1
        return 0

    def change_play_mode(self, value, index):
        self.settings.play_mode = value

    def read_ship_placement_mode(self):
            if self.settings.ship_placement_mode == ShipPlacemenMode.AUTO:
                return 1
            return 0
    
    def change_ship_placement_mode(self, value, index):
        self.settings.ship_placement_mode = value

    def handle_events(self, events):
        self.menu.update(events)

    def draw(self, screen):
        self.menu.draw(screen)