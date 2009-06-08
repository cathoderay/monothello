import matplotlib

from game import *
from util import *
import graphics
import minimax


def play_game(game, heuristic1, heuristic2):
    while not end_game(game.board):
        turn = game.turn.color
        board = game.board
        if has_valid_position(board, turn):
            minimax.PLAYER = turn
            if turn == "B":
                position = minimax.minimax(board, 1, turn, heuristic1)[1]
            else:
                position = minimax.minimax(board, 1, turn, heuristic2)[1]

            game.play(position)
        else:
            game.change_turn()
    return game.winning_side(formatted=False)


def run(p1_name, heuristic1, p2_name, heuristic2, times):
    rounds = times
    #black
    p1_color = "B"
    p1_win = 0

    #white
    p2_color = "W"
    p2_win = 0

    ties = 0

    for i in range(rounds):
        print 'Started game %s' % i
        game = Game(p1_color="B", p1_mode="C", p2_mode="C")
        game.start()
        winner = play_game(game, heuristic1, heuristic2)
        if winner == p1_color:
            p1_win += 1
            print '>>>>>>>>>>>>>>>>>>> Black win!'
        elif winner == p2_color:
            p2_win += 1
            print '>>>>>>>>>>>>>>>>>>> White win!'
        else:
            print 'Tie.'
            ties += 1
        print 'finished game %s' % i


    print 'After %s rounds:\n' % rounds
    print '%s: %s ' % (p1_name, p1_win)
    print '%s: %s' % (p2_name, p2_win)
    print 'ties: %s' % ties
    print 'Probabilities:'
    print '%s: %s' % (p1_name, str(p1_win/float(rounds)))
    print '%s: %s' % (p2_name, str(p2_win/float(rounds)))
    print 'ties: %s' % str(ties/float(rounds))

    graphics.plot(p1_name, p1_win, p2_name, p2_win, ties)    


if __name__ == "__main__":
    run(p1_name="Greedy",
        heuristic1=minimax.greedy, 
        p2_name="Posicional",
        heuristic2=minimax.posicional, 
        times=20)
