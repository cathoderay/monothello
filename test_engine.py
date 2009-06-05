import unittest
from engine import *


class TestGameInitialization(unittest.TestCase):
    def test_players(self):
        game = Game()
        self.assertTrue(game.player1.color, "W" or "B")
        self.assertTrue(game.player2.color, "W" or "B")       
        self.assertTrue(game.player1.mode, "H" or "C")
        self.assertTrue(game.player2.mode, "H" or "C")


class TestStartGame(unittest.TestCase):
    def test_start_pieces(self):
        game = Game()
        game.start()
        self.assertEqual(game.board[(3, 3)], "B")
        self.assertEqual(game.board[(4, 4)], "B")
        self.assertEqual(game.board[(3, 4)], "W")
        self.assertEqual(game.board[(4, 3)], "W")


class TestCalculateScore(unittest.TestCase):
    def test_calculate_score(self):
        game = Game(p1_color="B")
        game.board[(0, 1)] = "B"
        game.board[(0, 2)] = "B"
        game.board[(0, 3)] = "B"
        game.board[(0, 4)] = "B"
        game.board[(0, 5)] = "B"
        game.board[(1, 3)] = "W"
        game.board[(1, 4)] = "W"
        game.board[(1, 5)] = "W"
        game.update_scores()
        self.assertEqual(game.player1.score, 5)
        self.assertEqual(game.player2.score, 3)


class TestGamePlay(unittest.TestCase):
    def test_black_player(self):
        game = Game(p1_color="B")
        game.start()
        game.play((3, 5))
        self.assertEqual(game.board[(3, 4)], "B")


class TestGameChangeTurn(unittest.TestCase):
    def test_alternate_players(self):
        game = Game()
        old_turn = game.turn
        game.change_turn()
        new_turn = game.turn
        if old_turn.color == "W":
            self.assertEqual(new_turn.color, "B")
        else:
            self.assertEqual(new_turn.color, "W")


class TestEndGame(unittest.TestCase):
    def test_false_end_game(self):
        game = Game()
        game.board[(2, 4)] = "B"
        game.board[(5, 2)] = "W"
        game.board[(1, 3)] = "W"
        self.assertEqual(game.test_end(), False)
        
    def test_end_game(self):
        game = Game()
        game.board[(2, 4)] = "B"
        game.board[(5, 2)] = "W"
        game.board[(1, 7)] = "W"
        self.assertEqual(game.test_end(), True)


class TestCountPieces(unittest.TestCase):
    def test_10_blacks_2_whites(self):
        board = Board()
        board[(0, 1)] = "B"
        board[(0, 2)] = "B"
        board[(0, 3)] = "B"
        board[(0, 4)] = "B"
        board[(0, 5)] = "B"
        board[(0, 6)] = "B"
        board[(1, 0)] = "B"
        board[(1, 1)] = "B"
        board[(1, 2)] = "B"
        board[(1, 3)] = "B"
        board[(6, 6)] = "W"
        board[(7, 7)] = "W"
        self.assertEqual(board.count_pieces("B"), 10)
        self.assertEqual(board.count_pieces("W"), 2)


class TestPlayablePositions(unittest.TestCase):
    def test_6_valid_positions(self):
        board = Board()
        board[(2, 2)] = "B"
        board[(3, 2)] = "W"
        board[(2, 3)] = "W"
        board[(3, 3)] = "B"
        board[(2, 4)] = "B"
        board[(4, 4)] = "W"
        turn = "W"
        self.assertEqual(board.valid_positions(turn), 
                         set([(1, 1), (2, 1), (1, 2), (4, 3), (2, 5), (3, 4)]))

    def test_0_valid_positions(self):
        board = Board()
        board[(0, 0)] = "W"
        board[(0, 1)] = "B"
        board[(0, 5)] = "W"
        turn = "B"
        self.assertEqual(board.valid_positions(turn), set([]))
    

