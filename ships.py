from enum import Enum, auto

import pygame_menu
import pygame

pygame.init()

window = pygame.display.set_mode((1280, 720))

font = pygame.font.Font('freesansbold.ttf', 32)

GRID_SIZE = 10
CELL_SIZE = 50
GRID_SPACING = 5

BOARD_SIZE = GRID_SIZE * CELL_SIZE + (GRID_SIZE - 1) * GRID_SPACING

COLOR_CELL = (0, 123, 255)
COLOR_SHOT = (0, 85, 176)
COLOR_DEAD_SHIP = (222, 24, 24)
COLOR_SHIP = (50, 50, 50)

COLOR_BACKROUND = (255, 255, 255)
COLOR_BUTTON = (200, 200, 200)

shot_list = [(4,7), (1,5), (3,9)]
ship_list = [(6,9), (1,5), (5,4)]

running = True

class screen(Enum):
    MENU = auto()
    SETTINGS = auto()
    GAME = auto()
current_screen = screen.MENU

def settings():
    global context

    context = screen.MENU

def play():
    global context

    context = draw_board

def main_menu():
    global context

    context = draw_main_menu

def draw_main_menu():
    menu = pygame_menu.Menu(
        height=720, theme=pygame_menu.themes.THEME_BLUE, title="Ship game", width=1280
    )

    menu.add.button("Play", play)
    menu.add.button("Settings", settings)
    menu.add.button("Exit", lambda: exit())

    #


    menu.mainloop(window)

def draw_settings_menu():
    menu = pygame_menu.Menu(
        height=720, theme=pygame_menu.themes.THEME_BLUE, title="Settings", width=1280
    )

    menu.add.selector("Game mode ", [("Player vs Machine", 1), ("Player vs Player", 2)])
    menu.add.text_input("Board size ", default="10")
    menu.add.selector("Ship placement mode ", [("Manual", 1), ("Auto", 2)])
    menu.add.text_input("Ship limit ", default="5")
    menu.add.range_slider("Turn time limit ", 30, (5, 60), 5)

    menu.add.none_widget()
    menu.add.none_widget()

    menu.add.button("Back to main menu", lambda: main_menu, align=pygame_menu.locals.ALIGN_LEFT)

    menu.add.button("Play", play, align=pygame_menu.locals.ALIGN_RIGHT)

    menu.mainloop(window)


def draw_board():
    #pygame.draw.rect
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color = COLOR_CELL
            if (y, x) in shot_list and (y, x) in ship_list:
                color = COLOR_DEAD_SHIP
            elif (y, x) in shot_list:
                color = COLOR_SHOT
            elif (y, x) in ship_list:
                color = COLOR_SHIP

            pygame.draw.rect(
                screen,
                color,
                pygame.Rect(
                    (CELL_SIZE + GRID_SPACING) * y,
                    (CELL_SIZE + GRID_SPACING) * x,
                    CELL_SIZE,
                    CELL_SIZE))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            column = x / CELL_SIZE
            row = y / CELL_SIZE

    if current_screen == screen.GAME:
        draw_board()
    elif current_screen == screen.MENU:
        draw_main_menu
    elif current_screen == screen.SETTINGS:
        draw_settings_menu()

    # draw_board()
    context()

    pygame.display.flip()

