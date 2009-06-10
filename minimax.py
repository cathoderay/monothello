from copy import copy
import random

from util import *
from heuristics import *


PLAYER = "W"
INFINITUM = 100000000000000000000000000000000000000000000


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


def minimax(board, depth, turn, heuristic):
    if depth == 0 or end_game(board):
        value = heuristic(board, PLAYER)
        return (heuristic(board, PLAYER), None)
    else:
        movement = None
        if not has_valid_position(board, turn):
            child = copy(board)
            return (minimax(child, depth-1, change_turn(turn), heuristic)[0], movement)
        else:
            if is_max(turn):
                best = -INFINITUM
            else:
                best = INFINITUM
            valid = valid_positions(board, turn)
            ties = []
            for position in valid:
                child = copy(board)
                move(child, position, turn)
                child_value = minimax(child, depth-1, change_turn(turn), heuristic)[0]
                del(child)

                if is_max(turn):
                    if best == child_value:
                        ties.append((best, position))
                    elif child_value > best:
                        best = child_value
                        ties = [(best, position)]             
                else:
                    if best == child_value:
                        ties.append((best, position))
                    elif child_value < best:
                        best = child_value
                        ties = [(best, position)]             
            best, movement = random.choice(ties)
            return (best, movement)
