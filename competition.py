from game import *
from util import *
import minimax
import matplotlib


def play_game(game):
    while not end_game(game.board):
        turn = game.turn.color
        board = game.board
        if has_valid_position(board, turn):
            minimax.PLAYER = turn
            if turn == "B":
                position = minimax.minimax(board, 1, turn, minimax.posicional)[1]
            else:
                position = minimax.minimax(board, 1, turn, minimax.greedy)[1]

            game.play(position)
        else:
            game.change_turn()

    return game.winning_side(formatted=False)            


def run(times):
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
        winner = play_game(game)
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
    print 'p1: %s ' % p1_win
    print 'p2: %s' % p2_win
    print 'ties: %s' % ties
    print 'Probabilities:'
    print 'fp1: %s' % str(p1_win/float(rounds))
    print 'fp2: %s' % str(p2_win/float(rounds))
    print 'ties: %s' % str(ties/float(rounds))


if __name__ == "__main__":
    run(200)
