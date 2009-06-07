from util import *


class Game():
    def __init__(self, p1_color="W", p1_mode="H", p2_mode="C"):
        if p1_color == "W":
            p2_color = "B"
        else:
            p2_color = "W"
        self.board = Board()
        self.player1 = Player(color=p1_color, mode=p1_mode)
        self.player2 = Player(color=p2_color, mode=p2_mode)
        self.turn = self.player1

    def start(self):
        """Put the initial pieces on the board and update the scores."""
        self.board[(3, 3)] = self.board[(4, 4)] = "B"
        self.board[(3, 4)] = self.board[(4, 3)] = "W"
        self.update_scores()
    
    def play(self, position):
        if is_valid_position(self.board, position, self.turn.color):
            move(self.board, position, self.turn.color)
            self.update_scores()
            self.change_turn()
            return True
        else:
            return False
    
    def update_scores(self):
        """Update the scores of the players."""
        self.player1.score = count_pieces(self.board, self.player1.color)
        self.player2.score = count_pieces(self.board, self.player2.color)
    
    def change_turn(self):
        """Pass the turn to the other player."""
        if self.turn ==	self.player1:
            self.turn = self.player2
        else:
            self.turn = self.player1

    def winning_side(self, formatted=True):
        """Return a string with the winning side."""        
        self.update_scores()
        if self.player1.score > self.player2.score:
            winning = self.player1.color
            if not formatted: return winning
        elif self.player1.score < self.player2.score:
            winning = self.player2.color
            if not formatted: return winning
        else:
            if not formatted: return None
            return "Tie."
        if winning == "W":
            return "White win!"
        else:
            return "Black win!"

    def test_end(self):
        """Return a bool.
        Check the end of the game.

        """
        return end_game(self.board)

    def __str__(self):
        string = "----------------------\n"
        string += "GAME\n"
        string += "-------\n"
        string += "Turn: %s\n" % self.turn.color
        string += "-------\n"
        string += self.player1.__str__()
        string += "-------\n"
        string += self.player2.__str__()
        string += "-------\n"
        string += "Board:\n"
        string += self.board.__str__()
        string += "----------------------\n"
        return string


class Player():
    def __init__(self, color, mode):
        self.color = color
        self.mode = mode
        self.score = 0

    def __str__(self):
        string = "Player:\n"
        string += "Color: %s\n" % self.color
        string += "Mode: %s\n" % self.mode
        string += "Score: %s\n" % self.score
        return string


class Board(dict):
    def __init__(self):

        for i in range(8):
            for j in range(8):
                self[(i, j)] = "E"

    def __str__(self):
        string = ""
        for i in range(8):
            a = ""
            for j in range(8):
                a += self[(i, j)]
            string += a + '\n'
        return string
