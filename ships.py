import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
GRID_SIZE = 10
CELL_SIZE = 50
GRID_SPACING = 5

BOARD_SIZE = GRID_SIZE * CELL_SIZE + (GRID_SIZE - 1) * GRID_SPACING

running = True

COLOR_CELL = (0, 123, 255)
COLOR_SHOT = (0, 85, 176)
COLOR_DEAD_SHIP = (222, 24, 24)
COLOR_SHIP = (50, 50, 50)

shot_list = [(4,7), (1,5), (3,9)]
ship_list = [(6,9), (1,5), (5,4)]

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

    draw_board()

    pygame.display.flip()

