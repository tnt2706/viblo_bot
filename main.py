import sys
import random


def parse_input(input_str):
    print(input_str)
    lines = input_str.split("\n")
    current_piece = list(map(int, lines[1].split(" ")))
    my_board = list(map(int, lines[2].split(" ")))
    return (current_piece, my_board)


def coordinates_to_index(col, row):
    return col * 9 + row


def coordinates_to_slot(col, row):
    return (col // 3) * 9 + row


def find_placeable_slots(board):
    slots = get_slots(board)
    return slots


def get_slots(board):
    slots = []
    for i in range(3):
        for j in range(9):
            c1 = board[coordinates_to_index(i * 3, j)]
            if c1 < 1:
                slots.append(coordinates_to_slot(i * 3, j))

    return slots


input_str = """2
7 8 10
9 9 8 9 -1 9 9 -1 -1 7 10 7 7 -1 9 7 -1 -1 9 10 8 9 -1 10 10 -1 -1 -1 10 7 9 9 -1 -1 -1 8 -1 10 9 9 8 -1 -1 -1 10 -1 8 8 8 8 -1 -1 -1 7 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
7 9 9 9 -1 7 9 -1 -1 10 10 7 10 -1 9 7 -1 -1 9 10 8 9 -1 10 10 -1 -1 -1 10 7 9 9 -1 -1 -1 8 -1 10 9 9 8 -1 -1 -1 10 -1 8 8 7 8 -1 -1 -1 7 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1"""

# input_str = ""
# for line in sys.stdin:
#     input_str += line

current_piece, my_board = parse_input(input_str)
placeable = find_placeable_slots(my_board)
output = random.choice(placeable)

