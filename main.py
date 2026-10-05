import subprocess
import pygame

size = 10
number_of_ships = 5

starting_letter = 65
movement_helper = [
    (-1, 0), #UP: 0
    (1, 0), #DOWN: 1
    (0, 1), #RIGHT: 2
    (0, -1)] #LEFT: 3

def create_board():
    global size
    board = []

    for i in range(size):
        temp_list = []
        for j in range(size):
            temp_list.append("~")

        board.append(temp_list)

    return board

def display_board(board):
    global size

    display_string = ""

    for i in range(1, size + 1):
        display_string = display_string + " " + str(i)

    display_string += "\n"

    for i in range(size):
        temp_string = ""

        for j in range(size):
            temp_string = temp_string + board[i][j] + " "

        display_string = display_string + str(chr(starting_letter + i)) + " " + temp_string + "\n"


    print(display_string)

def convert_field_to_coordinates(field: str):
    num = ""
    for i in range(1, len(field)):
        if field[i].isdecimal() == False:
            print("Invalid coordinate format")
            return
        num = num + field[i]

    temp = (field[0], int(num))

    if temp[1] > size or ord(temp[0]) - starting_letter > size - 1:
        print("The coordinate is out of bounds")
        return

    x = temp[1] - 1
    y = ord(temp[0]) - starting_letter

    return (y, x)

def check_around_the_place(board, coordinate):
    for i in range(4):
        movement = movement_helper[i]
        if coordinate[0] + movement[0] >= 0 and coordinate[1] + movement[1] >= 0:
            if coordinate[0] + movement[0] <= size - 1 and coordinate[1] + movement[1] <= size - 1:
                if board[coordinate[0] + movement[0]][coordinate[1] + movement[1]] == "*":
                    print("You can't place your ship too close to a another ship")
                    return False
    return True
                
def place_ships(board, player_name):
    #2 player system

    number_of_placed_ships = 0

    # print("Place ships for " + player_name)

    while True:
        if number_of_ships == number_of_placed_ships:
            break

        field = input(f'({player_name}) Input the coordinate of where do you want your ship placed in this format "A1" or type "view" to view the current board ({number_of_ships - number_of_placed_ships} Left) ')

        if field == "view":
            display_board(board)
            continue
        
        coordinate = convert_field_to_coordinates(field)

        if coordinate == None:
            continue

        if board[coordinate[0]][coordinate[1]] == "*":
            print("This spot is already taken")
            continue

        if check_around_the_place(board, coordinate) == False:
            continue

        board[coordinate[0]][coordinate[1]] = "*"
        number_of_placed_ships += 1

    subprocess.run("cls", shell=True)

def start_game():
    board1 = create_board()
    board2 = create_board()

    place_ships(board1, "player1")
    place_ships(board2, "player2")

    print("player1 board")
    display_board(board1)

    print("player2 board")
    display_board(board2)

start_game()