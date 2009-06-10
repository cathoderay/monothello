from util import *


def baby(board, turn):
    return 0


def weak(board, turn):
    if turn == "W":
        return count_pieces(board, "W") - count_pieces(board, "B")
    else:
        return count_pieces(board, "B") - count_pieces(board, "W")


def greedy(board, turn):
    if turn == "W":
        return count_pieces(board, "W")
    else:
        return count_pieces(board, "B")


def posicional(board, turn):
    value = 0
    for i in range(8):
        for j in range(8):
            if board[(i, j)] == turn:
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


def marc_mandt_posicional(board, turn):
    value = 0
    for i in range(8):
        for j in range(8):
            if board[(i, j)] == turn:
                if (i == 0 and j == 0) or (i == 7 and j == 7) or \
                   (i == 0 and j == 7) or (i == 7 and j == 0):
                    value += 50
                elif (i == 3 and j == 3) or (i == 3 and j == 4) or \
                     (i == 4 and j == 3) or (i == 4 and j == 4):
                    pass
                elif (i == 0 and j == 1) or (i == 1 and j == 0) or \
                     (i == 7 and j == 1) or (i == 6 and j == 0) or \
                     (i == 0 and j == 6) or (i == 1 and j == 7) or \
                     (i == 7 and j == 6) or (i == 6 and j == 7):
                     value -= 1
                elif (i == 1 and j == 1) or (i == 6 and j == 6) or \
                     (i == 6 and j == 1) or (i == 1 and j == 6):
                     value -= 10
                elif (i == 0 and j == 2) or (i == 0 and j == 5) or \
                     (i == 7 and j == 2) or (i == 7 and j == 5) or \
                     (i == 2 and j == 0) or (i == 5 and j == 0) or \
                     (i == 2 and j == 7) or (i == 5 and j == 7):
                     value += 5
                elif (i == 0 and j == 3) or (i == 0 and j == 4) or \
                     (i == 7 and j == 3) or (i == 7 and j == 4) or \
                     (i == 3 and j == 0) or (i == 4 and j == 0) or \
                     (i == 3 and j == 7) or (i == 4 and j == 7):
                     value += 2
                else:
                     value += 1
    return value
