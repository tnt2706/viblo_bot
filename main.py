import sys
import random
from typing import Any

len_bot = 26

class Analysis:
    def __init__(self):
        self.count = 0
        self.ability = 0
        self.total_score = 0

    def update_count(self,count):
        self.count += count

    def update_ability(self,ability):
        self.ability += ability

    def update_total_score(self, score):
        self.total_score += score

    def get(self):
        return dict(ability=self.ability, count=self.count, total_score=self.total_score)


def parse_input(input_str):
    lines = input_str.split("\n")
    current_piece = list(map(int, lines[1].split(" ")))
    my_board = list(map(int, lines[2].split(" ")))
    return (current_piece, my_board)


def coordinates_to_index(col, row):
    return col * 9 + row


def coordinates_to_slot(col, row):
    return (col // 3) * 9 + row


def get_slots_matrix(arr):
    slots = []

    for i in range(3):
        for j in range(9):
            c1 = arr[coordinates_to_index(i * 3, j)]
            if c1 < 1:
                slots.append(coordinates_to_slot(i * 3, j))

    return slots

def Matrix(i,j,matrix):
    if i <0 or j <0 or j>9 or i>9 :
        return 0

    return matrix[i][j]


def get_analysis_slot(matrix,num,row, col,i,j):
    row = row+i
    ability, count, total_score = 0,0,0

    if j == 0:
        recent = Matrix(row,col + 1,matrix)
        if num == recent == Matrix(row,col + 2,matrix):
            count += 1
            total_score += num * 3
        elif num == recent:
            ability += 1

    if j == 1:
        recent = Matrix(row + 1, col + 1, matrix)
        if num == recent == Matrix(row + 2, col + 2, matrix):
            count += 1
            total_score += num * 3
        elif num == recent:
            ability += 1

    if j == 2:
        recent = Matrix(row+1, col, matrix)
        if num == recent == Matrix(row+2, col, matrix):
            count += 1
            total_score += num * 3
        elif num == recent:
            ability += 1

    if j == 3:
        recent = Matrix(row + 1, col - 1, matrix)
        if num == recent == Matrix(row + 2, col-2, matrix):
            count += 1
            total_score += num * 3
        elif num == recent :
            ability += 1

    if j == 4:
        recent = Matrix(row, col-1, matrix)
        if num == recent == Matrix(row, col-2, matrix):
            count += 1
            total_score += num * 3
        elif num == recent:
            ability += 1

    if j == 5:
        recent = Matrix(row-1, col - 1, matrix)
        if num ==recent == Matrix(row-2, col - 2, matrix):
            count += 1
            total_score += num * 3
        elif num == recent:
            ability += 1

    if j == 6:
        recent = Matrix(row-1, col, matrix)
        if num == recent == Matrix(row-2, col, matrix):
            count += 1
            total_score += num * 3
        elif num == recent:
            ability += 1

    if j == 7:
        recent = Matrix(row-1, col + 1, matrix)
        if num == recent == Matrix(row-1, col + 2, matrix):
            count += 1
            total_score += num * 3
        elif num == recent:
            ability += 1

    return (ability, count, total_score)

def analysis_slot(matrix,current_piece, slot):
    analysis = Analysis()

    row = slot//3
    col = slot -row*3


    for i in range(3):
        num = current_piece[i]

        for j in range(8):
         ability, count , total_score = get_analysis_slot(matrix,num,row, col,i,j)
         analysis.update_count(count)
         analysis.update_ability(ability)
         analysis.update_total_score(total_score)


    return analysis.get()



def find_placeable_slots(current_piece, my_board):
    slots = get_slots_matrix(my_board)
    matrix = [my_board[i:i + 9] for i in range(0, len(my_board), 9)]
    if len(slots) == 27:
        return 13

    best_slot = {
        "slot": 0,
        "ability":0,
        "count":0,
        "total_score":0
    }

    for slot in slots:
        aa = analysis_slot(matrix,current_piece,slot)
        print(aa, slot)


    return random.choice(slots)


# input_str = """2
# 7 8 10
# 9 9 8 9 -1 9 9 -1 -1 7 10 7 7 -1 9 7 -1 -1 9 10 8 9 -1 10 10 -1 -1 -1 10 7 9 9 -1 -1 -1 8 -1 10 9 9 8 -1 -1 -1 10 -1 8 8 8 8 -1 -1 -1 7 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# 7 9 9 9 -1 7 9 -1 -1 10 10 7 10 -1 9 7 -1 -1 9 10 8 9 -1 10 10 -1 -1 -1 10 7 9 9 -1 -1 -1 8 -1 10 9 9 8 -1 -1 -1 10 -1 8 8 7 8 -1 -1 -1 7 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1"""


input_str = """2
7 8 10
-1 9 -1 -1 -1 -1 -1 -1 -1 \
-1 9 -1 -1 -1 -1 -1 -1 -1 \
-1 9 -1 -1 -1 -1 -1 -1 -1 \
-1 -1 -1 -1 9 -1 -1 -1 -1 \
-1 -1 -1 -1 9 -1 -1 -1 -1 \
-1 -1 -1 -1 9 -1 -1 -1 -1 \
-1 -1 -1 -1 -1 -1 -1 -1 -1 \
-1 -1 -1 -1 -1 -1 -1 -1 -1 \
-1 -1 -1 -1 -1 -1 -1 -1 -1
7 9 9 9 -1 7 9 -1 -1 10 10 7 10 -1 9 7 -1 -1 9 10 8 9 -1 10 10 -1 -1 -1 10 7 9 9 -1 -1 -1 8 -1 10 9 9 8 -1 -1 -1 10 -1 8 8 7 8 -1 -1 -1 7 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1"""


#
# input_str = ""
# for line in sys.stdin:
#     input_str += line

current_piece, my_board = parse_input(input_str)
output = find_placeable_slots(current_piece,my_board)

print(output)

