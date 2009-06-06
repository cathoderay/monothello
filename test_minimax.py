import unittest

import minimax
from game import Board

class TestHeuristic1(unittest.TestCase):
    def test_configuration1(self):
        minimax.PLAYER = "W"
        board = Board()
        board[(1, 0)] = "W"
        board[(1, 1)] = "W"
        board[(1, 2)] = "W"        
        board[(1, 3)] = "W"
        board[(1, 4)] = "W"        
        board[(1, 5)] = "W"
        board[(2, 4)] = "B"
        self.assertEqual(minimax.heuristic1(board), 6-1)

    def test_configuration2(self):
        minimax.PLAYER = "B"
        board = Board()
        board[(1, 0)] = "W"
        board[(1, 1)] = "W"
        board[(1, 2)] = "W"        
        board[(1, 3)] = "W"
        board[(1, 4)] = "W"        
        board[(1, 5)] = "W"
        board[(2, 4)] = "B"
        self.assertEqual(minimax.heuristic1(board), 1-6)     


if __name__ == "__main__":
    unittest.main()
