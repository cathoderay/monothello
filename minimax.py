import random
from engine import *

def ingenuos(board, turn):
    return random.choice(list(board.valid_positions(turn)))


def minimax(board, depth, turn):
    pass
