from copy import deepcopy
import random
from util import *


PLAYER = "W"
INFINITUM = 100000000000000000000000000000000000000000000


def baby(board, turn):
    return random.choice(list(valid_positions(board, turn)))


def weak(board):
    if PLAYER == "W":
        return count_pieces(board, "W") - count_pieces(board, "B")
    else:
        return count_pieces(board, "B") - count_pieces(board, "W")


def greedy(board):
    if  PLAYER == "W":
        return count_pieces(board, "W")
    else:
        return count_pieces(board, "B")


def posicional(board):
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


def is_max(turn):
    if turn == PLAYER:
        return True
    else:
        return False


def change_turn(turn):
    if turn == "W":
        return "B"
    else:
        return "W"


def minimax(board, depth, turn, heuristic=greedy):
    if depth == 0 or end_game(board):
        return (heuristic(board), None)
    else:
        movement = None
        if not has_valid_position(board, turn):
            child = deepcopy(board)
            return (minimax(child, depth-1, change_turn(turn), heuristic)[0], movement)
        else:
            if is_max(turn):
                best = -INFINITUM
            else:
                best = -INFINITUM
            valid = valid_positions(board, turn)
            for position in valid:             
                child = deepcopy(board)
                move(child, position, turn)
                child_value = minimax(child, depth-1, change_turn(turn), heuristic)[0]

                if is_max(turn):
                    best = max(child_value, best)
                else:
                    best = min(child_value, best)

                if best == child_value:
                    movement = position           

        return (best, movement)
