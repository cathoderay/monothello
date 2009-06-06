from copy import deepcopy
import random
from engine import *

PLAYER = "W"
INFINITUM = 100000000000000000000000000000000000000000000


def ingenuos(board, turn):
    return random.choice(list(board.valid_positions(turn)))


def heuristic1(board, turn):
    if turn == "W":
        return board.count_pieces("W") - board.count_pieces("B")
    else:
        return board.count_pieces("B") - board.count_pieces("W")        


def minimax(board, depth, turn, heuristic=heuristic1):
    if depth == 0 or board.end_game():
        return (heuristic1(board, PLAYER), None)
    else:
        valid_positions = board.valid_positions(turn)
        movement = None
        if turn == PLAYER:
            best = -INFINITUM
        else:
            best = INFINITUM

        if turn == "W":
            new_turn = "B"
        else:
            new_turn = "W"
        for position in valid_positions:
            copy_board = deepcopy(board)
            copy_board.move(position, turn)
            value = minimax(copy_board, depth-1, new_turn, heuristic)[0]

            if turn == PLAYER:
                if value >= best:
                    best = value
                    movement = position
            else:
                if value <= best:
                    best = value
        return (best, movement)