class TestValidPosition(unittest.TestCase):
    def test_invalid_position(self):
        board = Board()
        board[(1, 1)] = "W"
        board[(2, 4)] = "W"
        board[(5, 2)] = "B"
        position = (6, 6)
        turn = "W"
        self.assertEqual(board.is_valid_position(position, turn), False)
           
    def test_valid_west(self):
        board = Board()
        board[(0, 0)] = "B"
        board[(0, 1)] = "W"
        position = (0, 2)
        turn = "B"
        self.assertEqual(board.is_valid_position(position, turn), True)

    def test_valid_east(self):
        board = Board()
        board[(0, 2)] = "B"
        board[(0, 1)] = "W"
        position = (0, 0)
        turn = "B"
        self.assertEqual(board.is_valid_position(position, turn), True) 

    def test_valid_east2(self):
        board = Board()
        board[(1, 1)] = "W"
        board[(1, 2)] = "W"
        board[(1, 3)] = "B"
        position = (1, 0)
        turn = "B"
        self.assertEqual(board.is_valid_position(position, turn), True)

    def test_valid_north(self):
        board = Board()
        board[(3, 2)] = "B"
        board[(4, 2)] = "W"
        position = (5, 2)
        turn = "B"
        self.assertEqual(board.is_valid_position(position, turn), True) 

    def test_valid_south(self):
        board = Board()        
        board[(5, 2)] = "B"
        board[(4, 2)] = "W"
        position = (3, 2)
        turn = "B"
        self.assertEqual(board.is_valid_position(position, turn), True) 

    def test_valid_northeast(self):
        board = Board()
        board[(3, 7)] = "B"
        board[(4, 6)] = "W"
        position = (5, 5)
        turn = "B"
        self.assertEqual(board.is_valid_position(position, turn), True) 

    def test_valid_southwest(self):
        board = Board()
        board[(5, 5)] = "B"
        board[(4, 6)] = "W"
        position = (3, 7)
        turn = "B"
        self.assertEqual(board.is_valid_position(position, turn), True) 
    
    def test_valid_northwest(self):
        board = Board()
        board[(3, 5)] = "B"
        board[(4, 6)] = "W"
        position = (5, 7)
        turn = "B"
        self.assertEqual(board.is_valid_position(position, turn), True)

    def test_valid_southeast(self):
        board = Board()
        board[(5, 7)] = "B"
        board[(4, 6)] = "W"
        position = (3, 5)
        turn = "B"
        self.assertEqual(board.is_valid_position(position, turn), True)

    def test_valid_configuration(self):
        board = Board()
        board[(3, 2)] = "W"
        board[(2, 3)] = "B"
        board[(3, 3)] = "B"
        board[(3, 4)] = "W"
        board[(4, 3)] = "B"
        board[(4, 4)] = "B"
        board[(5, 3)] = "B"
        position = (3, 5)
        turn = "W"
        self.assertEqual(board.is_valid_position(position, turn), False)


class TestMove(unittest.TestCase):
    def test_move_west(self):
        board = Board()
        board[(0, 0)] = "B"
        board[(0, 1)] = "W"
        board[(0, 2)] = "W"
        board[(0, 3)] = "W"
        turn = "B"
        board.move((0, 4), turn)
        self.assertEqual(board[(0, 0)], "B")
        self.assertEqual(board[(0, 1)], "B")
        self.assertEqual(board[(0, 2)], "B")
        self.assertEqual(board[(0, 3)], "B")
        self.assertEqual(board[(0, 4)], "B")

    def test_move_east(self):
        board = Board()
        board[(0, 2)] = "B"
        board[(0, 1)] = "W"
        turn = "B"
        board.move((0, 0), turn)
        self.assertEqual(board[(0, 1)], "B")        
    
    def test_move_north(self):
        board = Board()
        turn = "B"
        board[(3, 2)] = "B"
        board[(4, 2)] = "W"
        board.move((5, 2), turn)
        self.assertEqual(board[(4, 2)], "B")
    
    def test_move_south(self):
        board = Board()
        board[(5, 2)] = "B"
        board[(4, 2)] = "W"
        turn = "B"
        board.move((3, 2), turn)
        self.assertEqual(board[(3, 2)], "B")

    def test_move_northeast(self):
        board = Board()
        board[(3, 7)] = "B"
        board[(4, 6)] = "W"
        turn = "B"
        board.move((5, 5), turn)
        self.assertEqual(board[(4, 6)], "B")        
    
    def test_move_southwest(self):
        board = Board()       
        board[(5, 5)] = "B"
        board[(4, 6)] = "W"
        turn = "B"
        board.move((3, 7), turn)
        self.assertEqual(board[(4, 6)], "B")       
    
    def test_move_northwest(self):
        board = Board()
        board[(3, 5)] = "B"
        board[(4, 6)] = "W"
        turn = "B"        
        board.move((5, 7), turn)       
        self.assertEqual(board[(4, 6)], "B")        

    def test_move_southeast(self):
        board = Board()
        board[(5, 7)] = "B"
        board[(4, 6)] = "W"
        turn = "B"
        board.move((3, 5), turn)
        self.assertEqual(board[(4, 6)], "B")        
        

if __name__ == "__main__":
    unittest.main()
