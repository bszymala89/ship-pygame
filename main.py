import pygame_menu
import pygame

from settings import SCREEN_HEIGHT, SCREEN_WIDTH, COLOR_BACKROUND, Settings
from screens.settings_menu import Settings_menu
from screens.game_screen import game_Screen
from screens.main_menu import Menu


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ships")

    current_screen = "main_menu"
    running = True
    theme = pygame_menu.themes.THEME_BLUE

    font = pygame.font.Font("freesansbold.ttf", 32)


    def show_main_menu():
        nonlocal current_screen
        current_screen = "main_menu"
        print(current_screen)

    def show_settings():
        nonlocal current_screen
        current_screen = "settings_menu"
        print(current_screen)

    def start_game():
        nonlocal current_screen
        current_screen = "game"

    def exit_game():
        nonlocal running
        running = False

    main_menu = Menu(screen, theme, show_settings, start_game, exit_game)
    settings_menu = Settings_menu(theme, Settings)
    game_screen = game_Screen(screen)

    try:
        while running:
            screen.fill(COLOR_BACKROUND)

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    if current_screen == "main_menu":
                        running = False
                    else:
                        show_main_menu()

            if not running:
                break

            if current_screen == "main_menu":
                main_menu.handle_events(events)
                main_menu.draw(screen)
            elif current_screen == "settings_menu":
                settings_menu.handle_events(events)
                settings_menu.draw(screen)
            elif current_screen == "game":
                game_screen.draw([], [])

            pygame.display.flip()
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()