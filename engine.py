class Game():
    def __init__(self, p1_color="W", p1_mode="H", p2_mode="C", difficulty=0):
        if p1_color == "W":
            p2_color = "B"
        else:
            p2_color = "W"
        self.board = Board()
        self.player1 = Player(color=p1_color, mode=p1_mode)
        self.player2 = Player(color=p2_color, mode=p2_mode)
        self.turn = self.player1

    def start(self):
        """Put the initial pieces on the board."""
        self.board[(3, 3)] = self.board[(4, 4)] = "B"
        self.board[(3, 4)] = self.board[(4, 3)] = "W"
        self.update_scores()
    
    def play(self, position):
        if self.board.is_valid_position(position, self.turn.color):
            self.board.move(position, self.turn.color)
            self.update_scores()
            self.change_turn()
            return True
        else:
            return False
    
    def update_scores(self):
        """Update the scores of the players."""
        self.player1.score = self.board.count_pieces(self.player1.color)
        self.player2.score = self.board.count_pieces(self.player2.color)
    
    def change_turn(self):
        """Pass the turn to the other player."""
        if self.turn ==	self.player1:
            self.turn = self.player2
        else:
            self.turn = self.player1

    def test_end(self):
        """Return a bool.
        Check the end of the game.

        """
        return not self.board.has_valid_position("W") and not \
           self.board.has_valid_position("B")

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
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1), 
                           (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for i in range(8):
            for j in range(8):
                self[(i, j)] = "E"

    def count_pieces(self, color):
        """Count the pieces in the board of the given color."""
        sum = 0
        for i in range(8):
            for j in range(8):
                if self[(i, j)] == color:
                    sum += 1
        return sum

    def has_valid_position(self, turn):
        """Return if the turn has any valid position."""
        for i in range(8):
            for j in range(8):
                position = (i, j)
                if self.is_valid_position(position, turn):
                    return True
        return False

    def valid_positions(self, turn):
        """Return a set with all valid positions for the given turn."""
        valid = list()
        for i in range(8):
            for j in range(8):
                position = (i, j)
                if self.is_valid_position(position, turn):
                    valid.append(position)
        return set(valid)

    def is_valid_position(self, position, turn):
        """Return a bool.
        Check if the given position is valid for this turn.
        
        """
        if self[position] != "E": return False
        for direction in self.directions:
            between = 0
            i, j = position
            while True:
                try:
                    i += direction[0]
                    j += direction[1]
                    if self[(i, j)] == "E":
                        break
                    if self[(i, j)] != turn:
                        between += 1
                    elif between > 0:
                        return True
                    else:
                        break                    
                except KeyError:
                    break
        return False

    def move(self, position, turn):
        """Move to the given position a piece of the color of the turn."""
        to_change = []
        for direction in self.directions:
            between = 0
            i, j = position
            while True:
                try:
                    i += direction[0]
                    j += direction[1]
                    if self[(i, j)] == "E":
                        break
                    if self[(i, j)] != turn:
                        between += 1
                    elif between > 0:
                        x, y = position                        
                        for times in range(between+1):
                            to_change.append((x, y))
                            x += direction[0]
                            y += direction[1]
                        break
                    else:
                        break
                except KeyError:
                    break
        for item in to_change:
            self[item] = turn

    def __str__(self):
        string = ''
        for i in range(8):
            a = ''
            for j in range(8):
                a += self[(i, j)]
            string += a + '\n'
        return string
