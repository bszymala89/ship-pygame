import pygame

size = 10
starting_letter = 65

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
    


display_board(create_board())