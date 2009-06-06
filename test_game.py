import unittest
from game import *


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
        

if __name__ == "__main__":
    unittest.main()
