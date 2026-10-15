import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
GRID_SIZE = 10
CELL_SIZE = 50

BOARD_SIZE = GRID_SIZE * CELL_SIZE

running = True

COLOR_CELL = (0, 123, 255)
COLOR_SHOT = (0, 85, 176)
COLOR_DEAD_SHIP = (222, 24, 24)


shot_list = [(4,7), (1,5), (3,9)]

def draw_board():
    #pygame.draw.rect
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color = COLOR_CELL
            if (y, x) in shot_list:
                color = COLOR_SHOT

            pygame.draw.rect(screen, color, pygame.Rect(CELL_SIZE * y, CELL_SIZE * x, CELL_SIZE, CELL_SIZE))

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

