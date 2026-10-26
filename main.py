from settings import SCREEN_HEIGHT, SCREEN_WIDTH
from screens.main_menu import Menu
from screens.settings_menu import Settings_menu
import pygame_menu
import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    current_screen = "main_menu"
    running = True

    theme = pygame_menu.themes.THEME_BLUE

    pygame.display.set_caption("Ships")

    font = pygame.font.Font("freesansbold.ttf", 32)

    def show_settings():
        nonlocal current_screen
        current_screen = "settings_menu"

    def start_game():
        nonlocal current_screen
        current_screen = "game"

    def exit_game():
        nonlocal running
        running = False

    main_menu = Menu(screen, theme, show_settings, start_game, exit_game)

    try:
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            if current_screen == "main_menu":
                main_menu.handle_events(events)
                main_menu.draw(screen)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()