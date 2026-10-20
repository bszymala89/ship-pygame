from settings import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame_menu

class Menu:
    def __init__(self, screen, theme, settings, play, exit):
        self.menu = pygame_menu.Menu(
            height=SCREEN_HEIGHT,
            width=SCREEN_WIDTH,
            title="Main menu",
            theme=theme
        )

        self.menu.add.button("Play", play)
        self.menu.add.button("Settings", settings)
        self.menu.add.button("Exit", exit)

    def handle_events(self, events):
        self.menu.update(events)

    def draw(self, screen):
        self.menu.draw(screen)