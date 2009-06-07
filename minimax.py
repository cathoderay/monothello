from copy import deepcopy
import random
from util import *


PLAYER = "W"
INFINITUM = 100000000000000000000000000000000000000000000


def ingenuous(board, turn):
    return random.choice(list(valid_positions(board, turn)))


def heuristic1(board):
    if PLAYER == "W":
        return count_pieces(board, "W") - count_pieces(board, "B")
    else:
        return count_pieces(board, "B") - count_pieces(board, "W")


def heuristic2(board):
    value = 0
    for i in range(8):
        for j in range(8):
            if board[(i, j)] == PLAYER:
                if (i == 0 and j == 0) or (i == 7 and j == 7) or \
                   (i == 0 and j == 7) or (i == 7 and j == 0):
                    value += 20
                elif (i == 3 and j == 3) or (i == 3 and j == 4) or \
                     (i == 4 and j == 3) or (i == 4 and j == 4):
                    value += 5
                elif (i == 0 and j == 1) or (i == 1 and j == 0) or \
                     (i == 7 and j == 1) or (i == 6 and j == 0) or \
                     (i == 0 and j == 6) or (i == 1 and j == 7) or \
                     (i == 7 and j == 6) or (i == 6 and j == 7) or \
                     (i == 1 and j == 1) or (i == 6 and j == 6) or \
                     (i == 6 and j == 1) or (i == 1 and j == 6):
                    value += 0
                else:
                    value += 10
    return value

def minimax(board, depth, turn, heuristic=heuristic2):
    if depth == 0 or end_game(board):
        return (heuristic(board), None)
    else:
        movement = None
        if turn == PLAYER:
            best = -INFINITUM
        else:
            best = INFINITUM
        valid = valid_positions(board, turn)
        if len(valid) == 0:
            if turn == "W":
                new_turn = "B"
            else:
                new_turn = "W"
            copy_board = deepcopy(board)
            return (minimax(copy_board, depth-1, new_turn, heuristic)[0], movement)
        else:
            for position in valid:
                copy_board = deepcopy(board)
                move(copy_board, position, turn)
                if turn == "W":
                    new_turn = "B"
                else:
                    new_turn = "W"
                value = minimax(copy_board, depth-1, new_turn, heuristic)[0]

                if turn == PLAYER:
                    if value >= best:
                        best = value
                        movement = position
                else:
                    if value <= best:
                        best = value
        return (best, movement)
